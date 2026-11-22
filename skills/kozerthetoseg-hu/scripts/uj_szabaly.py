#!/usr/bin/env python3
"""Új szabályfájl létrehozása sablonból, a következő szabad azonosítóval.

Használat:
    python scripts/uj_szabaly.py --cim "A fő üzenet elöl" --csoport cel-es-tartalom
    python scripts/uj_szabaly.py --kovetkezo

Egyszer kiosztott azonosítót nem használunk újra: a következő azonosító
mindig a legnagyobb meglévő után jön, a visszavont szabályokat is beleszámítva.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import kozos  # noqa: E402


def kovetkezo_azonosito(gyoker: Path) -> str:
    mappa = gyoker / "assets" / "adatok" / "szabalyok"
    szamok = [int(p.stem[1:]) for p in mappa.glob("K*.toml") if kozos.SZABALY_MINTA.match(p.stem)]
    return f"K{(max(szamok) if szamok else 0) + 1:03d}"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="uj_szabaly.py",
                                description="Új szabályfájl létrehozása sablonból, a következő szabad azonosítóval.")
    p.add_argument("--cim", help="a szabály rövid címe")
    p.add_argument("--csoport", choices=list(kozos.CSOPORTOK), help="a szabály csoportja")
    p.add_argument("--kor", choices=["altalanos", "jogi"], default="altalanos",
                   help="alkalmazási kör (alapérték: altalanos)")
    p.add_argument("--kovetkezo", action="store_true", help="csak kiírja a következő szabad azonosítót")
    p.add_argument("--gyoker", type=Path, default=kozos.SKILL_GYOKER, help="a skill mappája")
    a = p.parse_args(argv)

    azon = kovetkezo_azonosito(a.gyoker)
    if a.kovetkezo:
        print(azon)
        return 0
    if not a.cim or not a.csoport:
        print("Hiba: a --cim és a --csoport kötelező (vagy használd a --kovetkezo kapcsolót).", file=sys.stderr)
        return 2
    if int(azon[1:]) > 999:
        print("Hiba: elfogyott a háromjegyű azonosítótartomány (K999).", file=sys.stderr)
        return 1
    sablon = (a.gyoker / "assets" / "sablonok" / "szabaly.toml").read_text(encoding="utf-8")
    tartalom = (sablon.replace("{{azonosito}}", azon).replace("{{cim}}", a.cim.replace('"', '\\"'))
                .replace("{{csoport}}", a.csoport).replace("{{kor}}", a.kor))
    cel = a.gyoker / "assets" / "adatok" / "szabalyok" / f"{azon}.toml"
    cel.write_text(tartalom, encoding="utf-8")
    print(f"Létrehozva: {cel.relative_to(a.gyoker)}")
    print("Következő lépés: töltsd ki a KITÖLTENDŐ mezőket, és a forrásleltár tételeinél "
          f"állítsd be: szabalyok = [\"{azon}\"]. Utána: python scripts/generalas.py && python scripts/ellenorzes.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
