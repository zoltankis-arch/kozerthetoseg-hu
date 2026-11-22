#!/usr/bin/env python3
"""Felszíni közérthetőségi mérőszámok magyar szövegre.

A mérőszám jelzés, nem ítélet: azt mutatja meg, hol érdemes ránézni a
szövegre. A szkript csak a standard könyvtárat használja, hálózat nélkül
fut, és ugyanarra a bemenetre mindig ugyanazt adja.

Használat:
    python scripts/meres.py szoveg.md
    python scripts/meres.py --json szoveg.txt
    cat szoveg.txt | python scripts/meres.py -
    python scripts/meres.py --huspacy szoveg.md   # ha a HuSpaCy telepítve van
    python scripts/meres.py --max-jelzes 0 --szint magas szoveg.md   # CI-ben

A beépített mutatók mellett a szabálykatalógus (assets/adatok/szabalyok/)
keresőmintáit és a szótár (assets/adatok/szotar.toml) párjait is lefuttatja,
és minden jelzést a szabály azonosítójához köt.

Kilépési kód: 0 rendben; 1 ha --max-jelzes meg van adva, és a --szint vagy
annál súlyosabb jelzések száma meghaladja; 2 hibás bemenet; 3 HuSpaCy-hiba.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # Python 3.10 alatt nincs; a szkripthez 3.11 kell
    tomllib = None

SKILL_GYOKER = Path(__file__).resolve().parent.parent
SULY_SORREND = {"magas": 0, "kozepes": 1, "alacsony": 2}
SULY_NEV = {"magas": "magas", "kozepes": "közepes", "alacsony": "alacsony"}
ELL_NEV = {"gepi": "gépi", "vegyes": "jelölt", "itelet": "olvasva"}

FIGYELMEZTETES = (
    "A mérőszám jelzés, nem ítélet. Felszíni jegyekből nem lehet megbízhatóan "
    "eldönteni, hogy egy mondat közérthető-e: Üveges (2026) magyar hivatali "
    "korpuszán a felszíni és szintaktikai jegyekből épített modell F1 = 0,58-at ért el. "
    "A számok azt mutatják meg, hol érdemes ránézni a szövegre."
)

NEM_MERI = [
    "Azt, hogy egy szó a szövegen belül két jelentésben szerepel-e.",
    "Azt, hogy az olvasó ismeri-e a szakszavakat.",
    "Azt, hogy a fő üzenet elöl áll-e, és kiderül-e, mit kell tennie az olvasónak.",
]

# A meres mezőben ezekre a kulcsokra lehet hivatkozni a szabályokból.
METRIKAK = {
    "mondathossz": "Mondathossz: átlag, maximum és a küszöb feletti mondatok.",
    "fonevesites": "Főnevesítési jelöltek (-ás/-és képzős főnevek).",
    "kerul_szerkezet": "„-ásra/-ésre kerül” szerkezetek.",
    "altal_torteno_valo": "„által”, „történő”, „való” előfordulásai.",
    "illetve_illetoleg": "„illetve” és „illetőleg” előfordulásai.",
    "zarojelmelyseg": "Zárójelek legnagyobb mélysége és az egymásba ágyazott zárójelek.",
    "hosszu_szavak": "15 betűnél hosszabb szavak.",
    "hivatali_fordulatok": "Gyakori hivatali fordulatok listája alapján talált jelöltek.",
    "tagadas": "Tagadószó és tagadó jelentésű szó együtt (kettős tagadás jelöltjei).",
    "huspacy": "Függőségi mélység és beágyazott tagmondatok (csak HuSpaCy-val).",
}

SZO = re.compile(r"§|[^\W_]+(?:[-'’][^\W_]+)*")
BETU = re.compile(r"[^\W\d_]")

# Pont utáni rövidítések, amelyek után nem kezdődik új mondat.
NEM_MONDATVEG = {
    "pl", "ill", "kb", "vö", "ún", "dr", "ld", "lásd", "ifj", "id", "özv", "u", "sz",
    "bek", "ápr", "aug", "febr", "jan", "jún", "júl", "márc", "nov", "okt", "szept", "dec",
    "kft", "zrt", "nyrt", "bt",
}

FONEV_VEG = re.compile(
    r"^[a-záéíóöőúüű]{3,}(?:ás|és)"
    r"(?:a|e|á|é|ai|ei|ái|éi|uk|ük|unk|ünk|aik|eik|ok|ek)?"
    r"(?:t|ra|re|ról|ről|ba|be|ban|ben|ból|ből|val|vel|nak|nek|hoz|hez|höz|tól|től"
    r"|on|en|ön|ért|ig|ként|kor|nál|nél)?$"
)
FONEV_KIVETEL = {"kevés", "hálás", "kevésbé", "mesés", "kedvezményes"}
# Lexikalizálódott főnevek: a szó -ás/-és-re végződik, de nem igéből képzett jelölt.
FONEV_LEXIKALIZALT = ("kérdés", "bekezdés", "szerződés")

KERUL = re.compile(
    r"\b([^\W\d_]+(?:ásra|ésre|ására|ésére))\s+(?:[^\W\d_]+\s+)?(kerül[^\W\d_]*|került[^\W\d_]*)\b"
    r"|\b(kerül[^\W\d_]*|került[^\W\d_]*)\s+(?:[^\W\d_]+\s+)?([^\W\d_]+(?:ásra|ésre|ására|ésére))\b",
    re.IGNORECASE,
)

HIVATALI = [
    ("amennyiben", r"\bamennyiben\b"),
    ("tekintettel arra", r"\btekintettel arra\b"),
    ("fentiekre tekintettel", r"\b(?:fentiekre|a fentiekre) tekintettel\b"),
    ("jelen (levél, határozat…)", r"\bjelen (?:levél|levelünk|levelem|határozat|tájékoztató|szerződés)\w*"),
    ("fent nevezett / nevezett", r"\b(?:fent ?nevezett|fentnevezett|fent hivatkozott)\b"),
    ("eszközöl", r"\beszközöl\w*"),
    ("foganatosít", r"\bfoganatosít\w*"),
    ("sor kerül", r"\b(?:sor kerül|sorra kerül|kerül sor|került sor)\w*"),
    ("megállapítást nyer", r"\bmegállapítást nyer\w*"),
    ("jelentőséggel bír", r"\bjelentőséggel bír\w*"),
    ("figyelembevételével", r"\bfigyelembevétel\w*"),
    ("vonatkozásában", r"\bvonatkozásában\b"),
    ("tekintetében", r"\btekintetében\b"),
    ("tájékoztatjuk/tájékoztatom, hogy", r"\btájékoztat(?:juk|om)(?: arról)?,? hogy\b"),
    ("kérjük … tudomásulvételét", r"\btudomásulvétel\w*"),
]
HIVATALI_RE = [(nev, re.compile(m, re.IGNORECASE)) for nev, m in HIVATALI]

TAGADAS = re.compile(
    r"\bnem\s+(?:[^\W\d_]+\s+){0,2}?"
    r"(mellőz[^\W\d_]*|nélkül[^\W\d_]*|nélküli|hiány[^\W\d_]*|tilos|tilt[^\W\d_]*|kizár[^\W\d_]*|elmarad[^\W\d_]*|kivéve)",
    re.IGNORECASE,
)


# --- Előfeldolgozás ------------------------------------------------------------------

def elofeldolgoz(szoveg: str) -> list[tuple[str, str]]:
    """Markdownból vagy sima szövegből egységek: [(fajta, szöveg)].

    Fajták: 'bekezdes', 'listaelem', 'cim', 'tablazat'. A YAML-frontmattert,
    a HTML-megjegyzést, a kódblokkot és a sorközi kódot kihagyja.
    """
    szoveg = szoveg.replace("\r\n", "\n").replace("\r", "\n")
    szoveg = re.sub(r"\A---\n.*?\n---\n", "", szoveg, flags=re.DOTALL)
    szoveg = re.sub(r"<!--.*?-->", " ", szoveg, flags=re.DOTALL)
    szoveg = re.sub(r"^(```|~~~).*?^\1[^\n]*$", "", szoveg, flags=re.DOTALL | re.MULTILINE)
    szoveg = re.sub(r"`[^`\n]*`", " ", szoveg)
    szoveg = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", szoveg)
    szoveg = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", szoveg)
    szoveg = re.sub(r"https?://\S+|www\.\S+|\b[\w.+-]+@[\w-]+\.[\w.]+", "URL", szoveg)
    szoveg = re.sub(r"<[^>\n]+>", " ", szoveg)

    egysegek: list[tuple[str, str]] = []
    puffer: list[str] = []

    def lezar():
        if puffer:
            egysegek.append(("bekezdes", " ".join(puffer)))
            puffer.clear()

    for sor in szoveg.split("\n"):
        s = sor.strip()
        s = re.sub(r"^>\s?", "", s)
        if not s:
            lezar()
            continue
        if re.match(r"^#{1,6}\s", s):
            lezar()
            egysegek.append(("cim", re.sub(r"^#{1,6}\s+", "", s).strip("# ")))
            continue
        if s.startswith("|"):
            lezar()
            if not re.fullmatch(r"\|?[\s:|-]+\|?", s):
                egysegek.append(("tablazat", s.strip("|").replace("|", " ")))
            continue
        if re.fullmatch(r"[-*_]{3,}", s):
            lezar()
            continue
        m = re.match(r"^([-*+•]|\d{1,3}[.)]|[a-z][.)])\s+(.*)$", s)
        if m:
            lezar()
            egysegek.append(("listaelem", m.group(2)))
            continue
        if egysegek and egysegek[-1][0] == "listaelem" and not puffer and sor.startswith(("  ", "\t")):
            fajta, regi = egysegek[-1]
            egysegek[-1] = (fajta, regi + " " + s)
            continue
        puffer.append(s)
    lezar()
    tiszta = []
    for fajta, t in egysegek:
        t = re.sub(r"(\*\*|__|\*|_)(?=\S)(.+?)(?<=\S)\1", r"\2", t)
        t = re.sub(r"\s+", " ", t).strip()
        if t:
            tiszta.append((fajta, t))
    return tiszta


def szavak(szoveg: str) -> list[str]:
    return SZO.findall(szoveg)


def mondatokra_bont(szoveg: str) -> list[str]:
    """Egy bekezdés mondatokra bontása egyszerű magyar szabályokkal."""
    mondatok: list[str] = []
    kezdet = 0
    for m in re.finditer(r"[.!?…]+[”\"'’»)\]]*(?=\s+|$)", szoveg):
        veg = m.end()
        utana = szoveg[veg:].lstrip()
        elotte = szoveg[kezdet:m.start()]
        utolso = re.findall(r"[^\s(„\"]+$", elotte)
        utolso_szo = utolso[0] if utolso else ""
        jel = m.group(0)[0]
        if not utana:
            hatar = True
        elif jel == ".":
            kov = utana[0]
            kicsi = utolso_szo.lower().rstrip(".")
            if kicsi in NEM_MONDATVEG:
                hatar = False
            elif re.fullmatch(r"\d+", utolso_szo) or re.fullmatch(r"[IVXLC]+", utolso_szo):
                hatar = kov.isupper() and BETU.match(kov) is not None
            elif re.fullmatch(r"[A-ZÁÉÍÓÖŐÚÜŰ]", utolso_szo):
                hatar = False
            else:
                hatar = kov.isupper() or kov.isdigit() or kov in "„\"(–-"
        else:
            kov = utana[0]
            hatar = not kov.islower()
        if hatar:
            mondat = szoveg[kezdet:veg].strip()
            if mondat:
                mondatok.append(mondat)
            kezdet = veg
    maradek = szoveg[kezdet:].strip()
    if maradek:
        mondatok.append(maradek)
    return mondatok


# --- Mérés -------------------------------------------------------------------------------

def zarojel_melyseg(szoveg: str) -> tuple[int, int]:
    """(legnagyobb mélység, egymásba ágyazott zárójelpárok száma)."""
    melyseg = legnagyobb = beagyazott = 0
    for ch in szoveg:
        if ch in "([":
            melyseg += 1
            legnagyobb = max(legnagyobb, melyseg)
            if melyseg >= 2:
                beagyazott += 1
        elif ch in ")]" and melyseg > 0:
            melyseg -= 1
    return legnagyobb, beagyazott


def rovid(szoveg: str, hossz: int = 90) -> str:
    return szoveg if len(szoveg) <= hossz else szoveg[: hossz - 1].rstrip() + "…"


def mer(szoveg: str, kuszob: int = 20, szohossz: int = 15) -> dict:
    egysegek = elofeldolgoz(szoveg)
    mondatok: list[str] = []
    for fajta, t in egysegek:
        if fajta in ("bekezdes", "listaelem"):
            mondatok.extend(mondatokra_bont(t))
    folyo = " ".join(t for f, t in egysegek if f in ("bekezdes", "listaelem"))
    minden = " ".join(t for _, t in egysegek)
    osszes_szo = szavak(minden)

    hosszak = [len(szavak(m)) for m in mondatok]
    hosszu = [
        {"sorszam": i + 1, "szavak": n, "kezdete": rovid(m)}
        for i, (m, n) in enumerate(zip(mondatok, hosszak)) if n > kuszob
    ]
    mondathossz = {
        "mondatok": len(mondatok),
        "atlag": round(statistics.fmean(hosszak), 1) if hosszak else 0.0,
        "median": float(statistics.median(hosszak)) if hosszak else 0.0,
        "maximum": max(hosszak) if hosszak else 0,
        "kuszob": kuszob,
        "kuszob_feletti": len(hosszu),
        "kuszob_feletti_mondatok": hosszu,
    }

    kisbetus = [w.lower() for w in szavak(folyo)]
    fonev = Counter(w for w in kisbetus if FONEV_VEG.match(w) and w not in FONEV_KIVETEL
                   and not w.startswith(FONEV_LEXIKALIZALT))
    fonevesites = {
        "jeloltek": sum(fonev.values()),
        "szaz_szavankent": round(100 * sum(fonev.values()) / len(kisbetus), 1) if kisbetus else 0.0,
        "leggyakoribbak": [{"szo": w, "db": n} for w, n in sorted(fonev.items(), key=lambda x: (-x[1], x[0]))[:15]],
    }

    kerul = []
    for m in KERUL.finditer(folyo):
        kerul.append(rovid(m.group(0), 60))
    kerul_szerkezet = {"db": len(kerul), "elofordulasok": kerul}

    atv = {}
    for szo in ("által", "történő", "való"):
        talalat = [m for m in re.finditer(r"([^\W\d_]+)\s+" + szo + r"\b", folyo, re.IGNORECASE)]
        egyedul = len(re.findall(r"\b" + szo + r"\b", folyo, re.IGNORECASE))
        atv[szo] = {
            "db": egyedul,
            "elotte": sorted({m.group(1).lower() for m in talalat})[:15],
        }

    ill = {
        "illetve": len(re.findall(r"\billetve\b", folyo, re.IGNORECASE)),
        "illetőleg": len(re.findall(r"\billetőleg\b", folyo, re.IGNORECASE)),
    }

    legmelyebb, beagyazott = zarojel_melyseg(folyo)
    zarojel = {"legnagyobb_melyseg": legmelyebb, "egymasba_agyazott": beagyazott}

    hosszu_szo = sorted({w for w in osszes_szo if len(BETU.findall(w)) > szohossz},
                        key=lambda w: (-len(w), w.lower()))
    hosszu_szavak = {"hatar": szohossz, "db": len(hosszu_szo), "szavak": hosszu_szo[:20]}

    hivatali = []
    for nev, minta in HIVATALI_RE:
        n = len(minta.findall(folyo))
        if n:
            hivatali.append({"fordulat": nev, "db": n})

    tagadas = [rovid(m.group(0), 60) for m in TAGADAS.finditer(folyo)]

    return {
        "figyelmeztetes": FIGYELMEZTETES,
        "nem_meri": NEM_MERI,
        "osszesites": {
            "szavak": len(osszes_szo),
            "mondatok": len(mondatok),
            "cimsorok": sum(1 for f, _ in egysegek if f == "cim"),
            "listaelemek": sum(1 for f, _ in egysegek if f == "listaelem"),
            "tablazatsorok": sum(1 for f, _ in egysegek if f == "tablazat"),
        },
        "mondathossz": mondathossz,
        "fonevesites": fonevesites,
        "kerul_szerkezet": kerul_szerkezet,
        "altal_torteno_valo": atv,
        "illetve_illetoleg": ill,
        "zarojelmelyseg": zarojel,
        "hosszu_szavak": hosszu_szavak,
        "hivatali_fordulatok": hivatali,
        "tagadas": {"db": len(tagadas), "elofordulasok": tagadas},
        "_folyo": folyo,
    }, mondatok


def metrika_db(e: dict, kulcs: str) -> int:
    """Egy beépített mutató jelzéseinek száma (0 = nincs mit jelezni)."""
    if kulcs == "mondathossz":
        return e["mondathossz"]["kuszob_feletti"]
    if kulcs == "fonevesites":
        return e["fonevesites"]["jeloltek"]
    if kulcs == "kerul_szerkezet":
        return e["kerul_szerkezet"]["db"]
    if kulcs == "altal_torteno_valo":
        return sum(v["db"] for v in e["altal_torteno_valo"].values())
    if kulcs == "illetve_illetoleg":
        return sum(e["illetve_illetoleg"].values())
    if kulcs == "zarojelmelyseg":
        return e["zarojelmelyseg"]["egymasba_agyazott"]
    if kulcs == "hosszu_szavak":
        return e["hosszu_szavak"]["db"]
    if kulcs == "hivatali_fordulatok":
        return sum(h["db"] for h in e["hivatali_fordulatok"])
    if kulcs == "tagadas":
        return e["tagadas"]["db"]
    return 0


def katalogus_betolt(gyoker: Path) -> tuple[dict, list]:
    """A szabályok és a szótárpárok a skill adataiból; ha nincsenek meg, üresen."""
    szabalyok, szotar = {}, []
    adat = gyoker / "assets" / "adatok"
    if tomllib is None or not (adat / "szabalyok").is_dir():
        return szabalyok, szotar
    for p in sorted((adat / "szabalyok").glob("K*.toml")):
        d = tomllib.loads(p.read_text(encoding="utf-8"))
        if d.get("allapot") == "aktiv":
            szabalyok[d["azonosito"]] = d
    if (adat / "szotar.toml").is_file():
        szotar = tomllib.loads((adat / "szotar.toml").read_text(encoding="utf-8")).get("par", [])
    return szabalyok, szotar


def kornyezet(szoveg: str, m: re.Match, szel: int = 30) -> str:
    eleje = max(0, m.start() - szel)
    vege = min(len(szoveg), m.end() + szel)
    return ("…" if eleje else "") + szoveg[eleje:vege].strip() + ("…" if vege < len(szoveg) else "")


def jelzesek(folyo: str, e: dict, szabalyok: dict, szotar: list) -> list[dict]:
    """Minden jelzés egy szabályhoz kötve: beépített mutató, katalógusminta vagy szótárpár."""
    ki = []

    def uj(sid, honnan, mi, db, pelda="", javaslat="", mikor_nem=""):
        d = szabalyok.get(sid, {})
        ki.append({
            "szabaly": sid,
            "cim": d.get("cim", ""),
            "sulyossag": d.get("sulyossag", "kozepes"),
            "ellenorzes": d.get("ellenorzes", "vegyes"),
            "kor": d.get("alkalmazasi_kor", "altalanos"),
            "honnan": honnan,
            "mi": mi,
            "db": db,
            "pelda": pelda,
            "javaslat": javaslat,
            "mikor_nem": mikor_nem,
        })

    for sid, d in szabalyok.items():
        for kulcs in d.get("meres", []):
            db = metrika_db(e, kulcs)
            if db:
                uj(sid, "mutató", METRIKAK.get(kulcs, kulcs), db)
        for mt in d.get("minta", []):
            talalat = list(re.finditer(mt["regex"], folyo, re.IGNORECASE))
            if talalat:
                uj(sid, "minta", mt["leiras"], len(talalat), kornyezet(folyo, talalat[0]))
    for p in szotar:
        talalat = list(re.finditer(p["regex"], folyo, re.IGNORECASE))
        if talalat and p.get("szabaly") in szabalyok:
            uj(p["szabaly"], "szótár", f"„{p['kifejezes']}”", len(talalat), kornyezet(folyo, talalat[0]),
               p.get("javaslat", ""), p.get("mikor_nem", ""))
    ki.sort(key=lambda j: (SULY_SORREND.get(j["sulyossag"], 1), j["szabaly"], j["honnan"], j["mi"]))
    return ki


def huspacy_meres(mondatok: list[str], modell: str) -> dict:
    """Függőségi mélység és beágyazott tagmondatok HuSpaCy-val."""
    try:
        import spacy  # type: ignore
    except ImportError as e:
        raise RuntimeError(
            "A --huspacy kapcsolóhoz telepíteni kell a HuSpaCy-t és egy magyar modellt "
            "(pip install huspacy, majd a modell letöltése). Kapcsoló nélkül a mérés "
            "külső csomag nélkül fut."
        ) from e
    try:
        nlp = spacy.load(modell)
    except Exception as e:  # noqa: BLE001 - a spacy többféle kivételt dob
        raise RuntimeError(f"A(z) „{modell}” HuSpaCy-modell nem tölthető be: {e}") from e
    beagyazo = {"acl", "advcl", "ccomp", "csubj", "xcomp"}
    melysegek, tagmondatok = [], []
    for m in mondatok:
        doc = nlp(m)
        legmelyebb = 0
        for tok in doc:
            d, t = 0, tok
            while t.head is not t and d < 200:
                t = t.head
                d += 1
            legmelyebb = max(legmelyebb, d)
        melysegek.append(legmelyebb)
        tagmondatok.append(sum(1 for tok in doc if tok.dep_ in beagyazo))
    return {
        "modell": modell,
        "fuggosegi_melyseg_atlag": round(statistics.fmean(melysegek), 1) if melysegek else 0.0,
        "fuggosegi_melyseg_max": max(melysegek) if melysegek else 0,
        "beagyazott_tagmondatok": sum(tagmondatok),
        "beagyazott_tagmondatos_mondatok": sum(1 for n in tagmondatok if n),
    }


# --- Kimenet ---------------------------------------------------------------------------

def szam(x) -> str:
    """Szám magyar tizedesvesszővel a Markdown-kimenethez."""
    return str(x).replace(".", ",")


def markdown(e: dict) -> str:
    s = []
    s.append("# Mérés")
    s.append("")
    s.append(f"> {e['figyelmeztetes']}")
    s.append("")
    o, mh = e["osszesites"], e["mondathossz"]
    s.append(f"Szavak: {o['szavak']}. Mondatok: {o['mondatok']}. Címsorok: {o['cimsorok']}. "
             f"Listaelemek: {o['listaelemek']}. Táblázatsorok: {o['tablazatsorok']}.")
    s.append("")
    s.append("| Mutató | Érték |")
    s.append("|---|---|")
    s.append(f"| Átlagos mondathossz | {szam(mh['atlag'])} szó (medián {szam(mh['median'])}) |")
    s.append(f"| Leghosszabb mondat | {mh['maximum']} szó |")
    s.append(f"| {mh['kuszob']} szó feletti mondatok | {mh['kuszob_feletti']} |")
    fv = e["fonevesites"]
    s.append(f"| Főnevesítési jelöltek | {fv['jeloltek']} ({szam(fv['szaz_szavankent'])} / 100 szó) |")
    s.append(f"| „-ásra/-ésre kerül” | {e['kerul_szerkezet']['db']} |")
    atv = e["altal_torteno_valo"]
    s.append(f"| által / történő / való | {atv['által']['db']} / {atv['történő']['db']} / {atv['való']['db']} |")
    ii = e["illetve_illetoleg"]
    s.append(f"| illetve / illetőleg | {ii['illetve']} / {ii['illetőleg']} |")
    z = e["zarojelmelyseg"]
    s.append(f"| Zárójelmélység | {z['legnagyobb_melyseg']} (egymásba ágyazva: {z['egymasba_agyazott']}) |")
    hs = e["hosszu_szavak"]
    s.append(f"| {hs['hatar']} betűnél hosszabb szavak | {hs['db']} |")
    s.append(f"| Hivatali fordulatok | {sum(h['db'] for h in e['hivatali_fordulatok'])} |")
    s.append(f"| Kettős tagadás jelöltjei | {e['tagadas']['db']} |")
    if "huspacy" in e:
        h = e["huspacy"]
        s.append(f"| Függőségi mélység (HuSpaCy) | átlag {szam(h['fuggosegi_melyseg_atlag'])}, max {h['fuggosegi_melyseg_max']} |")
        s.append(f"| Beágyazott tagmondatok (HuSpaCy) | {h['beagyazott_tagmondatok']} |")
    s.append("")
    if mh["kuszob_feletti_mondatok"]:
        s.append(f"## {mh['kuszob']} szó feletti mondatok")
        s.append("")
        for m in mh["kuszob_feletti_mondatok"]:
            s.append(f"- {m['sorszam']}. mondat, {m['szavak']} szó: {m['kezdete']}")
        s.append("")
    reszletek = []
    if fv["leggyakoribbak"]:
        reszletek.append("Főnevesítési jelöltek: " + ", ".join(f"{x['szo']} ({x['db']})" for x in fv["leggyakoribbak"]))
    if e["kerul_szerkezet"]["elofordulasok"]:
        reszletek.append("„kerül”-szerkezetek: " + "; ".join(e["kerul_szerkezet"]["elofordulasok"]))
    if hs["szavak"]:
        reszletek.append("Hosszú szavak: " + ", ".join(hs["szavak"]))
    if e["hivatali_fordulatok"]:
        reszletek.append("Hivatali fordulatok: " + ", ".join(f"{h['fordulat']} ({h['db']})" for h in e["hivatali_fordulatok"]))
    if e["tagadas"]["elofordulasok"]:
        reszletek.append("Kettős tagadás jelöltjei: " + "; ".join(e["tagadas"]["elofordulasok"]))
    if reszletek:
        s.append("## Részletek")
        s.append("")
        s.extend(f"- {r}" for r in reszletek)
        s.append("")
    if e.get("jelzesek"):
        s.append("## Szabályonkénti jelzések")
        s.append("")
        s.append("Súlyosság: a szabály alapértelmezett prioritása. Ellenőrzés: „gépi” = a szkript "
                 "megbízhatóan jelzi; „jelölt” = olvasva kell eldönteni, valóban hiba-e.")
        s.append("")
        s.append("| Szabály | Súlyosság | Ellenőrzés | Mit talált | Db | Példa | Javaslat |")
        s.append("|---|---|---|---|---|---|---|")
        for j in e["jelzesek"]:
            jog = " (jogi)" if j["kor"] == "jogi" else ""
            jav = j["javaslat"] + (f" Kivétel: {j['mikor_nem']}" if j["mikor_nem"] else "")
            cella = lambda x: x.replace("|", "\\|").replace("\n", " ")
            s.append(f"| {j['szabaly']}{jog} | {SULY_NEV.get(j['sulyossag'], j['sulyossag'])} | "
                     f"{ELL_NEV.get(j['ellenorzes'], j['ellenorzes'])} | {cella(j['mi'])} | {j['db']} | "
                     f"{cella(j['pelda'])} | {cella(jav)} |")
        s.append("")
    s.append("## Amit a mérés nem mutat meg")
    s.append("")
    s.extend(f"- {n}" for n in e["nem_meri"])
    return "\n".join(s) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        prog="meres.py",
        description="Felszíni közérthetőségi mérőszámok magyar szövegre. A mérőszám jelzés, nem ítélet.",
    )
    p.add_argument("fajl", help="a mérendő Markdown- vagy szövegfájl; „-” esetén a szabványos bemenet")
    p.add_argument("--json", action="store_true", help="JSON-kimenet a Markdown helyett")
    p.add_argument("--kuszob", type=int, default=20, help="mondathossz-küszöb szóban (alapérték: 20)")
    p.add_argument("--szohossz", type=int, default=15, help="hosszú szó határa betűben (alapérték: 15)")
    p.add_argument("--huspacy", action="store_true", help="függőségi mélység és beágyazott tagmondatok HuSpaCy-val")
    p.add_argument("--huspacy-modell", default="hu_core_news_lg", help="a betöltendő HuSpaCy-modell neve")
    p.add_argument("--max-jelzes", type=int, default=None,
                   help="ha a --szint vagy súlyosabb jelzések száma ennél több, a kilépési kód 1 (CI-hez)")
    p.add_argument("--szint", choices=["magas", "kozepes", "alacsony"], default="alacsony",
                   help="a --max-jelzes ennél súlyosabb vagy ilyen jelzéseket számol (alapérték: alacsony)")
    p.add_argument("--gyoker", type=Path, default=SKILL_GYOKER,
                   help="a skill mappája, ahol a szabályok és a szótár vannak (alapérték: a szkript fölötti mappa)")
    a = p.parse_args(argv)

    if a.kuszob < 1 or a.szohossz < 1:
        print("Hiba: a --kuszob és a --szohossz pozitív egész szám legyen.", file=sys.stderr)
        return 2
    if a.fajl == "-":
        szoveg = sys.stdin.read()
    else:
        ut = Path(a.fajl)
        if not ut.is_file():
            print(f"Hiba: nem található a fájl: {a.fajl}", file=sys.stderr)
            return 2
        try:
            szoveg = ut.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            print(f"Hiba: a(z) {a.fajl} nem UTF-8 kódolású szövegfájl.", file=sys.stderr)
            return 2
    if not szoveg.strip():
        print("Hiba: a bemenet üres.", file=sys.stderr)
        return 2

    eredmeny, mondatok = mer(szoveg, a.kuszob, a.szohossz)
    folyo = eredmeny.pop("_folyo")
    szabalyok, szotar = katalogus_betolt(a.gyoker)
    eredmeny["jelzesek"] = jelzesek(folyo, eredmeny, szabalyok, szotar)
    if a.huspacy:
        try:
            eredmeny["huspacy"] = huspacy_meres(mondatok, a.huspacy_modell)
        except RuntimeError as e:
            print(f"Hiba: {e}", file=sys.stderr)
            return 3
    if a.json:
        print(json.dumps(eredmeny, ensure_ascii=False, indent=2))
    else:
        print(markdown(eredmeny), end="")
    if a.max_jelzes is not None:
        hatar = SULY_SORREND[a.szint]
        db = sum(1 for j in eredmeny["jelzesek"] if SULY_SORREND.get(j["sulyossag"], 1) <= hatar)
        if db > a.max_jelzes:
            print(f"A(z) {a.szint} vagy súlyosabb jelzések száma ({db}) meghaladja a megengedettet ({a.max_jelzes}).",
                  file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
