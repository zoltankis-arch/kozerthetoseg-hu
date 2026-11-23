import json
import sys
import types

import meres
from conftest import EVALS, SKILL, futtat


def test_mondatbontas_roviditesek_es_datumok():
    szoveg = ("A határidő 2026. április 4-én jár le. Pl. Kovács J. Péter is beadta. "
              "A díj 5000 Ft. Fizesse be! A 3. § szerint kell eljárni. Kérdése van? Hívjon.")
    m = meres.mondatokra_bont(szoveg)
    assert m == [
        "A határidő 2026. április 4-én jár le.",
        "Pl. Kovács J. Péter is beadta.",
        "A díj 5000 Ft.",
        "Fizesse be!",
        "A 3. § szerint kell eljárni.",
        "Kérdése van?",
        "Hívjon.",
    ]


def test_markdown_elofeldolgozas():
    szoveg = ("---\nname: x\ndescription: frontmatter. Nem mondat.\n---\n<!-- megjegyzés. Ez nem mondat. -->\n# Cím\n\nElső bekezdés.\n\n"
              "- listaelem egy\n- listaelem kettő\n\n| a | b |\n|---|---|\n| c | d |\n\n"
              "```\nkód. Ez sem mondat.\n```\nA `kód` itt sorközi.")
    egysegek = meres.elofeldolgoz(szoveg)
    fajtak = [f for f, _ in egysegek]
    assert fajtak.count("cim") == 1
    assert fajtak.count("listaelem") == 2
    assert fajtak.count("tablazat") == 2
    teljes = " ".join(t for _, t in egysegek)
    assert "megjegyzés" not in teljes
    assert "frontmatter" not in teljes
    assert "Ez sem mondat" not in teljes
    assert "kód" not in teljes


def test_mutatok():
    szoveg = ("A határozat a kérelmező részére megküldésre kerül, illetve a Hatóság által történő "
              "felülvizsgálásra kerül sor (a GDPR (6. cikk (1) bekezdés)). Amennyiben kérdése van, "
              "a nyilatkozat nem mellőzhető. Az adatkezelési-tájékoztató-módosítás kötelező.")
    e, _ = meres.mer(szoveg)
    assert e["kerul_szerkezet"]["db"] == 2
    assert e["altal_torteno_valo"]["által"]["db"] == 1
    assert e["altal_torteno_valo"]["történő"]["db"] == 1
    assert e["illetve_illetoleg"]["illetve"] == 1
    assert e["zarojelmelyseg"]["legnagyobb_melyseg"] == 3
    assert e["tagadas"]["db"] == 1
    assert any(h["fordulat"] == "amennyiben" for h in e["hivatali_fordulatok"])
    assert e["hosszu_szavak"]["db"] >= 1
    assert e["fonevesites"]["jeloltek"] >= 2


def test_kuszob_feletti_mondatok():
    hosszu = " ".join(["szó"] * 25) + "."
    e, _ = meres.mer(hosszu + " Rövid mondat.")
    assert e["mondathossz"]["kuszob_feletti"] == 1
    assert e["mondathossz"]["maximum"] == 25


def test_lexikalizalt_fonev_nem_jelolt():
    e, _ = meres.mer("A kérdése és a szerződés bekezdése rendben van.")
    assert e["fonevesites"]["jeloltek"] == 0


def test_cli_markdown_es_json(tmp_path, capsys):
    f = tmp_path / "a.md"
    f.write_text("Megküldésre kerül a határozat. Ezt fizesse be!", encoding="utf-8")
    kod, ki, _ = futtat(meres, [str(f)], capsys)
    assert kod == 0
    assert ki.splitlines()[2].startswith("> A mérőszám jelzés, nem ítélet.")
    assert "két jelentésben" in ki
    kod, ki, _ = futtat(meres, ["--json", str(f)], capsys)
    assert kod == 0
    adat = json.loads(ki)
    assert list(adat)[0] == "figyelmeztetes"
    assert adat["kerul_szerkezet"]["db"] == 1


def test_determinisztikus(capsys):
    f = EVALS / "szovegek" / "03-hatosagi-level.md"
    _, egy, _ = futtat(meres, ["--json", str(f)], capsys)
    _, ketto, _ = futtat(meres, ["--json", str(f)], capsys)
    assert egy == ketto


def test_hibak(tmp_path, capsys):
    kod, _, hiba = futtat(meres, [str(tmp_path / "nincs.md")], capsys)
    assert kod == 2 and "nem található" in hiba
    ures = tmp_path / "ures.md"
    ures.write_text("  \n", encoding="utf-8")
    kod, _, hiba = futtat(meres, [str(ures)], capsys)
    assert kod == 2 and "üres" in hiba
    kod, _, hiba = futtat(meres, ["--kuszob", "0", str(ures)], capsys)
    assert kod == 2


def test_huspacy_hianyzik(tmp_path, capsys, monkeypatch):
    monkeypatch.setitem(sys.modules, "spacy", None)
    f = tmp_path / "a.md"
    f.write_text("Egy mondat.", encoding="utf-8")
    kod, _, hiba = futtat(meres, ["--huspacy", str(f)], capsys)
    assert kod == 3
    assert "HuSpaCy" in hiba


def test_huspacy_mukodik_hamis_modellel(tmp_path, capsys, monkeypatch):
    class Tok:
        def __init__(self, dep):
            self.dep_ = dep
            self.head = self

    def nlp(szoveg):
        gyoker, a, b = Tok("ROOT"), Tok("nsubj"), Tok("advcl")
        a.head, b.head = gyoker, a
        return [gyoker, a, b]

    hamis = types.SimpleNamespace(load=lambda nev: nlp)
    monkeypatch.setitem(sys.modules, "spacy", hamis)
    f = tmp_path / "a.md"
    f.write_text("Egy mondat. Még egy mondat.", encoding="utf-8")
    kod, ki, _ = futtat(meres, ["--json", "--huspacy", str(f)], capsys)
    assert kod == 0
    h = json.loads(ki)["huspacy"]
    assert h["fuggosegi_melyseg_max"] == 2
    assert h["beagyazott_tagmondatok"] == 2


def test_szabalyonkenti_jelzesek(tmp_path, capsys):
    f = tmp_path / "level.md"
    f.write_text("Amennyiben a kérelem elbírálásra kerül, tájékoztatjuk, hogy a döntés és/vagy "
                 "a határozat postai úton megküldésre kerül.", encoding="utf-8")
    kod, ki, _ = futtat(meres, ["--json", str(f)], capsys)
    assert kod == 0
    j = json.loads(ki)["jelzesek"]
    szabalyok = {x["szabaly"] for x in j}
    assert {"K036", "K043", "K047", "K038"} <= szabalyok
    szotar = [x for x in j if x["honnan"] == "szótár" and "amennyiben" in x["mi"]]
    assert szotar and szotar[0]["javaslat"] == "ha"
    assert all(x["sulyossag"] in ("magas", "kozepes", "alacsony") for x in j)


def test_kozertheto_szovegben_nincs_magas_jelzes(capsys):
    f = EVALS / "szovegek" / "08-kozertheto-level.md"
    kod, _, _ = futtat(meres, ["--max-jelzes", "0", "--szint", "magas", str(f)], capsys)
    assert kod == 0


def test_kuszob_tullepes_kilepesi_kod(capsys):
    f = EVALS / "szovegek" / "03-hatosagi-level.md"
    kod, _, hiba = futtat(meres, ["--max-jelzes", "0", str(f)], capsys)
    assert kod == 1 and "meghaladja" in hiba


def test_ugyanarra_ugyanazt_adja(capsys):
    f = EVALS / "szovegek" / "02-adatkezelesi-reszlet.md"
    _, egy, _ = futtat(meres, ["--json", str(f)], capsys)
    _, ketto, _ = futtat(meres, ["--json", str(f)], capsys)
    assert egy == ketto
