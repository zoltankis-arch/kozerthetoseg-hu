# Hozzájárulás

Köszönjük, hogy javítanád a skillt. Ez a leírás lépésről lépésre mutatja meg, hogyan vehetsz fel új forrást, új szabályt és új parancsot, és mikor melyik verziószám emelkedik.

A közreműködésre a [magatartási kódex](CODE_OF_CONDUCT.md) vonatkozik.

## Előkészület

```
git clone https://github.com/zoltankis-arch/kozerthetoseg-hu
cd kozerthetoseg-hu/kozerthetoseg-hu
python --version          # 3.11 vagy újabb
python scripts/ellenorzes.py
```

A szkriptek csak a standard könyvtárat használják. A tesztekhez a repó gyökerében: `python -m pip install pytest`, majd `python -m pytest`.

## Hogyan épül fel az adat

- `assets/adatok/szabalyok/K001.toml` és társai: egy szabály egy fájl. Ez az igazság forrása.
- `assets/adatok/forrasok/<azonosító>.toml`: forrásrekord és forrásleltár egy fájlban.
- `assets/adatok/katalogus.toml`: a forráskatalógus verziója.
- `assets/schemas/`: a két fájltípus mezőinek leírása (JSON Schema).
- `assets/sablonok/`: a szkriptek és az új parancsok sablonjai.
- `references/szabalyok.md`, `szabaly-index.md`, `szabalyok-<csoport>.md`, `ellenorzo-lista.md`, `forrasok.md`, `lefedettseg.md`: generált fájlok. Kézzel ne szerkeszd őket; a `scripts/generalas.py` írja újra.

Miért így? Az adat és a szöveg külön van, ezért egy új forrás felvétele adatfelvitel, és a lefedettség gépileg ellenőrizhető. A TOML-t a Python 3.11 óta a standard könyvtár olvassa, nem kell külső csomag. Minden adat a skill mappáján belül van, így a skill bárhová telepítve önálló, és a bővítés telepítés után is működik.

## Új forrás felvétele

A teljes leírás a [parancs-forras-felvetel.md](kozerthetoseg-hu/references/parancs-forras-felvetel.md) fájlban van; röviden:

1. Forrásrekord:

   ```
   python scripts/uj_forras.py kiado-rovidcim-2026 --cim "Cím" --kiado "Kiadó" --ev 2026 --url https://... --prioritas A
   ```

   Töltsd ki a KITÖLTENDŐ mezőket. Licenc: ha a forrás nem mondja ki, írd be, hogy nincs feltüntetve. Helyi elérési út nem kerülhet a fájlba.

2. Forrásleltár: a tartalomjegyzék minden fejezete egy `[[fejezet]]`, és fejezetről fejezetre minden szabály, ajánlás, ellenőrzőlista-pont, tilalom és előtte–utána példa egy `[[tetel]]`, oldalszámmal, saját szavaiddal. A következő szabad tételazonosító: `python scripts/uj_forras.py --kovetkezo-tetel kiado-rovidcim-2026`.

3. Összevonás: ha egy tételt már egy szabály kimond, a tétel arra a szabályra mutasson, és a szabály `forrasok` listájába is írd be. Ha a tétel ellentmond egy másik forrásnak, a szabályba kerüljön `[[elteres]]` bejegyzés: mit mond az egyik, mit a másik, mit követ a skill és miért.

4. Leképezés: minden tételnek pontosan egy célja van: `szabalyok`, `referencia` vagy `kihagyva` (egy mondat indoklással).

5. Példák: a forrás példáiból a mintázatot vedd át, ne a szöveget; a szabály példája saját példa legyen.

Utána:

```
python scripts/generalas.py
python scripts/ellenorzes.py
```

Ha egy fejezetből egy tétel sem kerül be, a fejezet `tetel_nelkul` mezőjében indokold; enélkül az ellenőrzés hibát jelez.

Végül vedd fel a forrást a README „A felhasznált források” táblázatába, a tételszámmal és a forrás URL-jével vagy DOI-jával. A `tests/test_readme.py` teszt jelzi, ha kimaradt.

## Új szabály felvétele

1. `python scripts/uj_szabaly.py --cim "A szabály címe" --csoport mondat` (a csoportok listája: `python scripts/uj_szabaly.py --help`). A szkript a következő szabad azonosítót adja. Egyszer kiosztott azonosítót nem használunk újra.
2. Töltsd ki: a szabály egy mondatban, miért segít az olvasónak, egy eldöntendő ellenőrző kérdés (`kerdes`; az igen válasz jelenti a megfelelést), saját rossz és jó példa, kivételek, alkalmazási kör (`altalanos` vagy `jogi`), alapértelmezett súlyosság (`sulyossag`: `magas`, `kozepes`, `alacsony`), és az ellenőrzés módja (`ellenorzes`): `gepi`, ha a mérőszkript megbízhatóan jelzi, `vegyes`, ha jelöltet ad, `itelet`, ha csak olvasva ellenőrizhető. Gépi vagy vegyes szabálynál kell `meres` mező (beépített mutató), `[[minta]]` (keresőminta) vagy szótárpár; különben az ellenőrzés hibát jelez.
3. Forrás nélküli szabályt nem veszünk fel: a leltárban legalább egy tétel mutasson rá, és a szabály `forrasok` listája ugyanezt tartalmazza.
4. Generálás és ellenőrzés, mint fent.

Szabályt nem törlünk. Ha egy szabály meghaladottá válik, visszavonjuk: `allapot = "visszavont"`, `utod = "K0xx"`, `visszavonas_oka = "..."`, és a rá mutató tételeket az utódra irányítjuk.

## Szótárpár felvétele

A szótár (`assets/adatok/szotar.toml`) körülményes kifejezéseket és egyszerűbb megfelelőjüket tartja. Egy pár egy `[[par]]`:

```toml
[[par]]
kifejezes = "amennyiben"
regex = "\\bamennyiben\\b"
javaslat = "ha"
szabaly = "K036"
forrasok = ["vilagos-beszed-kezikonyv-2025#112"]
mikor_nem = "elhagyható: mikor ne cseréld"
```

Minden párnak legyen forrása a leltárból, és ha a csere nem mindig helyes, a `mikor_nem` mező mondja meg, mikor nem. Utána futtasd a generálást (ez frissíti a `references/szotar.md`-t) és az ellenőrzést.

## Új parancs felvétele

1. Másold az `assets/sablonok/parancs.md` sablont `references/parancs-<név>.md` néven, és töltsd ki a szakaszait (Mikor kell, Bemenet, Lépések, Kimenet formája, Mit nem csinál, Példa). A szakaszok neve és sorrendje nem változhat; az ellenőrzés ezt figyeli.
2. Vegyél fel egy sort a SKILL.md parancstáblázatába: `` | `<név>` | mit csinál | [parancs-<név>.md](references/parancs-<név>.md) | ``.
3. Írj legalább egy evalt az `evals/evals.json`-ba, a `parancs` mezőben az új parancs nevével, és ha kell, tesztszöveget az `evals/szovegek/` mappába.
4. Vegyél fel bejegyzést a CHANGELOG.md-be.
5. `python scripts/ellenorzes.py`: jelzi, ha a táblázat, a fájl vagy az eval hiányzik.

## Verziók

A skill a [szemantikus verziókezelést](https://semver.org/lang/hu/) követi. A verzió a SKILL.md `metadata.version` mezőjében, a forráskatalógus verziója a `metadata.forraskatalogus` mezőben és az `assets/adatok/katalogus.toml`-ban áll; a kettőt együtt emeljük.

| Változás | Emelés |
|---|---|
| Új forrás vagy új szabály | minor (1.0.0 → 1.1.0) |
| Megfogalmazás javítása, elírás, példa cseréje | patch (1.0.0 → 1.0.1) |
| Szabály visszavonása, parancs átnevezése vagy törlése | major (1.0.0 → 2.0.0) |

Kiadáskor frissítsd a CITATION.cff `version` és `date-released` mezőjét, valamint a README verziójelvényét. A Codex-plugin verzióját a `.codex-plugin/plugin.json` fájlban igazítsd a skill verziójához.

Minden kiadás a CHANGELOG.md-ben kap bejegyzést ([Keep a Changelog](https://keepachangelog.com/hu/1.1.0/) formában), és a `main` ág megfelelő commitja `vX.Y.Z` címkét.

## Amit ne tegyél a repóba

- forrás-PDF-et és más, a forrás szövegét nagyobb részben tartalmazó fájlt;
- helyi elérési utat;
- személyes vagy ügyfélhez köthető adatot, és semmit, ami egy konkrét megbízásra utal. A tesztszövegek kitaláltak.

## Pull request

A PR-sablon ellenőrzőlistája szerint: generált fájlok frissek, ellenőrzés és tesztek zöldek, CHANGELOG frissítve. A CI ugyanezt futtatja, és a `skills-ref validate` ellenőrzést is.
