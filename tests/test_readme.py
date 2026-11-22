"""A docs/forrasok.md forrástáblázata minden forrást felsorol."""
import tomllib
from pathlib import Path

GYOKER = Path(__file__).resolve().parent.parent


def test_minden_forras_szerepel_a_readme_ben():
    readme = (GYOKER / "docs" / "forrasok.md").read_text(encoding="utf-8")
    hianyzik = []
    for f in sorted((GYOKER / "skills" / "kozerthetoseg-hu" / "assets" / "adatok" / "forrasok").glob("*.toml")):
        adat = tomllib.loads(f.read_text(encoding="utf-8"))
        jelek = [adat.get("url"), adat.get("doi")]
        if not any(j and j in readme for j in jelek):
            hianyzik.append(adat["azonosito"])
    assert not hianyzik, (
        "Ezek a források hiányoznak a docs/forrasok.md táblázatából "
        f"(az URL-jük vagy a DOI-juk nem szerepel benne): {', '.join(hianyzik)}"
    )
