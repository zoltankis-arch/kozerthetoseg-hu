# Közérthetőségi jelentés

Szöveg: „Megkaptuk a parkolási engedély iránti kérelmét” (tárgysor és levél)
Olvasó: lakossági ügyfél (Kovács Anna), aki kérelmet nyújtott be; nem tud szakszavakat vagy jogszabályt. Feltételezés: a kérdező nem adott meg több adatot, ezért ezt a legésszerűbb olvasót vettem alapul. Utána nincs teendője, csak a döntésre vár.
Szövegtípus: nem jogi tájékoztató (hivatali visszaigazoló levél); nem kötelező szöveg, szabadon átírható lenne, de nincs rá szükség.
Jogi modul: nem

## Összkép

A levél már közérthető. Mind a négy kérdésre jó a válasz.
1. Megkapja, amire szüksége van: a levél kimondja, hogy a kérelem megérkezett, mikorra lesz döntés, és hogyan értesítik.
2. Megtalálja: a tárgysor elmondja a lényeget, és a levél rövid, a sorrend természetes (üzenet, határidő, teendő, segítség).
3. Megérti: a mondatok rövidek (átlag 7,4 szó), a szavak köznyelviek, a cselekvő meg van nevezve („elbíráljuk”, „értesítjük”).
4. Használni tudja: a levél kimondja, hogy most nincs teendő (K003), és megadja a telefonszámot és az ügyfélfogadási időt.

A levélben nincs olyan hiba, amit javítani kellene. Ezért nem gyártok kötelező megállapítást. Az alábbi két javaslat alacsony prioritású, és nem kötelező.

## Megállapítások

| # | Hol | Szabály | Mi a baj az olvasónak | Javasolt átírás | Prioritás |
|---|---|---|---|---|---|
| 1 | „A kérelmet 15 napon belül elbíráljuk” | K004 A teendőhöz (és a várakozáshoz) minden szükséges adat | Nem derül ki, mettől számít a 15 nap (a beadástól, a beérkezéstől?). Ez csak akkor számít, ha az olvasó ki akarja számolni a határidőt. | „A kérelmet {a kezdőnap} után 15 napon belül elbíráljuk.” A kezdőnapot a kiadó tudja; én nem találok ki helyette adatot. | alacsony, nem kötelező |
| 2 | „a döntésről levélben értesítjük” | K007 Az olvasó kimondatlan kérdései | Az olvasó megkérdezheti, mit tegyen, ha 15 nap alatt nem érkezik levél. Ezt a levél nem mondja ki, bár a telefonszám megvan. | „Ha 15 napon belül nem kap levelet, hívja ügyfélszolgálatunkat.” Ezt csak akkor érdemes bevenni, ha a kiadó így is kéri. | alacsony, nem kötelező |

Megjegyzés a megszólításról (K049): a „Kedves Kovács Anna!” és az „Ön” együtt szokásos udvarias forma, nem hiba. Nem javaslok változtatást.

## Mérés

A mérőszám jelzés, nem ítélet. A meres.py kimenete (teljes változat: meres.md): 52 szó, 7 mondat, átlagos mondathossz 7,4 szó, a leghosszabb mondat 17 szó, 20 szó feletti mondat nincs. Nincs „kerül”-szerkezet, hivatali fordulat, kettős tagadás vagy „illetve”.

Három gyenge jelzést adott, mindháromnál megnéztem a szöveget, és egyik sem hiba:
- K029 és K032: a „ügyfélszolgálatunkat” 15 betűnél hosszabb. Ez köznyelvi, ismert szó, a levél célközönsége érti. Marad.
- K042: a „döntésről” főnevesítési jelölt, de a „döntés” lexikalizálódott főnév, és a mondat cselekvő igével szól („értesítjük”). Marad.

## Amit a jelentés nem vizsgált

- Olvasói próba nem volt. Egy ilyen rövid, kis tétű levélnél ez nem is szükséges; ha a levelet sok ügyfélnek küldik sablonként, érdemes lehet a `proba` parancsot használni (K076).
- Nem vizsgáltam, hogy a 15 napos határidő és az ügyfélszolgálat nyitva tartása igaz-e; ezt a kiadónak kell ellenőriznie.
- Értelmi fogyatékossággal élő vagy alacsony nyelvi kompetenciájú olvasót nem feltételeztem; ha ilyen is olvassa, ahhoz könnyen érthető (KÉK) kommunikáció kell, amit ez a jelentés nem pótol.
