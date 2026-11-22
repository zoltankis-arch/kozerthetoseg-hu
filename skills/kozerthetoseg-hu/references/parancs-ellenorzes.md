# Parancs: `ellenorzes`

Teljességi és konzisztencia-ellenőrzést futtat a skill adatain: séma, azonosítók, lefedettség, hivatkozások, generált fájlok.

## Mikor kell

Minden adatmódosítás után (új forrás, új szabály, javítás), kiadás előtt, és ha a hívó azt kérdezi, rendben van-e a skill tudásbázisa. A CI minden pusholáskor lefuttatja.

## Bemenet

Nincs; a szkript a skill mappáját olvassa. Más helyen lévő skillhez: `--gyoker /út/a/skillhez`.

## Lépések

1. Futtasd: `python scripts/ellenorzes.py`.
2. A szkript ellenőrzi:
   - a szabály- és forrásfájlok sémáját (`assets/schemas/`), és hogy a fájlnév egyezik-e az azonosítóval;
   - hogy az azonosítók egyediek, és a szabályazonosítók K001-től hézag nélkül folytonosak (szabályt nem törlünk, visszavonunk);
   - hogy minden leltártételnek pontosan egy célja van, és a cél létezik (szabály, referenciafájl és horgony);
   - hogy minden fejezetből van tétel, vagy indokolva van, miért nincs;
   - hogy minden aktív szabálynak van forrása, és a szabály és a tétel kölcsönösen egymásra mutat;
   - hogy visszavont szabályra nem mutat tétel, és a visszavont szabály utódja aktív;
   - a SKILL.md frontmatterét, a törzs hosszát (legfeljebb 500 sor, kb. 5000 token), a parancstáblázatot, és hogy minden parancsfájl a sablon szakaszait követi;
   - hogy minden parancshoz van eval;
   - a Markdown-hivatkozásokat a SKILL.md-ben és a `references/` fájljaiban;
   - hogy a generált fájlok (`szabalyok.md`, `szabaly-index.md`, a `szabalyok-<csoport>.md` fájlok, `ellenorzo-lista.md`, `szotar.md`, `forrasok.md`, `lefedettseg.md`) frissek;
   - a szótár sémáját, regexeit, és hogy minden pár létező szabályra és leltártételre mutat;
   - hogy minden gépi vagy vegyes szabályhoz tartozik mutató, keresőminta vagy szótárpár;
   - ha a skill a repóban van, hogy a CHANGELOG.md-ben van-e bejegyzés a SKILL.md verziójához.
3. Hibánál a kimenet minden sora `fájl:sor: üzenet` alakú. Javítsd, majd futtasd újra. Elavult generált fájlnál: `python scripts/generalas.py`.

## Kimenet formája

Siker esetén egy sor: „Rendben: N forrás, M leltártétel, K aktív és V visszavont szabály.” Kilépési kód 0.

Hiba esetén a hibák listája, a végén a hibák száma; kilépési kód 1. Ha a megadott mappa nem a skill mappája, kilépési kód 2.

## Mit nem csinál

- Nem javít magától, és nem generál újra; a hibát a hívónak kell kijavítania.
- Nem dönti el, hogy egy tétel tartalmilag jól van-e leképezve; ezt a forrás újraolvasása mutatja meg.
- A `skills-ref validate` ellenőrzést nem helyettesíti; a CI mindkettőt futtatja.

## Példa

Egy tétel a K099 szabályra mutat, amely nem létezik:

```
kozerthetoseg-hu/assets/adatok/forrasok/mintaforras-2026.toml:31: a(z) mintaforras-2026#004 nem létező szabályra mutat: K099

1 hiba. (17 forrás, 345 leltártétel, 83 aktív és 0 visszavont szabály)
```
