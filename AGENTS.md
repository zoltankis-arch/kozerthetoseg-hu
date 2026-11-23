# Útmutató kódoló agenteknek

Ez a fájl annak az agentnek szól, amely a repón dolgozik. Leírja, mit hol talál, és mit nem szabad elrontania. Az emberi közreműködőknek a [CONTRIBUTING.md](CONTRIBUTING.md) szól.

## Mi van a repóban?

- `skills/kozerthetoseg-hu/`: maga a skill. Csak ez kerül a felhasználóhoz.
  - `SKILL.md`: a prompt, amelyet az asszisztens olvas.
  - `assets/adatok/`: a szabályok, a források és a szótár TOML-ban. Ez az igazság forrása.
  - `references/`: generált referenciák, a `parancs-*.md`, a `jogi.md`, a `kek-hatar.md` és a `szovegtipusok.md` kivételével.
  - `scripts/`: a mérő-, generáló- és ellenőrzőszkriptek. Csak a Python 3.11 szabványos könyvtárát használják.
- `evals/`: az evalok (`evals.json`), a bemeneti szövegek (`szovegek/`) és a futtatások nyers eredménye (`eredmenyek/`).
- `tests/`: pytest-tesztek. `tools/`: az eval-összesítő szkript.
- `plugin.json`, `.claude-plugin/`, `.codex-plugin/`, `.agents/`: a manifestek. Az Agent Plugins, a Claude és a Codex mindegyik a saját fájlját olvassa. A Claude-piactér csak a `skills/kozerthetoseg-hu/` mappát telepíti.
- `docs/`: telepítés, forráslista, roadmap. `examples/`: előtte–utána példák.

## Szabályok

1. A `references/` generált fájljait ne szerkeszd kézzel. Módosítsd a TOML-adatot, majd futtasd a `generalas.py`-t és az `ellenorzes.py`-t (a parancsokat lásd lent).
2. Új szabály vagy forrás a `scripts/uj_szabaly.py` és a `scripts/uj_forras.py` szkripttel készüljön, a CONTRIBUTING.md lépései szerint.
3. A forrásokból ne másolj át hosszabb szövegrészt. A repó nyilvános: szabályt és mintázatot vegyél át, rövid idézetet csak forrásmegjelöléssel.
4. A repóba nem kerülhet helyi elérési út, személyes adat, ügyféladat, és semmi, ami konkrét megbízásra utal.
5. A verzió hat helyen szerepel, és mindegyiknek egyeznie kell: a SKILL.md `metadata.version` mezője, a `plugin.json`, a `.claude-plugin/marketplace.json` pluginbejegyzése, a `.codex-plugin/plugin.json`, a `CITATION.cff` és a README verziójelvénye. A CHANGELOG-ban is legyen bejegyzés hozzá. A `tests/test_plugin.py` és az `ellenorzes.py` jelzi, ha valamelyik elmaradt.
6. A skill szövege és a dokumentáció magyar, közérthető. Új szöveget futtass át a skill `audit` parancsán.
7. Minden logikai lépés külön commit legyen, értelmes magyar üzenettel.

## Ellenőrzés commit előtt

```
python skills/kozerthetoseg-hu/scripts/generalas.py
python skills/kozerthetoseg-hu/scripts/ellenorzes.py
python -m pytest -q
skills-ref validate skills/kozerthetoseg-hu
python tools/eval_osszesit.py --ellenoriz evals/eredmenyek/iteracio-2
```

Ugyanezt futtatja a CI is.
