"""Az összehasonlító evalok összesítése újraszámolható és ellenőrzi magát."""
import importlib.util
import json
import shutil
import sys
from pathlib import Path

GYOKER = Path(__file__).resolve().parent.parent
ITERACIO = GYOKER / "eredmenyek" / "iteracio-2"

spec = importlib.util.spec_from_file_location("eval_osszesit", GYOKER / "tools" / "eval_osszesit.py")
eval_osszesit = importlib.util.module_from_spec(spec)
sys.modules["eval_osszesit"] = eval_osszesit
spec.loader.exec_module(eval_osszesit)


def test_a_commitolt_osszesites_friss(capsys):
    assert eval_osszesit.main(["--ellenoriz", str(ITERACIO)]) == 0


def test_az_ellenorzes_eszreveszi_a_modositott_ertekelest(tmp_path, capsys):
    masolat = tmp_path / "iteracio"
    shutil.copytree(ITERACIO, masolat)
    ert = next(masolat.glob("eval-*/baseline/ertekeles.json"))
    adat = json.loads(ert.read_text(encoding="utf-8"))
    adat["elvarasok"][0]["teljesul"] = not adat["elvarasok"][0]["teljesul"]
    ert.write_text(json.dumps(adat, ensure_ascii=False), encoding="utf-8")
    assert eval_osszesit.main(["--ellenoriz", str(masolat)]) == 1


def test_a_biralat_megfeleltetese(tmp_path, capsys):
    ed = tmp_path / "eval-01"
    for k in ("with_skill", "baseline"):
        (ed / k).mkdir(parents=True)
        (ed / k / "ertekeles.json").write_text(
            json.dumps({"elvarasok": [{"szoveg": "x", "teljesul": k == "with_skill", "indok": "-"}]}),
            encoding="utf-8")
    (ed / "eval_metadata.json").write_text(json.dumps({"id": 1, "eval_name": "proba"}), encoding="utf-8")
    (ed / "biralat.json").write_text(json.dumps({"A": "baseline", "gyoztes": "B", "indok": "-"}), encoding="utf-8")
    o = eval_osszesit.osszesit(tmp_path)
    assert o["evalok"][0]["biralat"] == "with_skill"
    assert o["osszesen"]["elvarasok"]["with_skill"]["teljesult"] == 1
    assert o["osszesen"]["elvarasok"]["baseline"]["teljesult"] == 0
