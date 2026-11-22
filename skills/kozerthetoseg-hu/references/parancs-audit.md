# Parancs: `audit`

Jelentést ad egy szöveg közérthetőségéről a szabálykatalógus szerint. Nem ír át.

## Mikor kell

Ha a hívó azt kéri, hogy nézd át, értékeld, ellenőrizd vagy véleményezd egy magyar szöveg érthetőségét, de nem kér átírást. Ha átírást kér, az `atiras` parancs fut; ha csak számokat, a `meres`.

Ne induljon nem magyar szövegre (mondd meg, hogy a szöveg nem magyar), gép–gép kimenetre (JSON, napló, kód) és szépirodalomra.

## Bemenet

- A vizsgálandó szöveg (beillesztve vagy fájlban).
- Az olvasó és a cél: ki olvassa, mit tud, mit kell tennie utána. Ha a hívó nem adja meg, egy kérdésben kérdezz rá; ha nincs kit kérdezni, írd le, milyen olvasót feltételeztél.
- Elhagyható: a szöveg műfaja, a kiadó szervezet, a megszólítás (alapértelmezés a magázás, ha a szöveg nem dönt).

## Lépések

1. Olvasó és cél. Rögzítsd egy-egy mondatban.
2. Szövegtípus. Sorold be a [szovegtipusok.md](szovegtipusok.md) szerint. Ha kötelező szövegről van szó (jogszabály, előírt formula, jogszabályban megállapított feltétel, kamarai egységes szöveg), a jelentés ezt mondja ki, és csak a köré írt tájékoztató részt vizsgálja.
3. KÉK-határ. Ha az olvasó értelmi fogyatékossággal élő vagy alacsony nyelvi kompetenciájú, mondd ki a [kek-hatar.md](kek-hatar.md) szerint, hogy ehhez könnyen érthető kommunikáció kell, és ez a jelentés azt nem pótolja.
4. Keret: a négy kérdés (lent). Ezekre adj rövid összképet.
5. Vizsgálat a [szabaly-index.md](szabaly-index.md) szerint, csoportonként; a részleteket a vonatkozó szabályoknál nyisd meg a csoportfájlban. Minden megállapításnál: hol van (idézd a rövid szövegrészt), melyik szabályt sérti (azonosítóval), miért baj az olvasónak, javasolt átírás, prioritás.
6. Mérés: futtasd a `scripts/meres.py`-t, és jelzésként értelmezd ([parancs-meres.md](parancs-meres.md)).
7. Jogi szövegnél töltsd be a [jogi.md](jogi.md) modult is, és a jelentés végén írd ki: a jelentés nem jogi tanács, a jogi tartalom változatlanságáért a szakember felel.

<a id="negy-kerdes"></a>

### A négy kérdés

Az ISO 24495-1 szabvány négy elve, a Világos Beszéd, a NAV és Gerencsér meghatározásával egybevágva:

1. Megkapja-e az olvasó, amire szüksége van? (cél és tartalom: K001–K009)
2. Megtalálja-e? (felépítés és kinézet: K010–K018, K051–K055)
3. Megérti-e? (mondat, szó, szerkezet: K019–K050)
4. Tudja-e használni? (teendő, határidő, segítség: K003, K004, nyomtatványnál K068–K073)

### Prioritás

- magas: az olvasó emiatt nem tudja, mit kell tennie, vagy félreérti (hiányzó teendő vagy határidő, félrevezető szó, kettős tagadás egy feltételben);
- közepes: a megértés lassabb vagy több erőfeszítést kér (hosszú mondat, főnevesítés, a jogszabályhely a mondat közepén);
- alacsony: forma és stílus (kiemelés, dátumforma, felesleges igekötő).

Ha egy szabály több helyen sérül, egy megállapítás elég, a helyek felsorolásával.

## Kimenet formája

Az [assets/sablonok/jelentes.md](../assets/sablonok/jelentes.md) szerinti jelentés: fejléc (olvasó, szövegtípus, jogi modul), összkép a négy kérdés szerint, megállapítások táblázatban, mérés, és mit nem vizsgált a jelentés.

Ha a szöveg már közérthető, ezt mondd ki, és ne gyárts megállapítást. Kis javaslat (alacsony prioritás) lehet, de jelöld, hogy nem kötelező.

## Mit nem csinál

- Nem írja át a szöveget (arra az `atiras` való); a javasolt átírás csak az adott szövegrészre vonatkozik.
- Nem dönti el, hogy a jogi tartalom helyes-e.
- Nem pótolja az olvasói próbát; ha a tét nagy, javasold a `proba` parancsot.

## Példa

Bemenet: „A kérelem elbírálásra került, a határozat postai úton megküldésre kerül.” Olvasó: lakossági ügyfél.

Kimenet (részlet):

| # | Hol | Szabály | Mi a baj az olvasónak | Javasolt átírás | Prioritás |
|---|---|---|---|---|---|
| 1 | „elbírálásra került” | K043 | Nem derül ki, ki döntött, és mi lett a döntés. | „Elbíráltuk a kérelmét.” és a döntés maga | magas |
| 2 | teljes mondat | K003 | Nem derül ki, van-e teendője. | „A határozatot postán küldjük el. Önnek nincs teendője.” | magas |
