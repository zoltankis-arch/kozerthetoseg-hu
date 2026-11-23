import json
import re

import pytest

import ellenorzes
import generalas
from conftest import futtat


def csere(ut, regi, uj, db=1):
    szoveg = ut.read_text(encoding="utf-8")
    assert szoveg.count(regi) >= 1, f"nem található: {regi!r}"
    ut.write_text(szoveg.replace(regi, uj, db), encoding="utf-8")


def ellenoriz(skill, capsys):
    return futtat(ellenorzes, ["--gyoker", str(skill)], capsys)


def ujragenerál(skill, capsys):
    futtat(generalas, ["--gyoker", str(skill)], capsys)


def test_tiszta_masolat_zold(skill, capsys):
    kod, ki, hiba = ellenoriz(skill, capsys)
    assert kod == 0, hiba
    assert ki.startswith("Rendben:")


def test_nem_skill_mappa(tmp_path, capsys):
    kod, _, hiba = futtat(ellenorzes, ["--gyoker", str(tmp_path)], capsys)
    assert kod == 2 and "nem a skill mappája" in hiba


@pytest.fixture
def forras(skill):
    return skill / "assets" / "adatok" / "forrasok" / "vilagos-beszed-kisokos-2025.toml"


@pytest.fixture
def szabalydir(skill):
    return skill / "assets" / "adatok" / "szabalyok"


def test_lekepezetlen_tetel(skill, forras, capsys):
    csere(forras, 'kihagyva = "Motiváció; a skill céljaként', 'megjegyzes_x = "Motiváció; a skill céljaként')
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1
    assert "vilagos-beszed-kisokos-2025#001 tétel leképezetlen" in hiba
    assert "vilagos-beszed-kisokos-2025.toml:" in hiba


def test_ket_lekepezes(skill, forras, capsys):
    csere(forras, 'kihagyva = "Motiváció; a skill céljaként', 'szabalyok = ["K001"]\nkihagyva = "Motiváció; a skill céljaként')
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "pontosan egy leképezése" in hiba


def test_nem_letezo_szabaly(skill, forras, capsys):
    csere(forras, 'szabalyok = ["K068"]', 'szabalyok = ["K999"]')
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "nem létező szabályra mutat: K999" in hiba


def test_nem_letezo_horgony(skill, forras, capsys):
    csere(forras, "references/parancs-audit.md#negy-kerdes", "references/parancs-audit.md#nincs-ilyen")
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "nem létező horgonyra mutat" in hiba


def test_ketiranyu_egyezes(skill, szabalydir, capsys):
    csere(szabalydir / "K068.toml", '  "vilagos-beszed-kisokos-2025#036",\n', "")
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1
    assert "vilagos-beszed-kisokos-2025#036 tétel erre a szabályra mutat" in hiba


def test_forras_nelkuli_aktiv_szabaly(skill, szabalydir, capsys):
    # A K057-nek egyetlen forrása van; ha azt elvesszük, forrás nélkül marad.
    csere(szabalydir / "K057.toml", '  "nav-ertheto-hivatal-2#073",\n', "")
    csere(skill / "assets" / "adatok" / "forrasok" / "nav-ertheto-hivatal-2.toml", 'szabalyok = ["K057"]', 'kihagyva = "teszt"')
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "legalább egy forrása legyen" in hiba


def test_ismetlodo_tetelazonosito(skill, forras, capsys):
    csere(forras, 'azonosito = "vilagos-beszed-kisokos-2025#002"', 'azonosito = "vilagos-beszed-kisokos-2025#001"')
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "ismétlődő tételazonosító" in hiba


def test_semahiba_sorszammal(skill, szabalydir, capsys):
    csere(szabalydir / "K010.toml", 'csoport = "felepites"', 'csoport = "nincs-ilyen"')
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1
    assert "K010.toml:3:" in hiba and "nem megengedett" in hiba


def test_toml_szintaxishiba(skill, szabalydir, capsys):
    csere(szabalydir / "K010.toml", 'cim = "', 'cim = ')
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "K010.toml:2:" in hiba and "hibás TOML-szintaxis" in hiba


def test_hezag_a_szabalyazonositokban(skill, szabalydir, forras, capsys):
    (szabalydir / "K072.toml").unlink()
    csere(forras, 'szabalyok = ["K072"]', 'kihagyva = "teszt"')
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "hiányzik a K072 szabály" in hiba


def test_visszavont_szabalyra_mutato_tetel(skill, szabalydir, capsys):
    csere(szabalydir / "K072.toml", 'allapot = "aktiv"', 'allapot = "visszavont"\nutod = "K073"')
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "visszavont szabályra mutat (K072); a helyes cél: K073" in hiba


def test_kitoltendo_marad(skill, szabalydir, capsys):
    csere(szabalydir / "K010.toml", 'cim = "', 'cim = "KITÖLTENDŐ ')
    ujragenerál(skill, capsys)
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "kitöltetlen sablonmező" in hiba


def test_fejezet_tetel_nelkul(skill, forras, capsys):
    csere(forras, '[[fejezet]]\nazonosito = "f01"', '[[fejezet]]\nazonosito = "f99"\ncim = "Üres"\noldal = "99"\n\n[[fejezet]]\nazonosito = "f01"')
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "fejezetből nincs leltártétel" in hiba


def test_elavult_generalt_fajl(skill, capsys):
    csere(skill / "references" / "szabalyok.md", "# Szabálykatalógus", "# Átírva kézzel")
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "szabalyok.md:3: a generált fájl elavult" in hiba


def test_parancs_hianyzik_a_tablazatbol(skill, capsys):
    (skill / "references" / "parancs-uj.md").write_text(
        (skill / "assets" / "sablonok" / "parancs.md").read_text(encoding="utf-8"), encoding="utf-8")
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1
    assert "`uj` parancs nem szerepel a SKILL.md parancstáblázatában" in hiba
    assert "`uj` parancshoz nincs eval" in hiba


def test_parancsfajl_eltér_a_sablontol(skill, capsys):
    csere(skill / "references" / "parancs-meres.md", "## Mit nem csinál", "## Korlátok")
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "nem egyeznek a sablonnal" in hiba


def test_tores_hivatkozas(skill, capsys):
    csere(skill / "references" / "jogi.md", "(szovegtipusok.md#kotott-szoveg)", "(szovegtipusok.md#nincs)")
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "jogi.md:" in hiba and "nem létező horgonyra" in hiba


def test_katalogusverzio_egyezes(skill, capsys):
    kat = skill / "assets" / "adatok" / "katalogus.toml"
    kat.write_text(re.sub(r'verzio = "[^"]*"', 'verzio = "9.9.9"', kat.read_text(encoding="utf-8")), encoding="utf-8")
    ujragenerál(skill, capsys)
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "forraskatalogus" in hiba


def test_eval_hianyzo_mezo(skill, capsys):
    p = skill.parent / "evals" / "evals.json"
    adat = json.loads(p.read_text(encoding="utf-8"))
    del adat["evals"][0]["parancs"]
    p.write_text(json.dumps(adat, ensure_ascii=False), encoding="utf-8")
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "hiányzik a(z) „parancs” mező" in hiba


def test_changelog_bejegyzes(skill, capsys):
    (skill.parent / "CHANGELOG.md").write_text("# Változásnapló\n", encoding="utf-8")
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "nincs bejegyzés a(z) " in hiba and " verzióhoz" in hiba


def test_hianyzo_ellenorzo_kerdes(skill, szabalydir, capsys):
    p = szabalydir / "K043.toml"
    p.write_text(re.sub(r"^kerdes = .*\n", "", p.read_text(encoding="utf-8"), flags=re.M), encoding="utf-8")
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "K043.toml" in hiba and "kerdes" in hiba


def test_hibas_minta_regex(skill, szabalydir, capsys):
    csere(szabalydir / "K047.toml", 'regex = "\\\\bés\\\\s*/\\\\s*vagy\\\\b"', 'regex = "(nyitott"')
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "K047.toml" in hiba and "regexe hibás" in hiba


def test_gepi_szabaly_meres_nelkul(skill, szabalydir, capsys):
    csere(szabalydir / "K031.toml", 'ellenorzes = "itelet"', 'ellenorzes = "gepi"')
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "K031.toml" in hiba and "gépi vagy vegyes" in hiba


def test_szotar_nem_letezo_tetel(skill, capsys):
    p = skill / "assets" / "adatok" / "szotar.toml"
    csere(p, '"vilagos-beszed-kezikonyv-2025#113"', '"vilagos-beszed-kezikonyv-2025#999"')
    kod, _, hiba = ellenoriz(skill, capsys)
    assert kod == 1 and "szotar.toml" in hiba and "#999" in hiba
