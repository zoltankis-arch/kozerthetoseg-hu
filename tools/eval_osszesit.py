#!/usr/bin/env python3
"""Az összehasonlító evalok összesítése a commitolt nyers eredményekből.

Használat:
    python tools/eval_osszesit.py eredmenyek/iteracio-2            # összesít, és kiírja
    python tools/eval_osszesit.py --ellenoriz eredmenyek/iteracio-2 # a commitolt összesítéssel veti össze

Bemenet egy iteráció mappájában, evalonként (eval-NN/):
    with_skill/valasz.md, baseline/valasz.md      a futások válasza
    with_skill/atirt.md, baseline/atirt.md        az átírt szöveg, ha van
    with_skill/ertekeles.json, baseline/ertekeles.json
        {"elvarasok": [{"szoveg": "...", "teljesul": true, "indok": "..."}]}
    biralat.json
        {"A": "with_skill" | "baseline", "gyoztes": "A" | "B" | "dontetlen", "indok": "..."}
        A bíráló csak A-t és B-t látta; a megfeleltetést a futtató írta be utólag.

Kimenet: osszesites.json és osszesites.md ugyanabban a mappában.
Mérőszám az átírt szövegeken: a meres.py magas és közepes súlyosságú jelzéseinek száma
100 szóra. A skill ismeri ezt a mérőszámot, az alapváltozat nem; ezért ez a mutató
a skill javára torzíthat, és az összesítés ezt ki is írja.

Kilépési kód: 0 rendben; 1 az --ellenoriz eltérést talált; 2 hibás bemenet.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

GYOKER = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(GYOKER / "skills" / "kozerthetoseg-hu" / "scripts"))
import meres  # noqa: E402

KONFIGOK = ("with_skill", "baseline")
NEV = {"with_skill": "skill-lel", "baseline": "skill nélkül"}


def jelzes_100_szora(fajl: Path, szabalyok: dict, szotar: list) -> float | None:
    if not fajl.is_file():
        return None
    szoveg = fajl.read_text(encoding="utf-8")
    e, _ = meres.mer(szoveg, 20, 15)
    folyo = e.pop("_folyo")
    j = meres.jelzesek(folyo, e, szabalyok, szotar)
    db = sum(x["db"] for x in j if x["sulyossag"] in ("magas", "kozepes"))
    szavak = e["osszesites"]["szavak"]
    return round(100 * db / szavak, 1) if szavak else None


def osszesit(mappa: Path) -> dict:
    szabalyok, szotar = meres.katalogus_betolt(GYOKER / "skills" / "kozerthetoseg-hu")
    evalok = []
    for ed in sorted(mappa.glob("eval-*")):
        meta = json.loads((ed / "eval_metadata.json").read_text(encoding="utf-8"))
        sor = {"id": meta["id"], "nev": meta["eval_name"], "tipus": meta.get("tipus", "alap")}
        for k in KONFIGOK:
            ert = ed / k / "ertekeles.json"
            if not ert.is_file():
                sor[k] = None
                continue
            el = json.loads(ert.read_text(encoding="utf-8"))["elvarasok"]
            sor[k] = {
                "teljesult": sum(1 for x in el if x["teljesul"]),
                "osszes": len(el),
                "jelzes_100_szora": jelzes_100_szora(ed / k / "atirt.md", szabalyok, szotar),
            }
        b = ed / "biralat.json"
        if b.is_file():
            bd = json.loads(b.read_text(encoding="utf-8"))
            if bd["gyoztes"] == "dontetlen":
                sor["biralat"] = "dontetlen"
            else:
                a_konfig = bd["A"]
                b_konfig = "baseline" if a_konfig == "with_skill" else "with_skill"
                sor["biralat"] = a_konfig if bd["gyoztes"] == "A" else b_konfig
        else:
            sor["biralat"] = None
        evalok.append(sor)

    def osszeg(k):
        t = sum(e[k]["teljesult"] for e in evalok if e.get(k) and e.get("baseline") and e.get("with_skill"))
        o = sum(e[k]["osszes"] for e in evalok if e.get(k) and e.get("baseline") and e.get("with_skill"))
        return t, o

    pariban = [e for e in evalok if e.get("with_skill") and e.get("baseline")]
    jel = {k: [e[k]["jelzes_100_szora"] for e in pariban if e[k]["jelzes_100_szora"] is not None
               and e["baseline"]["jelzes_100_szora"] is not None and e["with_skill"]["jelzes_100_szora"] is not None]
           for k in KONFIGOK}
    ossz = {
        "evalok_szama": len(evalok),
        "parban_futott": len(pariban),
        "elvarasok": {k: dict(zip(("teljesult", "osszes"), osszeg(k))) for k in KONFIGOK},
        "jelzes_100_szora_atlag": {k: (round(sum(v) / len(v), 1) if v else None) for k, v in jel.items()},
        "atirasok_szama": len(jel["with_skill"]),
        "biralat": {
            "with_skill": sum(1 for e in evalok if e["biralat"] == "with_skill"),
            "baseline": sum(1 for e in evalok if e["biralat"] == "baseline"),
            "dontetlen": sum(1 for e in evalok if e["biralat"] == "dontetlen"),
        },
    }
    return {"osszesen": ossz, "evalok": evalok}


def tizedes(x) -> str:
    return "–" if x is None else f"{x}".replace(".", ",")


def markdown(o: dict) -> str:
    s = o["osszesen"]
    sz = lambda d: f"{d['teljesult']}/{d['osszes']} ({round(100 * d['teljesult'] / d['osszes'])}%)" if d["osszes"] else "–"
    ki = ["# Összehasonlító evalok", "",
          "Generált fájl (tools/eval_osszesit.py); kézzel ne szerkeszd.", "",
          f"{s['parban_futott']} eval futott mindkét változatban: a skill-lel és nélküle, ugyanazzal a modellel.", "",
          "| | Skill-lel | Skill nélkül |", "|---|---|---|",
          f"| Teljesült elvárások | {sz(s['elvarasok']['with_skill'])} | {sz(s['elvarasok']['baseline'])} |",
          f"| Vak bíráló szerint jobb | {s['biralat']['with_skill']} | {s['biralat']['baseline']} |",
          f"| Magas és közepes jelzés 100 szóra az átírásokban ({s['atirasok_szama']} átírás) | "
          f"{tizedes(s['jelzes_100_szora_atlag']['with_skill'])} | {tizedes(s['jelzes_100_szora_atlag']['baseline'])} |",
          "", f"Döntetlen a vak bírálatban: {s['biralat']['dontetlen']}.", "",
          "## Mit nem mutatnak ezek a számok?", "",
          "- Evalonként és változatonként egy futás van, ezért a különbség egy része véletlen lehet.",
          "- Az elvárások egy része a skill saját fogalmaira épül (szabályazonosító, mérőszkript, "
          "jogi zárómondat). Ezeket az alapváltozat nem ismerheti, így az elvárásszám a skill javára torzít.",
          "- A vak bíráló látta az elvárásokat, ezért az ítéletét ugyanez a torzítás érheti.",
          "- A jelzésszám is a skill javára torzíthat, mert a skill ismeri a mérőszkriptet. "
          "Ha mégis a skill átírásainál magasabb, azt érdemes szövegenként megnézni.",
          "- Ahol csak skill-lel futott az eval (például új forrás felvétele), ott nincs összevetés.", "",
          "## Evalonként", "",
          "| # | Eval | Típus | Skill-lel | Skill nélkül | Vak bíráló |", "|---|---|---|---|---|---|"]
    for e in o["evalok"]:
        f = lambda d: f"{d['teljesult']}/{d['osszes']}" if d else "–"
        b = {"with_skill": "skill-lel", "baseline": "skill nélkül", "dontetlen": "döntetlen", None: "–"}[e["biralat"]]
        ki.append(f"| {e['id']} | {e['nev']} | {e['tipus']} | {f(e.get('with_skill'))} | {f(e.get('baseline'))} | {b} |")
    return "\n".join(ki) + "\n"


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Az összehasonlító evalok összesítése a nyers eredményekből.")
    p.add_argument("mappa", type=Path, help="egy iteráció mappája, például eredmenyek/iteracio-2")
    p.add_argument("--ellenoriz", action="store_true", help="nem ír, csak összeveti a commitolt összesítéssel")
    a = p.parse_args(argv)
    if not a.mappa.is_dir():
        print(f"Hiba: nincs ilyen mappa: {a.mappa}", file=sys.stderr)
        return 2
    o = osszesit(a.mappa)
    j = json.dumps(o, ensure_ascii=False, indent=2) + "\n"
    m = markdown(o)
    if a.ellenoriz:
        hibak = [n for n, t in (("osszesites.json", j), ("osszesites.md", m))
                 if not (a.mappa / n).is_file() or (a.mappa / n).read_text(encoding="utf-8") != t]
        if hibak:
            print("Hiba: a közölt számok nem egyeznek a nyers eredményekből számoltakkal: " + ", ".join(hibak)
                  + ". Futtasd: python tools/eval_osszesit.py " + str(a.mappa), file=sys.stderr)
            return 1
        print("Rendben: az összesítés megegyezik a nyers eredményekkel.")
        return 0
    (a.mappa / "osszesites.json").write_text(j, encoding="utf-8")
    (a.mappa / "osszesites.md").write_text(m, encoding="utf-8")
    print(m, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
