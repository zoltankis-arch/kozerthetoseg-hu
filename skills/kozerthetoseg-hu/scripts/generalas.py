#!/usr/bin/env python3
"""A generált referenciák előállítása a TOML-adatokból.

Újraírja a references/ generált fájljait: szabalyok.md (a teljes
katalógus), szabaly-index.md, a csoportonkénti szabalyok-<csoport>.md,
ellenorzo-lista.md, forrasok.md és lefedettseg.md. Kétszer futtatva ugyanazt adja, mert nem tesz
bele időbélyeget, és minden listát rendez.

Használat:
    python scripts/generalas.py            # a fájlok újraírása
    python scripts/generalas.py --ellenoriz # csak megnézi, frissek-e
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kozos  # noqa: E402

FEJLEC = (
    "<!-- GENERÁLT FÁJL. Ne szerkeszd kézzel: a forrása az assets/adatok/ mappa "
    "TOML-fájljai. Újragenerálás: python scripts/generalas.py -->"
)
KOR_NEV = {"altalanos": "általános", "jogi": "csak jogi szövegnél"}
ELL_NEV = {"gepi": "gépi", "vegyes": "jelölt", "itelet": "olvasva"}
SULY_NEV = {"magas": "magas", "kozepes": "közepes", "alacsony": "alacsony"}


def horgony(azonosito: str) -> str:
    return azonosito.lower().replace("#", "-")


def tetel_hivatkozas(adatok: kozos.Adatok, tid: str) -> str:
    fid, _, szam = tid.partition("#")
    f = adatok.forrasok.get(fid)
    if not f:
        return tid
    tetel = next((t for t in f.adat.get("tetel", []) if t.get("azonosito") == tid), None)
    oldal = f", {kozos.oldal_jel(tetel['oldal'])}" if tetel and tetel.get("oldal") else ""
    return f"[{f.adat.get('rovid', fid)}{oldal}](forrasok.md#{horgony(tid)})"


def esc(szoveg: str) -> str:
    """Táblázatcellába: a függőleges vonal és a sortörés nem törheti el a táblát."""
    return str(szoveg).replace("|", "\\|").replace("\n", " ").strip()


def szabaly_blokk(a: kozos.Adatok, sid: str) -> list[str]:
    """Egy szabály részletes leírása Markdownban (a szabalyok.md és a csoportfájlok közös része)."""
    d = a.szabalyok[sid].adat
    s = [f'<a id="{sid.lower()}"></a>', ""]
    jel = " (visszavonva)" if d.get("allapot") == "visszavont" else ""
    s.append(f"### {sid} {d.get('cim', '')}{jel}")
    s.append("")
    if d.get("allapot") == "visszavont":
        s.append(f"Visszavonva, helyette: [{d.get('utod')}](szabalyok.md#{str(d.get('utod', '')).lower()}). "
                 f"Ok: {d.get('visszavonas_oka', 'nincs megadva')}")
        s.append("")
    s.append(f"Szabály: {d.get('szabaly', '')}")
    s.append("")
    s.append(f"Miért segít: {d.get('miert', '')}")
    s.append("")
    if d.get("kerdes"):
        s.append(f"Ellenőrző kérdés: {d['kerdes']}")
        s.append("")
    p = d.get("pelda", {})
    s.append(f"- Rossz: {p.get('rossz', '')}")
    s.append(f"- Jó: {p.get('jo', '')}")
    if p.get("megjegyzes"):
        s.append(f"- Megjegyzés a példához: {p['megjegyzes']}")
    s.append("")
    if d.get("kivetelek"):
        s.append("Kivételek:")
        s.append("")
        s.extend(f"- {k}" for k in d["kivetelek"])
        s.append("")
    sor = f"Kör: {KOR_NEV.get(d.get('alkalmazasi_kor', ''), d.get('alkalmazasi_kor', ''))}."
    sor += (f" Alapértelmezett súlyosság: {SULY_NEV.get(d.get('sulyossag', ''), d.get('sulyossag', ''))}."
            f" Ellenőrzés: {ELL_NEV.get(d.get('ellenorzes', ''), d.get('ellenorzes', ''))}.")
    if d.get("meres"):
        sor += " Mérés (meres.py): " + ", ".join(d["meres"]) + "."
    if d.get("minta"):
        sor += " Keresőminta: " + "; ".join(m.get("leiras", "") for m in d["minta"]) + "."
    s.append(sor)
    s.append("")
    forr = d.get("forrasok", [])
    if forr:
        s.append("Források: " + "; ".join(tetel_hivatkozas(a, t) for t in forr) + ".")
        s.append("")
    for e in d.get("elteres", []):
        s.append("Ha a források eltérnek: " + e.get("leiras", "") + " "
                 + "A skill döntése: " + e.get("dontes", "") + " ("
                 + "; ".join(tetel_hivatkozas(a, t) for t in e.get("forrasok", [])) + ")")
        s.append("")
    return s


def csoportositas(a: kozos.Adatok) -> dict[str, list[str]]:
    csoport_szab: dict[str, list[str]] = defaultdict(list)
    for sid in kozos.szabaly_sorrend(a.szabalyok):
        csoport_szab[a.szabalyok[sid].adat.get("csoport", "")].append(sid)
    return csoport_szab


def csoportfajl(c: str) -> str:
    return f"szabalyok-{c}.md"


def szabalyok_md(a: kozos.Adatok) -> str:
    verzio = a.katalogus.adat.get("verzio", "?") if a.katalogus else "?"
    aktiv = [s for s in a.szabalyok if a.szabalyok[s].adat.get("allapot") == "aktiv"]
    vissza = [s for s in a.szabalyok if a.szabalyok[s].adat.get("allapot") == "visszavont"]
    s = [FEJLEC, "", "# Szabálykatalógus", ""]
    s.append(f"Katalógusverzió: {verzio}. Aktív szabályok: {len(aktiv)}. Visszavont szabályok: {len(vissza)}.")
    s.append("")
    s.append(
        "Minden szabálynál: mit kér, miért segít az olvasónak, egy saját rossz és jó példa, "
        "a kivételek, és hogy melyik forrás mondja ki (oldalszámmal, a forrásleltár tételére mutatva). "
        "A „csak jogi szövegnél” jelölésű szabályokat a jogi modul alkalmazza."
    )
    s.append("")
    s.append("Ez a teljes katalógus egy fájlban, emberi olvasásra. A skill a tömör "
             "[szabaly-index.md](szabaly-index.md) fájlt és a csoportonkénti fájlokat használja.")
    s.append("")
    s.append("## Csoportok")
    s.append("")
    csoport_szab = csoportositas(a)
    for c, nev in kozos.CSOPORTOK.items():
        if csoport_szab.get(c):
            ids = csoport_szab[c]
            s.append(f"- [{nev}](#{c}): {', '.join(f'[{i}](#{i.lower()})' for i in ids)}")
    s.append("")
    for c, nev in kozos.CSOPORTOK.items():
        ids = csoport_szab.get(c)
        if not ids:
            continue
        s.append(f'<a id="{c}"></a>')
        s.append("")
        s.append(f"## {nev}")
        s.append("")
        for sid in ids:
            s.extend(szabaly_blokk(a, sid))
    return "\n".join(s).rstrip() + "\n"


def szabaly_index_md(a: kozos.Adatok) -> str:
    verzio = a.katalogus.adat.get("verzio", "?") if a.katalogus else "?"
    s = [FEJLEC, "", "# Szabályindex", ""]
    s.append(f"Katalógusverzió: {verzio}. Szabályonként egy sor. Először ezt olvasd el; "
             "a részleteket (példa, kivételek, források) csak azoknál a szabályoknál nyisd meg "
             "a csoportfájlban, amelyek a vizsgált szövegre vonatkoznak. Ellenőrzés: „gépi” = a meres.py "
             "megbízhatóan jelzi; „jelölt” = a meres.py jelöltet ad, olvasva kell dönteni; „olvasva” = csak olvasva "
             "ellenőrizhető.")
    s.append("")
    csoport_szab = csoportositas(a)
    for c, nev in kozos.CSOPORTOK.items():
        ids = csoport_szab.get(c)
        if not ids:
            continue
        s.append(f"## {nev}")
        s.append("")
        s.append(f"Részletek: [{csoportfajl(c)}]({csoportfajl(c)})")
        s.append("")
        s.append("| Szabály | Cím | Kör | Súlyosság | Ellenőrzés |")
        s.append("|---|---|---|---|---|")
        for sid in ids:
            d = a.szabalyok[sid].adat
            if d.get("allapot") == "visszavont":
                cim = f"{esc(d.get('cim', ''))} (visszavonva, helyette {d.get('utod')})"
            else:
                cim = esc(d.get("cim", ""))
            kor = "jogi" if d.get("alkalmazasi_kor") == "jogi" else "általános"
            sul = SULY_NEV.get(d.get("sulyossag", ""), "")
            ell = ELL_NEV.get(d.get("ellenorzes", ""), "")
            s.append(f"| [{sid}]({csoportfajl(c)}#{sid.lower()}) | {cim} | {kor} | {sul} | {ell} |")
        s.append("")
    return "\n".join(s).rstrip() + "\n"


def csoport_md(a: kozos.Adatok, c: str) -> str:
    nev = kozos.CSOPORTOK[c]
    s = [FEJLEC, "", f"# Szabályok: {nev}", ""]
    s.append("Az összes csoport: [szabaly-index.md](szabaly-index.md).")
    s.append("")
    for sid in csoportositas(a).get(c, []):
        s.extend(szabaly_blokk(a, sid))
    return "\n".join(s).rstrip() + "\n"


def szotar_md(a: kozos.Adatok) -> str:
    s = [FEJLEC, "", "# Közérthetőségi szótár", ""]
    s.append("Körülményes kifejezés és egyszerűbb megfelelője. A meres.py javaslatként jelzi a találatokat; "
             "átírásnál nézd meg a „Mikor ne cseréld” oszlopot is. Jogi kifejezést csak magyarázattal együtt cserélj.")
    s.append("")
    s.append("| Kifejezés | Javaslat | Szabály | Mikor ne cseréld | Forrás |")
    s.append("|---|---|---|---|---|")
    parok = a.szotar.adat.get("par", []) if a.szotar else []
    for p in sorted(parok, key=lambda x: (x.get("szabaly", ""), x.get("kifejezes", "").lower())):
        sid = p.get("szabaly", "")
        c = a.szabalyok[sid].adat.get("csoport", "") if sid in a.szabalyok else ""
        forr = "; ".join(tetel_hivatkozas(a, t) for t in p.get("forrasok", []))
        s.append(f"| {esc(p.get('kifejezes', ''))} | {esc(p.get('javaslat', ''))} | "
                 f"[{sid}]({csoportfajl(c)}#{sid.lower()}) | {esc(p.get('mikor_nem', ''))} | {forr} |")
    return "\n".join(s).rstrip() + "\n"


def ellenorzo_lista_md(a: kozos.Adatok) -> str:
    s = [FEJLEC, "", "# Ellenőrző lista", ""]
    s.append("Minden aktív szabályhoz egy kérdés. Ha a válasz igen, a szöveg megfelel a szabálynak; "
             "ha nem, nézd meg a szabályt. A „jogi” jelölésű kérdések csak jogi szövegnél érvényesek. "
             "Amelyik csoport a szövegre nem vonatkozik (például nyomtatvány, táblázat), azt hagyd ki.")
    s.append("")
    csoport_szab = csoportositas(a)
    for c, nev in kozos.CSOPORTOK.items():
        ids = [i for i in csoport_szab.get(c, []) if a.szabalyok[i].adat.get("allapot") == "aktiv"]
        if not ids:
            continue
        s.append(f"## {nev}")
        s.append("")
        for sid in ids:
            d = a.szabalyok[sid].adat
            jogi = " (jogi)" if d.get("alkalmazasi_kor") == "jogi" else ""
            s.append(f"- [ ] {d.get('kerdes', '')}{jogi} [{sid}]({csoportfajl(c)}#{sid.lower()})")
        s.append("")
    return "\n".join(s).rstrip() + "\n"


def forrasok_md(a: kozos.Adatok) -> str:
    s = [FEJLEC, "", "# Forráskatalógus és forrásleltár", ""]
    s.append(
        "A skill szabályai az alábbi forrásokra épülnek. Minden forrásnál a bibliográfiai adatok, "
        "a felhasználási feltétel, majd a leltár: a forrás minden szabálya, ajánlása, ellenőrzőlista-pontja, "
        "tilalma és példája saját szavakkal, oldalszámmal. A leltártétel vagy egy szabályra, vagy egy "
        "referenciafájl adott pontjára mutat, vagy indoklással ki van hagyva. Szövegrészt a leltár nem "
        "vesz át; a forrás eredetijét a megadott hivatkozáson lehet elolvasni."
    )
    s.append("")
    s.append("| Forrás | Prioritás | Tételek |")
    s.append("|---|---|---|")
    for fid in sorted(a.forrasok, key=lambda x: (a.forrasok[x].adat.get("prioritas", "Z"), x)):
        d = a.forrasok[fid].adat
        s.append(f"| [{esc(d.get('rovid', fid))}](#{fid}) {esc(d.get('cim', ''))} | {d.get('prioritas', '')} "
                 f"| {len(d.get('tetel', []))} |")
    s.append("")
    for fid in sorted(a.forrasok, key=lambda x: (a.forrasok[x].adat.get("prioritas", "Z"), x)):
        d = a.forrasok[fid].adat
        s.append(f'<a id="{fid}"></a>')
        s.append("")
        s.append(f"## {d.get('rovid', fid)}: {d.get('cim', '')}")
        s.append("")
        s.append(f"- Azonosító: `{fid}`")
        s.append(f"- Hivatkozás: {d.get('hivatkozas', '')}")
        if d.get("url"):
            s.append(f"- Elérhetőség: {d['url']}")
        if d.get("doi"):
            s.append(f"- DOI: {d['doi']}")
        if d.get("isbn"):
            s.append(f"- ISBN: {d['isbn']}")
        s.append(f"- Felhasználási feltétel: {d.get('licenc', '')}")
        s.append(f"- Feldolgozott kiadás: {d.get('kiadas', '')}")
        s.append(f"- Oldalszámozás a leltárban: {d.get('oldalszamozas', '')}")
        s.append(f"- Feldolgozva: {d.get('feldolgozas_datuma', '')}, "
                 f"{'teljesen' if d.get('feldolgozottsag', 'teljes') == 'teljes' else 'részlegesen'}")
        s.append(f"- Prioritás: {d.get('prioritas', '')}")
        if d.get("megjegyzes"):
            s.append(f"- Megjegyzés: {d['megjegyzes']}")
        s.append("")
        fejezetek = {f["azonosito"]: f for f in d.get("fejezet", [])}
        tetelek_fejezetenkent: dict[str, list[dict]] = defaultdict(list)
        for t in d.get("tetel", []):
            tetelek_fejezetenkent[t.get("fejezet", "")].append(t)
        for fej_id, fej in fejezetek.items():
            s.append(f"### {fej.get('cim', '')} ({kozos.oldal_jel(fej.get('oldal', ''))})")
            s.append("")
            ts = tetelek_fejezetenkent.get(fej_id, [])
            if not ts:
                s.append(f"Nincs leltártétel. Ok: {fej.get('tetel_nelkul', 'nincs megadva')}")
                s.append("")
                continue
            s.append("| Tétel | Oldal | Fajta | Tartalom | Leképezés |")
            s.append("|---|---|---|---|---|")
            for t in ts:
                tid = t.get("azonosito", "")
                fajta, cel = kozos.lekepezes(t)
                if fajta == "szabalyok":
                    lek = ", ".join(f"[{x}](szabalyok.md#{x.lower()})" for x in cel)
                elif fajta == "referencia":
                    fajl, _, anc = str(cel).partition("#")
                    lek = f"[{Path(fajl).name}#{anc}]({Path(fajl).name}#{anc})"
                elif fajta == "kihagyva":
                    lek = "kihagyva: " + esc(cel)
                else:
                    lek = "HIBÁS LEKÉPEZÉS"
                s.append(f'| <a id="{horgony(tid)}"></a>{tid.split("#")[1]} | {esc(t.get("oldal", ""))} '
                         f"| {kozos.TETEL_TIPUSOK.get(t.get('tipus', ''), t.get('tipus', ''))} "
                         f"| {esc(t.get('tartalom', ''))} | {lek} |")
            s.append("")
    return "\n".join(s).rstrip() + "\n"


def lefedettseg_md(a: kozos.Adatok) -> str:
    s = [FEJLEC, "", "# Lefedettség", ""]
    s.append(
        "Ez a fájl gépileg mutatja meg, hogy a forrásleltár minden tétele célba ért-e: szabályba, "
        "referenciafájlba, vagy indokolt kihagyásba. Az „összevont” oszlop azokat a tételeket számolja, "
        "amelyek olyan szabályra mutatnak, amelyet más forrás is kimond."
    )
    s.append("")
    szabaly_forrasai: dict[str, set[str]] = defaultdict(set)
    for fid, _, t, _ in a.tetelek():
        fajta, cel = kozos.lekepezes(t)
        if fajta == "szabalyok":
            for sid in cel:
                szabaly_forrasai[sid].add(fid)
    s.append("| Forrás | Tételek | Szabályba | ebből összevont | Referenciába | Kihagyva | Leképezetlen |")
    s.append("|---|---|---|---|---|---|---|")
    ossz = Counter()
    for fid in sorted(a.forrasok, key=lambda x: (a.forrasok[x].adat.get("prioritas", "Z"), x)):
        c = Counter()
        for t in a.forrasok[fid].adat.get("tetel", []):
            fajta, cel = kozos.lekepezes(t)
            c["tetel"] += 1
            if fajta == "szabalyok":
                c["szabaly"] += 1
                if any(len(szabaly_forrasai[x]) > 1 for x in cel):
                    c["osszevont"] += 1
            elif fajta == "referencia":
                c["referencia"] += 1
            elif fajta == "kihagyva":
                c["kihagyva"] += 1
            else:
                c["hibas"] += 1
        ossz.update(c)
        s.append(f"| [{esc(a.forrasok[fid].adat.get('rovid', fid))}](forrasok.md#{fid}) | {c['tetel']} | "
                 f"{c['szabaly']} | {c['osszevont']} | {c['referencia']} | {c['kihagyva']} | {c['hibas']} |")
    s.append(f"| Összesen | {ossz['tetel']} | {ossz['szabaly']} | {ossz['osszevont']} | "
             f"{ossz['referencia']} | {ossz['kihagyva']} | {ossz['hibas']} |")
    s.append("")
    s.append("## Fejezetek")
    s.append("")
    s.append("Minden forrás minden fejezete: hány tétel került belőle a leltárba. Ha egy sem, az ok a fejezetnél áll.")
    s.append("")
    for fid in sorted(a.forrasok, key=lambda x: (a.forrasok[x].adat.get("prioritas", "Z"), x)):
        d = a.forrasok[fid].adat
        db = Counter(t.get("fejezet") for t in d.get("tetel", []))
        s.append(f"### {d.get('rovid', fid)}")
        s.append("")
        if d.get("feldolgozottsag") == "reszleges":
            s.append("Részlegesen feldolgozott forrás: csak az alábbi fejezetek kerültek leltárba.")
            s.append("")
        for f in d.get("fejezet", []):
            n = db.get(f["azonosito"], 0)
            if n:
                s.append(f"- {f['cim']} ({kozos.oldal_jel(f['oldal'])}): {n} tétel")
            else:
                s.append(f"- {f['cim']} ({kozos.oldal_jel(f['oldal'])}): nincs tétel. {f.get('tetel_nelkul', '')}")
        s.append("")
    s.append("## Szabályok forrásai")
    s.append("")
    s.append("| Szabály | Források száma | Leltártételek | Eltérés jelölve |")
    s.append("|---|---|---|---|")
    for sid in sorted(a.szabalyok):
        d = a.szabalyok[sid].adat
        if d.get("allapot") != "aktiv":
            continue
        s.append(f"| [{sid}](szabalyok.md#{sid.lower()}) {esc(d.get('cim', ''))} | "
                 f"{len({x.split('#')[0] for x in d.get('forrasok', [])})} | {len(d.get('forrasok', []))} | "
                 f"{'igen' if d.get('elteres') else ''} |")
    s.append("")
    return "\n".join(s).rstrip() + "\n"


CELOK = {
    "szabalyok.md": szabalyok_md,
    "szabaly-index.md": szabaly_index_md,
    "ellenorzo-lista.md": ellenorzo_lista_md,
    "szotar.md": szotar_md,
    "forrasok.md": forrasok_md,
    "lefedettseg.md": lefedettseg_md,
}


def generalt_tartalmak(adatok: kozos.Adatok) -> dict[str, str]:
    t = {nev: fv(adatok) for nev, fv in CELOK.items()}
    for c in kozos.CSOPORTOK:
        t[csoportfajl(c)] = csoport_md(adatok, c)
    return t


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="generalas.py",
        description="A references/ generált fájljainak előállítása az assets/adatok/ TOML-fájljaiból.",
    )
    p.add_argument("--gyoker", type=Path, default=kozos.SKILL_GYOKER,
                   help="a skill mappája (alapérték: a szkript fölötti mappa)")
    p.add_argument("--ellenoriz", action="store_true",
                   help="nem ír, csak jelzi, ha egy generált fájl elavult (kilépési kód: 1)")
    a = p.parse_args(argv)
    adatok = kozos.adatok_betolt(a.gyoker)
    if adatok.olvasasi_hibak:
        for h in adatok.olvasasi_hibak:
            print(f"Hiba: {h.szoveg()}", file=sys.stderr)
        print("Hiba: az adatfájlok nem olvashatók, a generálás leállt.", file=sys.stderr)
        return 1
    tartalmak = generalt_tartalmak(adatok)
    ref = a.gyoker / "references"
    elavult = []
    for nev, tartalom in tartalmak.items():
        ut = ref / nev
        regi = ut.read_text(encoding="utf-8") if ut.exists() else None
        if regi != tartalom:
            elavult.append(nev)
            if not a.ellenoriz:
                ut.write_text(tartalom, encoding="utf-8")
    if a.ellenoriz:
        if elavult:
            for nev in elavult:
                print(f"Hiba: references/{nev} elavult; futtasd: python scripts/generalas.py", file=sys.stderr)
            return 1
        print("A generált fájlok frissek.")
        return 0
    print("Frissítve: " + (", ".join(f"references/{n}" for n in elavult) if elavult else "nincs változás"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
