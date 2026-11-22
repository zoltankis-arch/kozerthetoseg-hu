"""A repó Agent Plugins 1.0.0 szerinti plugin: manifest a gyökérben, skill a skills/ alatt."""
import json
import re
from pathlib import Path

GYOKER = Path(__file__).resolve().parent.parent
SEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
MEZOK = {"$schema", "name", "version", "description", "author", "homepage",
         "repository", "license", "keywords", "extensions"}
NEV = re.compile(r"^(?!.*(?:--|\.\.))[a-z0-9](?:[a-z0-9.-]*[a-z0-9])?$")


def manifest() -> dict:
    return json.loads((GYOKER / "plugin.json").read_text(encoding="utf-8"))


def skill_verzio() -> str:
    szoveg = (GYOKER / "skills" / "kozerthetoseg-hu" / "SKILL.md").read_text(encoding="utf-8")
    return re.search(r'^\s+version:\s*"([^"]+)"', szoveg, re.M).group(1)


def test_a_manifest_megfelel_a_szabvanynak():
    m = manifest()
    assert m["$schema"] == SEMA
    assert set(m) <= MEZOK, f"nem megengedett mező: {set(m) - MEZOK}"
    assert 1 <= len(m["name"]) <= 64 and NEV.match(m["name"])
    for k in ("version", "description", "homepage", "repository", "license"):
        assert isinstance(m.get(k, ""), str)
    assert set(m.get("author", {})) <= {"name", "email", "url"}
    assert all(isinstance(x, str) for x in m.get("author", {}).values())
    assert all(isinstance(x, str) for x in m.get("keywords", []))


def test_a_skill_a_rogzitett_helyen_van():
    skillek = [d for d in (GYOKER / "skills").iterdir() if (d / "SKILL.md").is_file()]
    assert [d.name for d in skillek] == ["kozerthetoseg-hu"]


def test_a_verziok_egyeznek():
    v = manifest()["version"]
    assert skill_verzio() == v
    for f in (".codex-plugin/plugin.json", ".claude-plugin/plugin.json"):
        assert json.loads((GYOKER / f).read_text(encoding="utf-8"))["version"] == v, f
    assert f'version: "{v}"' in (GYOKER / "CITATION.cff").read_text(encoding="utf-8")


def test_a_claude_piacter_a_repo_gyokeret_adja_meg():
    m = json.loads((GYOKER / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
    assert {"name", "owner", "plugins"} <= set(m)
    assert [(x["name"], x["source"]) for x in m["plugins"]] == [(manifest()["name"], "./")]
