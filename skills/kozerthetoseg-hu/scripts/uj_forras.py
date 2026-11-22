#!/usr/bin/env python3
"""Új forrásrekord és üres forrásleltár létrehozása sablonból.

Használat:
    python scripts/uj_forras.py kiado-cim-2026 --cim "A forrás címe" --kiado "Kiadó" --ev 2026
    python scripts/uj_forras.py --kovetkezo-tetel nav-ertheto-hivatal-2

A létrehozott fájl: assets/adatok/forrasok/<azonosító>.toml. Utána töltsd ki
a KITÖLTENDŐ mezőket a forrás-felvétel öt lépése szerint
(references/parancs-forras-felvetel.md).
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kozos  # noqa: E402


def kovetkezo_tetel(gyoker: Path, fid: str) -> str:
    ut = gyoker / "assets" / "adatok" / "forrasok" / f"{fid}.toml"
    if not ut.is_file():
        raise FileNotFoundError(f"nincs ilyen forrás: {fid}")
    szoveg = ut.read_text(encoding="utf-8")
    szamok = [int(x) for x in re.findall(re.escape(fid) + r"#(\d{3})", szoveg)]
    return f"{fid}#{(max(szamok) if szamok else 0) + 1:03d}"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="uj_forras.py",
                                description="Új forrásrekord és üres leltár létrehozása sablonból.")
    p.add_argument("azonosito", nargs="?", help="a forrás azonosítója: kisbetű, szám, kötőjel (pl. kiado-cim-2026)")
    p.add_argument("--cim", default="KITÖLTENDŐ", help="a forrás címe")
    p.add_argument("--kiado", default="KITÖLTENDŐ", help="kiadó vagy szerző intézmény")
    p.add_argument("--ev", default="KITÖLTENDŐ", help="megjelenési év (négy számjegy)")
    p.add_argument("--url", default="", help="nyilvános URL (ha van)")
    p.add_argument("--prioritas", choices=["A", "B", "C"], default="A",
                   help="A: szabály alapja; B: háttér; C: kitekintés")
    p.add_argument("--datum", default=None, help="a feldolgozás dátuma (ÉÉÉÉ-HH-NN; alapérték: ma)")
    p.add_argument("--kovetkezo-tetel", metavar="FORRAS",
                   help="nem hoz létre fájlt, csak kiírja a forrás következő szabad tételazonosítóját")
    p.add_argument("--gyoker", type=Path, default=kozos.SKILL_GYOKER, help="a skill mappája")
    a = p.parse_args(argv)

    if a.kovetkezo_tetel:
        try:
            print(kovetkezo_tetel(a.gyoker, a.kovetkezo_tetel))
        except FileNotFoundError as e:
            print(f"Hiba: {e}", file=sys.stderr)
            return 1
        return 0
    if not a.azonosito:
        print("Hiba: add meg az új forrás azonosítóját (vagy a --kovetkezo-tetel kapcsolót).", file=sys.stderr)
        return 2
    if not kozos.FORRAS_MINTA.match(a.azonosito):
        print(f"Hiba: az azonosító csak kisbetűt, számot és egyszeres kötőjelet tartalmazhat: {a.azonosito!r}",
              file=sys.stderr)
        return 2
    if a.ev != "KITÖLTENDŐ" and not re.fullmatch(r"\d{4}", a.ev):
        print(f"Hiba: az év négy számjegy legyen: {a.ev!r}", file=sys.stderr)
        return 2
    if a.url and not re.match(r"^https?://", a.url):
        print(f"Hiba: az URL http:// vagy https:// előtaggal kezdődjön: {a.url!r}", file=sys.stderr)
        return 2
    cel = a.gyoker / "assets" / "adatok" / "forrasok" / f"{a.azonosito}.toml"
    if cel.exists():
        print(f"Hiba: már létezik ilyen forrás: {cel}", file=sys.stderr)
        return 1
    sablon = (a.gyoker / "assets" / "sablonok" / "forras.toml").read_text(encoding="utf-8")
    datum = a.datum or dt.date.today().isoformat()
    tartalom = (sablon.replace("{{azonosito}}", a.azonosito).replace("{{cim}}", a.cim.replace('"', '\\"'))
                .replace("{{kiado}}", a.kiado.replace('"', '\\"')).replace("{{ev}}", a.ev)
                .replace("{{datum}}", datum).replace("{{prioritas}}", a.prioritas))
    if a.url:
        tartalom = tartalom.replace("{{url}}", a.url)
    else:
        tartalom = re.sub(r'^url = "\{\{url\}\}"\n', "", tartalom, flags=re.MULTILINE)
    cel.write_text(tartalom, encoding="utf-8")
    print(f"Létrehozva: {cel.relative_to(a.gyoker)}")
    print("Következő lépés: töltsd ki a KITÖLTENDŐ mezőket, majd futtasd: "
          "python scripts/generalas.py && python scripts/ellenorzes.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
