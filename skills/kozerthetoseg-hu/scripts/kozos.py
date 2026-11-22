"""Közös segédfüggvények a kozerthetoseg-hu szkriptjeihez.

Csak a Python 3.11+ standard könyvtárát használja. A többi szkript innen
olvassa be a TOML-adatokat, innen validál a JSON Schema egy szűk
részhalmaza szerint, és innen keresi meg, melyik fájl melyik sorában van
egy adott kulcs.
"""

from __future__ import annotations

import json
import re
import sys
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

SKILL_GYOKER = Path(__file__).resolve().parent.parent

CSOPORTOK: dict[str, str] = {
    "cel-es-tartalom": "Cél és tartalom",
    "felepites": "Felépítés",
    "mondat": "Mondat",
    "szo": "Szó",
    "szerkezet": "Szerkezet",
    "megszolitas-es-hang": "Megszólítás és hang",
    "kinezet": "Kinézet",
    "szamok-es-jelek": "Helyesírás, számok és írásjelek",
    "tablazat-es-abra": "Táblázat és ábra",
    "nyomtatvany": "Nyomtatvány",
    "folyamat": "Írási folyamat és ellenőrzés",
}

TETEL_TIPUSOK: dict[str, str] = {
    "szabaly": "szabály",
    "ajanlas": "ajánlás",
    "tilalom": "tilalom",
    "ellenorzolista": "ellenőrzőlista-pont",
    "pelda": "előtte–utána példa",
    "meghatarozas": "meghatározás",
    "hatter": "háttér",
}

KITOLTENDO = "KITÖLTENDŐ"
SZABALY_MINTA = re.compile(r"^K\d{3}$")
FORRAS_MINTA = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TETEL_MINTA = re.compile(r"^([a-z0-9]+(?:-[a-z0-9]+)*)#(\d{3})$")


class AdatHiba(Exception):
    """Olvasási vagy formai hiba egy adatfájlban, fájl- és sorhivatkozással."""

    def __init__(self, fajl: Path, sor: int | None, uzenet: str):
        self.fajl = fajl
        self.sor = sor
        self.uzenet = uzenet
        super().__init__(self.szoveg())

    def szoveg(self) -> str:
        return hely(self.fajl, self.sor) + ": " + self.uzenet


def hely(fajl: Path, sor: int | None = None) -> str:
    """Fájl és sor egységes formában (fájl:sor), a skill gyökeréhez képest."""
    try:
        nev = str(fajl.relative_to(SKILL_GYOKER.parent))
    except ValueError:
        nev = str(fajl)
    return f"{nev}:{sor}" if sor else nev


@dataclass
class TomlFajl:
    utvonal: Path
    szoveg: str
    adat: dict

    def sor(self, kulcs: str | None = None, tabla: str | None = None,
            index: int | None = None) -> int | None:
        """Megkeresi, melyik sorban áll egy kulcs.

        Ha ``tabla`` és ``index`` meg van adva, a ``[[tabla]]`` blokkok közül
        az index-ediken belül keres; ha a kulcs nincs ott, a blokk fejlécének
        sorát adja vissza.
        """
        sorok = self.szoveg.splitlines()
        kezdet, veg = 0, len(sorok)
        if tabla is not None and index is not None:
            fejlecek = [i for i, s in enumerate(sorok)
                        if s.strip() in (f"[[{tabla}]]", f"[{tabla}]")]
            if index >= len(fejlecek):
                return None
            kezdet = fejlecek[index]
            kovetkezo = [i for i, s in enumerate(sorok)
                         if i > kezdet and s.strip().startswith("[")]
            veg = kovetkezo[0] if kovetkezo else len(sorok)
            if kulcs is None:
                return kezdet + 1
        elif tabla is not None:
            for i, s in enumerate(sorok):
                if s.strip() == f"[{tabla}]":
                    kezdet = i
                    kovetkezo = [j for j, t in enumerate(sorok)
                                 if j > i and t.strip().startswith("[")]
                    veg = kovetkezo[0] if kovetkezo else len(sorok)
                    break
        else:
            elso_tabla = [i for i, s in enumerate(sorok) if s.strip().startswith("[")]
            veg = elso_tabla[0] if elso_tabla else len(sorok)
        if kulcs is None:
            return None
        minta = re.compile(r"^\s*" + re.escape(kulcs) + r"\s*=")
        for i in range(kezdet, veg):
            if minta.match(sorok[i]):
                return i + 1
        return kezdet + 1 if tabla is not None else None


def toml_olvas(utvonal: Path) -> TomlFajl:
    """TOML-fájl beolvasása; formai hibánál AdatHiba sorszámmal."""
    try:
        szoveg = utvonal.read_text(encoding="utf-8")
    except OSError as e:
        raise AdatHiba(utvonal, None, f"a fájl nem olvasható ({e.strerror})") from e
    try:
        adat = tomllib.loads(szoveg)
    except tomllib.TOMLDecodeError as e:
        m = re.search(r"line (\d+)", str(e))
        sor = int(m.group(1)) if m else None
        raise AdatHiba(utvonal, sor, f"hibás TOML-szintaxis: {e}") from e
    return TomlFajl(utvonal, szoveg, adat)


# --- JSON Schema: a sémákban használt részhalmaz ellenőrzése -------------------

TIPUSOK = {
    "string": str,
    "integer": int,
    "boolean": bool,
    "array": list,
    "object": dict,
}


def sema_ellenoriz(adat, sema: dict, ut: str = "") -> list[tuple[str, str]]:
    """Validál a JSON Schema egy részhalmaza szerint.

    Támogatott kulcsszavak: type, required, properties,
    additionalProperties (false), enum, pattern, minLength, items, minItems,
    uniqueItems. Visszaad: [(útvonal, magyar hibaüzenet)].
    """
    hibak: list[tuple[str, str]] = []
    tipus = sema.get("type")
    if tipus:
        elvart = TIPUSOK[tipus]
        if not isinstance(adat, elvart) or (tipus == "integer" and isinstance(adat, bool)):
            hibak.append((ut, f"a(z) „{ut or 'gyökér'}” típusa {tipus_nev(tipus)} legyen"))
            return hibak
    if "enum" in sema and adat not in sema["enum"]:
        lehet = ", ".join(str(e) for e in sema["enum"])
        hibak.append((ut, f"a(z) „{ut}” értéke nem megengedett: {adat!r}; lehetséges: {lehet}"))
    if isinstance(adat, str):
        if "minLength" in sema and len(adat.strip()) < sema["minLength"]:
            hibak.append((ut, f"a(z) „{ut}” nem lehet üres"))
        if "pattern" in sema and not re.search(sema["pattern"], adat):
            hibak.append((ut, f"a(z) „{ut}” formája hibás: {adat!r} (minta: {sema['pattern']})"))
    if isinstance(adat, list):
        if "minItems" in sema and len(adat) < sema["minItems"]:
            hibak.append((ut, f"a(z) „{ut}” legalább {sema['minItems']} elemet tartalmazzon"))
        if sema.get("uniqueItems") and len(adat) != len({json.dumps(a, sort_keys=True) for a in adat}):
            hibak.append((ut, f"a(z) „{ut}” elemei ismétlődnek"))
        if "items" in sema:
            for i, elem in enumerate(adat):
                hibak += sema_ellenoriz(elem, sema["items"], f"{ut}[{i}]")
    if isinstance(adat, dict):
        for k in sema.get("required", []):
            if k not in adat:
                hibak.append((ut, f"hiányzik a kötelező mező: „{(ut + '.' if ut else '') + k}”"))
        props = sema.get("properties", {})
        if sema.get("additionalProperties") is False:
            for k in adat:
                if k not in props:
                    hibak.append((f"{ut}.{k}" if ut else k,
                                  f"ismeretlen mező: „{(ut + '.' if ut else '') + k}”"))
        for k, alsema in props.items():
            if k in adat:
                hibak += sema_ellenoriz(adat[k], alsema, f"{ut}.{k}" if ut else k)
    return hibak


def tipus_nev(tipus: str) -> str:
    return {"string": "szöveg", "integer": "egész szám", "boolean": "logikai érték",
            "array": "lista", "object": "tábla"}.get(tipus, tipus)


def sema_betolt(nev: str, gyoker: Path = SKILL_GYOKER) -> dict:
    return json.loads((gyoker / "assets" / "schemas" / nev).read_text(encoding="utf-8"))


# --- Adatok betöltése -------------------------------------------------------------

@dataclass
class Adatok:
    gyoker: Path
    szabalyok: dict[str, TomlFajl] = field(default_factory=dict)
    forrasok: dict[str, TomlFajl] = field(default_factory=dict)
    katalogus: TomlFajl | None = None
    szotar: TomlFajl | None = None
    olvasasi_hibak: list[AdatHiba] = field(default_factory=list)

    def tetelek(self):
        """Minden leltártétel: (forrás-azonosító, index, tétel, TomlFajl)."""
        for fid in sorted(self.forrasok):
            f = self.forrasok[fid]
            for i, t in enumerate(f.adat.get("tetel", [])):
                yield fid, i, t, f


def adatok_betolt(gyoker: Path = SKILL_GYOKER) -> Adatok:
    a = Adatok(gyoker)
    adatdir = gyoker / "assets" / "adatok"
    try:
        a.katalogus = toml_olvas(adatdir / "katalogus.toml")
    except AdatHiba as e:
        a.olvasasi_hibak.append(e)
    if (adatdir / "szotar.toml").exists():
        try:
            a.szotar = toml_olvas(adatdir / "szotar.toml")
        except AdatHiba as e:
            a.olvasasi_hibak.append(e)
    for p in sorted((adatdir / "szabalyok").glob("*.toml")):
        try:
            a.szabalyok[p.stem] = toml_olvas(p)
        except AdatHiba as e:
            a.olvasasi_hibak.append(e)
    for p in sorted((adatdir / "forrasok").glob("*.toml")):
        try:
            a.forrasok[p.stem] = toml_olvas(p)
        except AdatHiba as e:
            a.olvasasi_hibak.append(e)
    return a


def oldal_jel(oldal: str) -> str:
    """Oldalszám hivatkozási alakja: „12. o.”, de „4. §” vagy „71–75. pont” változatlanul."""
    oldal = str(oldal).strip()
    return f"{oldal}. o." if re.fullmatch(r"[0-9][0-9–, ]*", oldal) else oldal


def lekepezes(tetel: dict) -> tuple[str, object]:
    """Egy leltártétel leképezésének fajtája és célja."""
    kinds = [(k, tetel[k]) for k in ("szabalyok", "referencia", "kihagyva") if k in tetel]
    if len(kinds) != 1:
        return ("hibas", [k for k, _ in kinds])
    return kinds[0]


def szabaly_sorrend(szabalyok: dict[str, TomlFajl]) -> list[str]:
    """Csoportsorrend, azon belül azonosító szerint."""
    csop = list(CSOPORTOK)

    def kulcs(sid: str):
        c = szabalyok[sid].adat.get("csoport", "")
        return (csop.index(c) if c in csop else len(csop), sid)

    return sorted(szabalyok, key=kulcs)


def kilep_hibaval(uzenet: str, kod: int = 1) -> None:
    print(f"Hiba: {uzenet}", file=sys.stderr)
    sys.exit(kod)


def frontmatter(szoveg: str) -> tuple[dict, str, int]:
    """A SKILL.md YAML-frontmatterének egyszerű olvasása.

    Csak a skill által használt alakot érti: kulcs: érték, egy szint
    behúzott metadata, és a „>-” vagy „|” blokkszöveg. Visszaad:
    (adatok, törzs, a törzs első sorának száma).
    """
    sorok = szoveg.splitlines()
    if not sorok or sorok[0].strip() != "---":
        raise ValueError("a SKILL.md nem YAML-frontmatterrel kezdődik (---)")
    try:
        zaro = next(i for i in range(1, len(sorok)) if sorok[i].strip() == "---")
    except StopIteration as e:
        raise ValueError("a frontmatter nincs lezárva (---)") from e
    adat: dict = {}
    i = 1
    while i < zaro:
        s = sorok[i]
        if not s.strip() or s.lstrip().startswith("#"):
            i += 1
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", s)
        if not m:
            raise ValueError(f"értelmezhetetlen frontmattersor ({i + 1}. sor): {s!r}")
        kulcs, ertek = m.group(1), m.group(2).strip()
        if ertek in (">", ">-", "|", "|-"):
            blokk = []
            i += 1
            while i < zaro and (sorok[i].startswith("  ") or not sorok[i].strip()):
                blokk.append(sorok[i].strip())
                i += 1
            adat[kulcs] = (" " if ertek.startswith(">") else "\n").join(
                b for b in blokk if b).strip()
            continue
        if ertek == "":
            al: dict = {}
            i += 1
            while i < zaro and sorok[i].startswith("  "):
                m2 = re.match(r"^\s+([A-Za-z0-9_-]+):\s*(.*)$", sorok[i])
                if m2:
                    al[m2.group(1)] = m2.group(2).strip().strip('"')
                i += 1
            adat[kulcs] = al
            continue
        adat[kulcs] = ertek.strip('"')
        i += 1
    torzs = "\n".join(sorok[zaro + 1:])
    return adat, torzs, zaro + 2
