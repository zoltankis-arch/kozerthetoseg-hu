#!/usr/bin/env python3
"""Teljességi és konzisztencia-ellenőrzés.

Megnézi a sémákat, az azonosítókat, a forrásleltár lefedettségét, a
szabályok forrásait, a hivatkozásokat, a parancsfájlok szerkezetét, az
evalokat és azt, hogy a generált referenciák frissek-e. Minden hibánál
megmondja, melyik fájl melyik sora a hibás.

Használat:
    python scripts/ellenorzes.py
    python scripts/ellenorzes.py --gyoker /út/a/skillhez

Kilépési kód: 0, ha nincs hiba; 1, ha van.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generalas  # noqa: E402
import kozos  # noqa: E402
import meres  # noqa: E402

SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
SKILL_SOROK_MAX = 500


class Naplo:
    def __init__(self, gyoker: Path):
        self.gyoker = gyoker
        self.hibak: list[str] = []

    def hiba(self, fajl: Path, sor: int | None, uzenet: str) -> None:
        try:
            nev = str(fajl.relative_to(self.gyoker.parent))
        except ValueError:
            nev = str(fajl)
        self.hibak.append(f"{nev}:{sor}: {uzenet}" if sor else f"{nev}: {uzenet}")


def sema_hibak(n: Naplo, f: kozos.TomlFajl, sema: dict, tablak: tuple[str, ...]) -> None:
    for ut, uzenet in kozos.sema_ellenoriz(f.adat, sema):
        sor = None
        m = re.match(r"^([a-z_]+)\[(\d+)\](?:\.([a-z_]+))?", ut)
        if m and m.group(1) in tablak:
            sor = f.sor(m.group(3), tabla=m.group(1), index=int(m.group(2)))
        elif ut.startswith("pelda."):
            sor = f.sor(ut.split(".")[1], tabla="pelda")
        else:
            sor = f.sor(ut.split(".")[0].split("[")[0]) if ut else None
        n.hiba(f.utvonal, sor, uzenet)


def kitoltendo(n: Naplo, f: kozos.TomlFajl) -> None:
    for i, s in enumerate(f.szoveg.splitlines(), 1):
        if kozos.KITOLTENDO in s and not s.lstrip().startswith("#"):
            n.hiba(f.utvonal, i, f"kitöltetlen sablonmező ({kozos.KITOLTENDO})")


def horgonyok(md: str) -> set[str]:
    """Explicit <a id> horgonyok és a GitHub-szerű címsorhorgonyok."""
    h = set(re.findall(r'<a id="([^"]+)"', md))
    for cim in re.findall(r"^#{1,6}\s+(.+)$", md, flags=re.MULTILINE):
        slug = unicodedata.normalize("NFC", cim.strip().lower())
        slug = re.sub(r"[^\w\- ]", "", slug)
        h.add(slug.replace(" ", "-"))
    return h


def ellenoriz_adatok(n: Naplo, a: kozos.Adatok) -> None:
    for h in a.olvasasi_hibak:
        n.hiba(h.fajl, h.sor, h.uzenet)
    gy = a.gyoker
    szabaly_sema = kozos.sema_betolt("szabaly.schema.json", gy)
    forras_sema = kozos.sema_betolt("forras.schema.json", gy)

    # Katalógus
    if a.katalogus:
        v = a.katalogus.adat.get("verzio", "")
        if not SEMVER.match(str(v)):
            n.hiba(a.katalogus.utvonal, a.katalogus.sor("verzio"),
                   "a katalógus verziója SemVer alakú legyen (pl. 1.0.0)")

    # Szabályok: séma, fájlnév, folytonos azonosítók
    for sid, f in a.szabalyok.items():
        sema_hibak(n, f, szabaly_sema, ("elteres", "minta"))
        kitoltendo(n, f)
        if f.adat.get("azonosito") != sid:
            n.hiba(f.utvonal, f.sor("azonosito"),
                   f"az azonosító ({f.adat.get('azonosito')}) nem egyezik a fájlnévvel ({sid})")
    szamok = sorted(int(s[1:]) for s in a.szabalyok if kozos.SZABALY_MINTA.match(s))
    for x in range(1, (szamok[-1] if szamok else 0) + 1):
        if x not in szamok:
            n.hiba(gy / "assets" / "adatok" / "szabalyok", None,
                   f"hiányzik a K{x:03d} szabály. Szabályt nem törlünk: visszavonjuk (allapot = \"visszavont\").")

    # Források: séma, fájlnév, tételazonosítók, fejezetek
    minden_tetel: dict[str, tuple[str, int, dict, kozos.TomlFajl]] = {}
    for fid, f in a.forrasok.items():
        sema_hibak(n, f, forras_sema, ("tetel", "fejezet"))
        kitoltendo(n, f)
        if f.adat.get("azonosito") != fid:
            n.hiba(f.utvonal, f.sor("azonosito"),
                   f"az azonosító ({f.adat.get('azonosito')}) nem egyezik a fájlnévvel ({fid})")
        fejezetek = {}
        for i, fej in enumerate(f.adat.get("fejezet", [])):
            fa = fej.get("azonosito")
            if fa in fejezetek:
                n.hiba(f.utvonal, f.sor("azonosito", "fejezet", i), f"ismétlődő fejezetazonosító: {fa}")
            fejezetek[fa] = i
        hasznalt_fejezet = set()
        for i, t in enumerate(f.adat.get("tetel", [])):
            tid = t.get("azonosito", "")
            m = kozos.TETEL_MINTA.match(tid)
            if m and m.group(1) != fid:
                n.hiba(f.utvonal, f.sor("azonosito", "tetel", i),
                       f"a tétel azonosítója ({tid}) nem ennek a forrásnak az előtagjával kezdődik ({fid}#)")
            if tid in minden_tetel:
                n.hiba(f.utvonal, f.sor("azonosito", "tetel", i), f"ismétlődő tételazonosító: {tid}")
            minden_tetel[tid] = (fid, i, t, f)
            if t.get("fejezet") not in fejezetek:
                n.hiba(f.utvonal, f.sor("fejezet", "tetel", i),
                       f"a(z) {tid} tétel nem létező fejezetre mutat: {t.get('fejezet')}")
            hasznalt_fejezet.add(t.get("fejezet"))
        for fa, i in fejezetek.items():
            fej = f.adat["fejezet"][i]
            if fa not in hasznalt_fejezet and not fej.get("tetel_nelkul"):
                n.hiba(f.utvonal, f.sor("cim", "fejezet", i),
                       f"a(z) „{fej.get('cim')}” fejezetből nincs leltártétel, és a tetel_nelkul mező sem mondja meg, miért")

    # Szótár: séma, regex, létező szabály és leltártétel
    if a.szotar:
        sf = a.szotar
        sema_hibak(n, sf, kozos.sema_betolt("szotar.schema.json", gy), ("par",))
        for j, p in enumerate(sf.adat.get("par", [])):
            try:
                re.compile(p.get("regex", ""))
            except re.error as e:
                n.hiba(sf.utvonal, sf.sor("regex", "par", j), f"a(z) „{p.get('kifejezes')}” regexe hibás: {e}")
            if p.get("szabaly") not in a.szabalyok:
                n.hiba(sf.utvonal, sf.sor("szabaly", "par", j), f"nem létező szabály: {p.get('szabaly')}")
            for tid in p.get("forrasok", []):
                if tid not in minden_tetel:
                    n.hiba(sf.utvonal, sf.sor("forrasok", "par", j), f"nem létező leltártételre hivatkozik: {tid}")

    # Leképezés: minden tétel célba ér
    visszautal: dict[str, set[str]] = defaultdict(set)
    for tid, (fid, i, t, f) in minden_tetel.items():
        fajta, cel = kozos.lekepezes(t)
        if fajta == "hibas":
            if cel:
                n.hiba(f.utvonal, f.sor("azonosito", "tetel", i),
                       f"a(z) {tid} tételnek pontosan egy leképezése legyen; most: {', '.join(cel)}")
            else:
                n.hiba(f.utvonal, f.sor("azonosito", "tetel", i),
                       f"a(z) {tid} tétel leképezetlen: adj meg szabalyok, referencia vagy kihagyva mezőt")
        elif fajta == "szabalyok":
            for sid in cel:
                if sid not in a.szabalyok:
                    n.hiba(f.utvonal, f.sor("szabalyok", "tetel", i), f"a(z) {tid} nem létező szabályra mutat: {sid}")
                elif a.szabalyok[sid].adat.get("allapot") == "visszavont":
                    utod = a.szabalyok[sid].adat.get("utod", "?")
                    n.hiba(f.utvonal, f.sor("szabalyok", "tetel", i),
                           f"a(z) {tid} visszavont szabályra mutat ({sid}); a helyes cél: {utod}")
                visszautal[sid].add(tid)
        elif fajta == "referencia":
            fajl, _, anc = str(cel).partition("#")
            ut = gy / fajl
            if not ut.is_file():
                n.hiba(f.utvonal, f.sor("referencia", "tetel", i), f"a(z) {tid} nem létező fájlra mutat: {fajl}")
            elif anc not in horgonyok(ut.read_text(encoding="utf-8")):
                n.hiba(f.utvonal, f.sor("referencia", "tetel", i),
                       f"a(z) {tid} nem létező horgonyra mutat: {fajl}#{anc}")

    # Szabályok forrásai: létezzenek, és a két irány egyezzen
    for sid, f in a.szabalyok.items():
        d = f.adat
        forr = d.get("forrasok", [])
        if d.get("allapot") == "aktiv" and not forr:
            n.hiba(f.utvonal, f.sor("forrasok"), "aktív szabálynak legalább egy forrása legyen")
        for tid in forr:
            if tid not in minden_tetel:
                n.hiba(f.utvonal, f.sor("forrasok"), f"nem létező leltártételre hivatkozik: {tid}")
            elif tid not in visszautal.get(sid, set()):
                n.hiba(f.utvonal, f.sor("forrasok"),
                       f"a(z) {tid} tétel nem erre a szabályra mutat; a tétel leképezését is frissítsd")
        for tid in sorted(visszautal.get(sid, set()) - set(forr)):
            n.hiba(f.utvonal, f.sor("forrasok"),
                   f"a(z) {tid} tétel erre a szabályra mutat, de a szabály forrásai között nem szerepel")
        if d.get("allapot") == "visszavont":
            utod = d.get("utod")
            if not utod:
                n.hiba(f.utvonal, f.sor("allapot"), "visszavont szabálynál kötelező az utod mező")
            elif utod not in a.szabalyok or a.szabalyok[utod].adat.get("allapot") != "aktiv":
                n.hiba(f.utvonal, f.sor("utod"), f"az utód ({utod}) nem létező vagy nem aktív szabály")
        elif "utod" in d:
            n.hiba(f.utvonal, f.sor("utod"), "utod mező csak visszavont szabálynál állhat")
        for j, e in enumerate(d.get("elteres", [])):
            for tid in e.get("forrasok", []):
                if tid not in forr:
                    n.hiba(f.utvonal, f.sor("forrasok", "elteres", j),
                           f"az eltérésnél hivatkozott tétel ({tid}) nincs a szabály forrásai között")
        for j, mt in enumerate(d.get("minta", [])):
            try:
                re.compile(mt.get("regex", ""))
            except re.error as e:
                n.hiba(f.utvonal, f.sor("regex", "minta", j), f"a minta regexe hibás: {e}")
        if d.get("allapot") == "aktiv" and d.get("ellenorzes") in ("gepi", "vegyes"):
            szotarban = a.szotar and any(p.get("szabaly") == sid for p in a.szotar.adat.get("par", []))
            if not (d.get("meres") or d.get("minta") or szotarban):
                n.hiba(f.utvonal, f.sor("ellenorzes"),
                       "gépi vagy vegyes szabálynak legyen meres mezője, minta bejegyzése vagy szótárpárja; "
                       "különben az ellenorzes mező legyen „itelet”")
        for m in d.get("meres", []):
            if m not in meres.METRIKAK:
                n.hiba(f.utvonal, f.sor("meres"),
                       f"ismeretlen mérőszám: {m}; lehetséges: {', '.join(meres.METRIKAK)}")


def ellenoriz_skill_md(n: Naplo, gy: Path, a: kozos.Adatok) -> None:
    ut = gy / "SKILL.md"
    if not ut.is_file():
        n.hiba(ut, None, "hiányzik a SKILL.md")
        return
    szoveg = ut.read_text(encoding="utf-8")
    try:
        fm, torzs, torzs_kezdet = kozos.frontmatter(szoveg)
    except ValueError as e:
        n.hiba(ut, 1, str(e))
        return
    if fm.get("name") != gy.name:
        n.hiba(ut, 2, f"a name mező ({fm.get('name')}) egyezzen a mappanévvel ({gy.name})")
    leiras = fm.get("description", "")
    if not leiras or len(leiras) > 1024:
        n.hiba(ut, 3, f"a description 1 és 1024 karakter közötti legyen (most {len(leiras)})")
    if "---" in leiras:
        n.hiba(ut, 3, "a description nem tartalmazhat „---” jelsort")
    meta = fm.get("metadata", {})
    if not isinstance(meta, dict):
        n.hiba(ut, None, "a metadata kulcs–érték tábla legyen")
        meta = {}
    sor_meta = next((i for i, s in enumerate(szoveg.splitlines(), 1) if s.startswith("metadata:")), None)
    if not SEMVER.match(meta.get("version", "")):
        n.hiba(ut, sor_meta, "a metadata.version SemVer alakú legyen")
    if a.katalogus and meta.get("forraskatalogus") != str(a.katalogus.adat.get("verzio")):
        n.hiba(ut, sor_meta, f"a metadata.forraskatalogus ({meta.get('forraskatalogus')}) egyezzen az "
               f"assets/adatok/katalogus.toml verziójával ({a.katalogus.adat.get('verzio')})")
    torzs_sorok = torzs.splitlines()
    if len(torzs_sorok) > SKILL_SOROK_MAX:
        n.hiba(ut, None, f"a SKILL.md törzse {len(torzs_sorok)} sor; legfeljebb {SKILL_SOROK_MAX} lehet")
    becsult_token = len(torzs) // 4
    if becsult_token > 5000:
        n.hiba(ut, None, f"a SKILL.md törzse kb. {becsult_token} token; a javasolt felső határ 5000")

    # Parancstáblázat és parancsfájlok
    tablazat = {}
    for i, s in enumerate(szoveg.splitlines(), 1):
        m = re.match(r"^\|\s*`([a-z-]+)`\s*\|.*\]\((references/parancs-[a-z-]+\.md)\)", s)
        if m:
            tablazat[m.group(1)] = (m.group(2), i)
    fajlok = {p.stem.removeprefix("parancs-"): p for p in (gy / "references").glob("parancs-*.md")}
    for nev, (fajl, sor) in tablazat.items():
        if fajl != f"references/parancs-{nev}.md":
            n.hiba(ut, sor, f"a(z) `{nev}` parancs sora rossz fájlra mutat: {fajl}")
        if nev not in fajlok:
            n.hiba(ut, sor, f"a(z) `{nev}` parancshoz nincs references/parancs-{nev}.md")
    for nev, p in fajlok.items():
        if nev not in tablazat:
            n.hiba(p, None, f"a(z) `{nev}` parancs nem szerepel a SKILL.md parancstáblázatában")
    sablon = gy / "assets" / "sablonok" / "parancs.md"
    if sablon.is_file():
        elvart = re.findall(r"^## (.+)$", sablon.read_text(encoding="utf-8"), flags=re.MULTILINE)
        for nev, p in fajlok.items():
            van = re.findall(r"^## (.+)$", p.read_text(encoding="utf-8"), flags=re.MULTILINE)
            if van != elvart:
                n.hiba(p, None, "a parancsfájl szakaszai nem egyeznek a sablonnal "
                       f"(elvárt sorrend: {' / '.join(elvart)}; van: {' / '.join(van)})")
    else:
        n.hiba(sablon, None, "hiányzik a parancssablon")

    # Evalok: minden parancshoz legalább egy
    evp = gy / "evals" / "evals.json"
    if evp.is_file():
        try:
            ev = json.loads(evp.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            n.hiba(evp, e.lineno, f"hibás JSON: {e.msg}")
            ev = {"evals": []}
        lefedett = set()
        idk = set()
        for j, e in enumerate(ev.get("evals", [])):
            for k in ("id", "prompt", "expected_output", "expectations", "parancs"):
                if k not in e:
                    n.hiba(evp, None, f"a(z) {j + 1}. evalból hiányzik a(z) „{k}” mező")
            if e.get("id") in idk:
                n.hiba(evp, None, f"ismétlődő eval-azonosító: {e.get('id')}")
            idk.add(e.get("id"))
            for p in e.get("parancs", "").split(","):
                lefedett.add(p.strip())
            for fajl in e.get("files", []):
                if not (gy / fajl).is_file():
                    n.hiba(evp, None, f"a(z) {e.get('id')}. eval nem létező fájlra hivatkozik: {fajl}")
        for nev in fajlok:
            if nev not in lefedett:
                n.hiba(evp, None, f"a(z) `{nev}` parancshoz nincs eval")
    else:
        n.hiba(evp, None, "hiányzik az evals/evals.json")

    # Hivatkozások a SKILL.md-ben és a references/ fájljaiban
    for md in [ut, *sorted((gy / "references").glob("*.md"))]:
        tartalom = md.read_text(encoding="utf-8")
        for i, s in enumerate(tartalom.splitlines(), 1):
            for cel in LINK.findall(s):
                if re.match(r"^[a-z]+:", cel):
                    continue
                fajl, _, anc = cel.partition("#")
                celut = (md.parent / fajl) if fajl else md
                if not celut.exists():
                    n.hiba(md, i, f"nem létező fájlra mutató hivatkozás: {cel}")
                    continue
                if anc and celut.suffix == ".md" and anc not in horgonyok(celut.read_text(encoding="utf-8")):
                    n.hiba(md, i, f"nem létező horgonyra mutató hivatkozás: {cel}")
        if md != ut and md.parent == gy / "references":
            for i, s in enumerate(tartalom.splitlines(), 1):
                for cel in LINK.findall(s):
                    if cel.startswith("../references/"):
                        n.hiba(md, i, "a referenciafájlok egymásra a mappán belül hivatkozzanak")

    # Változásnapló: ha a skill a repóban él, a verziója szerepeljen benne
    changelog = gy.parent / "CHANGELOG.md"
    if changelog.is_file() and meta.get("version"):
        if f"## [{meta['version']}]" not in changelog.read_text(encoding="utf-8"):
            n.hiba(changelog, None, f"a CHANGELOG.md-ben nincs bejegyzés a(z) {meta['version']} verzióhoz")


def ellenoriz_generalt(n: Naplo, a: kozos.Adatok) -> None:
    if a.olvasasi_hibak:
        return
    for nev, tartalom in generalas.generalt_tartalmak(a).items():
        ut = a.gyoker / "references" / nev
        regi = ut.read_text(encoding="utf-8") if ut.exists() else None
        if regi != tartalom:
            sor = None
            if regi is not None:
                for i, (x, y) in enumerate(zip(regi.splitlines(), tartalom.splitlines()), 1):
                    if x != y:
                        sor = i
                        break
            n.hiba(ut, sor, "a generált fájl elavult; futtasd: python scripts/generalas.py")


def osszesites(a: kozos.Adatok) -> str:
    tetelek = list(a.tetelek())
    aktiv = sum(1 for s in a.szabalyok.values() if s.adat.get("allapot") == "aktiv")
    return (f"{len(a.forrasok)} forrás, {len(tetelek)} leltártétel, "
            f"{aktiv} aktív és {len(a.szabalyok) - aktiv} visszavont szabály")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="ellenorzes.py",
        description="Teljességi és konzisztencia-ellenőrzés: séma, azonosítók, lefedettség, hivatkozások.",
    )
    p.add_argument("--gyoker", type=Path, default=kozos.SKILL_GYOKER,
                   help="a skill mappája (alapérték: a szkript fölötti mappa)")
    a = p.parse_args(argv)
    gy = a.gyoker.resolve()
    if not (gy / "assets" / "adatok").is_dir():
        print(f"Hiba: a(z) {gy} nem a skill mappája (nincs assets/adatok).", file=sys.stderr)
        return 2
    n = Naplo(gy)
    adatok = kozos.adatok_betolt(gy)
    ellenoriz_adatok(n, adatok)
    ellenoriz_skill_md(n, gy, adatok)
    ellenoriz_generalt(n, adatok)
    if n.hibak:
        for h in n.hibak:
            print(h, file=sys.stderr)
        print(f"\n{len(n.hibak)} hiba. ({osszesites(adatok)})", file=sys.stderr)
        return 1
    print(f"Rendben: {osszesites(adatok)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
