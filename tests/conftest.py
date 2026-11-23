"""Közös tesztfixtúrák: a skill mappájának másolata, hogy a tesztek szabadon módosíthassák."""

import shutil
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / "skills" / "kozerthetoseg-hu"
EVALS = REPO / "evals"
sys.path.insert(0, str(SKILL / "scripts"))


@pytest.fixture
def skill(tmp_path: Path) -> Path:
    """A skill mappájának friss másolata, mellette a repó evaljaival (a CHANGELOG nélkül)."""
    cel = tmp_path / "kozerthetoseg-hu"
    shutil.copytree(SKILL, cel, ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copytree(REPO / "evals", tmp_path / "evals", ignore=shutil.ignore_patterns("eredmenyek"))
    return cel


def futtat(modul, argv, capsys):
    """Egy szkript main() függvényének futtatása; (kód, stdout, stderr)."""
    kod = modul.main(argv)
    ki = capsys.readouterr()
    return kod, ki.out, ki.err
