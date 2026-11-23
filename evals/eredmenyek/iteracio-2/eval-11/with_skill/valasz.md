# Mérés: hiánypótlási felhívás

A mérőszám jelzés, nem ítélet. Azt mutatja meg, hol érdemes ránézni a szövegre, azt nem, hogy közérthető-e. (Üveges 2026 korpuszán a felszíni jegyekre épített modell F1 értéke 0,58 volt.)

## Feltételezések

Nem tudtam kérdezni, ezért ezt feltételeztem:
- Az olvasó laikus magánszemély, aki építési engedélyt kért, és most hiánypótlást kapott. Nem jogász, és nem ismeri az eljárás menetét.
- A szöveg eljárási vegyes szöveg (hatósági felhívás). A szerkezete és a mondatai javíthatók, de a jogi elemek maradnak: a határidő, a jogkövetkezmény és a jogszabályhely.
- A skill a mérésen kívül mást nem kért tőlem, ezért nem írtam át a levelet. Ha átírást is kér, az `atiras` parancsot kell futtatni.

## A mért értékek

A szkript 83 szót és 6 mondatot számolt.

| Mutató | Érték |
|---|---|
| Átlagos mondathossz | 13,8 szó (medián 7,5) |
| Leghosszabb mondat | 37 szó |
| 20 szó feletti mondat | 2 |
| Főnevesítési jelölt | 10 (12 / 100 szó) |
| „-ásra/-ésre kerül” szerkezet | 5 |
| Hivatali fordulat | 3 |
| 15 betűnél hosszabb szó | 1 (tudomásulvételét) |
| Zárójelmélység | 1 |

## Mire figyelj

1. **A 4. mondat (37 szó) túl sokat visz egyszerre (K020, K023, súlyosság: közepes).** Ebben van a teendő (a nyilatkozat benyújtása), a határidő (15 nap) és a jogkövetkezmény (megszüntetés). Érdemes három külön mondatra bontani. A teendő és a határidő álljon elöl. A 3. mondat (26 szó) is hosszú, mert az ügyet, az elbírálást és a hiányt egyben mondja.
2. **Az öt „kerül”-szerkezet elrejti, ki mit csinál (K043, gépi jelzés, közepes).** Ilyen az „elbírálásra került”, a „megállapításra került”, a „csatolásra nem került”, a „benyújtására kerüljön sor” és a „megszüntetésre kerül”. Az olvasó nem tudja meg, hogy a hatóság bírált el, és hogy ő nem csatolt valamit. A mérés javaslata az „elbíráljuk”. A többi helyen is cselekvő igét érdemes keresni.
3. **Sok a főnevesítés (K042, jelölt, közepes).** A 10 jelölt között van igazi főnevesítés (benyújtására, csatolásra, elbírálásra, megállapításra, megszüntetésre), de a „felhívás”, az „eljárás” és a „hiánypótlás” a szövegben megszokott szó, ezeket nem kell cserélni. Nézd meg olvasva, melyik valódi gond.
4. **A jogszabályhely a mondat közepén áll (K012, jelölt, magas).** A „2016. évi CL. törvény 47. § (1) bekezdés b) pontja” megszakítja a mondatot. Ezt a mérés magas súlyúnak jelzi. A hivatkozás tartalmához nem nyúlhatsz, de áthelyezheted a mondat végére, vagy külön, zárójeles mondatba. A hivatkozás helyességét a jogi szakembernek kell ellenőriznie, ezt a skill nem vizsgálja.
5. **Hivatali fordulatok (K035, K036, K045, K050, közepes):**
   - A „Tájékoztatjuk, hogy” elhagyható.
   - A „Fentiekre tekintettel felhívjuk” helyett elég: „Kérjük, pótolja…”.
   - A záró „Kérjük tájékoztatásunk szíves tudomásulvételét” nem mond semmit, és ez a legnehezebb szó is (K029, K032). Hagyd el, vagy zárd azzal, hogy hova fordulhat kérdéssel.
6. **A „postai úton” (K038, jelölt, közepes).** Egyszerűbb a „postán”. Írd oda azt is, hogy az elektronikus felületen hol és hogyan nyújtható be a pótlás, és mi a postai cím.

## Amit a szkript nem lát, olvasva nézd meg

- **Fő üzenet és teendő (K002–K004):** a levél a 3. mondatig a múltról szól, a teendő csak a 4. mondatban jön. A tárgysor („Hiánypótlási felhívás”) nem mondja meg, mit kell tenni. Olvasva ez a legfontosabb gond.
- **Határidő:** „a kézhezvételtől számított 15 nap” nem dátum, és az olvasó nem tudja kiszámolni. Ha a hatóság tudja a pontos dátumot, érdemes megadni. Ezt én nem írom be, mert nem ismerem. Átírásnál helyőrző kellene.
- **Mi az a tervezői nyilatkozat, és hol szerezhető be:** a szöveg ezt nem mondja.
- **Következmény:** az „eljárás megszüntetésre kerül” kimondhatná, hogy a kérelem nem lesz elbírálva.

## Összkép

A szöveg rövid, a mérőszámok nem extrémek, a fő baj a szerkezet: a teendő későn jön, és egy túl hosszú mondatban van. A hosszú mondat, a „kerül”-szerkezet és a jogszabályhely együtt a legfontosabb három teendő, ebben a sorrendben. Mivel a határidő elmulasztása az eljárás megszűnésével jár, az átírt változatot érdemes olvasói próbával is kipróbálni (`proba` parancs).

A skill nem ad jogi tanácsot. A jogi tartalom változatlanságáért a szakember felel.

## Mentett fájlok

- `meres-kimenet.md`: a szkript teljes kimenete
- `meres-kimenet.json`: ugyanez gépi formában
