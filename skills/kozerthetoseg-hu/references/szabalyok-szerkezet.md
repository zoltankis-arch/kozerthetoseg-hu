<!-- GENERÁLT FÁJL. Ne szerkeszd kézzel: a forrása az assets/adatok/ mappa TOML-fájljai. Újragenerálás: python scripts/generalas.py -->

# Szabályok: Szerkezet

Az összes csoport: [szabaly-index.md](szabaly-index.md).

<a id="k042"></a>

### K042 Ige a főnévvé tett cselekvés helyett

Szabály: Az -ás/-és képzős főnévvel kifejezett cselekvést, különösen az „által”, „történő”, „való” mellett, írd át ragozott igére.

Miért segít: Az igéből képzett főnév elrejti, ki cselekszik és mikor. Az igés mondat rövidebb, és kiderül belőle a cselekvő.

Ellenőrző kérdés: A cselekvéseket ige fejezi ki, nem főnévvé tett ige („által”, „történő”, „való” mellett sem)?

- Rossz: A szerződés a megrendelésnek a szolgáltató által történő visszaigazolásával jön létre.
- Jó: A szerződés akkor jön létre, amikor a szolgáltató visszaigazolja a megrendelést.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: jelölt. Mérés (meres.py): fonevesites, altal_torteno_valo.

Források: [Balogh 2023, 181. o.](forrasok.md#balogh-2023-006); [Európai Bizottság 2013, 8. o.](forrasok.md#eu-pontos-fogalmazas-2013-032); [Európai Bizottság 2013, 8. o.](forrasok.md#eu-pontos-fogalmazas-2013-033); [Horváth 2021, 110. o.](forrasok.md#horvath-2021-024); [NAV 2024b, 23. o.](forrasok.md#nav-ertheto-hivatal-2-041); [NAV 2024b, 30. o.](forrasok.md#nav-ertheto-hivatal-2-051); [NAV 2024b, 30–33. o.](forrasok.md#nav-ertheto-hivatal-2-052); [Világos Beszéd kézikönyv 2025, 16. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-029); [Világos Beszéd kézikönyv 2025, 24. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-058); [Világos Beszéd kézikönyv 2025, 24. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-060); [Világos Beszéd kézikönyv 2025, 24. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-061); [Világos Beszéd kézikönyv 2025, 31. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-091); [Világos Beszéd kézikönyv 2025, 32–33. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-098); [Világos Beszéd 2025, 8. o.](forrasok.md#vilagos-beszed-kisokos-2025-024); [Világos Beszéd 2025, 8. o.](forrasok.md#vilagos-beszed-kisokos-2025-025); [WP260 2018, 10. o.](forrasok.md#wp260-2018-012).

<a id="k043"></a>

### K043 Cselekvő ige az „-ásra/-ésre kerül” helyett

Szabály: Az „-ásra/-ésre kerül” szerkezet helyett nevezd meg a cselekvőt, vagy használj általános alanyt, visszaható vagy más igét.

Miért segít: A „kerül” elvont használatban tartalmatlan ige: a cselekvés magától történik meg, a felelős eltűnik.

Ellenőrző kérdés: Nincs „-ásra/-ésre kerül” szerkezet?

- Rossz: A határozat a kérelmező részére postai úton megküldésre kerül.
- Jó: A határozatot postán elküldjük Önnek.

Kivételek:

- Ha a „kerül” valódi helyváltozást jelent (a pénz a számlára kerül), maradhat.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: gépi. Mérés (meres.py): kerul_szerkezet.

Források: [Európai Bizottság 2013, 10. o.](forrasok.md#eu-pontos-fogalmazas-2013-039); [NAV 2024b, 22. o.](forrasok.md#nav-ertheto-hivatal-2-039); [NAV 2024b, 25. o.](forrasok.md#nav-ertheto-hivatal-2-044); [NAV 2024b, 26. o.](forrasok.md#nav-ertheto-hivatal-2-045); [NAV 2024b, 27–29. o.](forrasok.md#nav-ertheto-hivatal-2-046); [Világos Beszéd kézikönyv 2025, 38. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-115); [Világos Beszéd 2025, 8. o.](forrasok.md#vilagos-beszed-kisokos-2025-025).

<a id="k044"></a>

### K044 Nevezd meg, ki cselekszik

Szabály: A szenvedő szerkezet (el lett intézve), az igenévi állítmány (a kérelem benyújtott) és a személytelen fogalmazás helyett nevezd meg a cselekvőt; ha nem ismert, használj általános alanyt.

Miért segít: Ha nem derül ki, ki cselekszik, az olvasó nem tudja, kinek mi a dolga. Az alany nélküli mondat ködösítésnek is hathat.

Ellenőrző kérdés: Kiderül, ki cselekszik, és nincs szenvedő vagy személytelen szerkezet ott, ahol a cselekvő ismert?

- Rossz: A hiba ki lett javítva, a számla újra lett küldve.
- Jó: Kijavítottuk a hibát, és újra elküldtük a számlát.

Kivételek:

- Általános alanyt (elintézték) csak akkor használj, ha a cselekvőt nem tudod vagy nem lényeges, és ügyelj, hogy az előző mondat alanya ne keveredjen bele.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: jelölt.

Források: [Európai Bizottság 2013, 10. o.](forrasok.md#eu-pontos-fogalmazas-2013-042); [Európai Bizottság 2013, 10. o.](forrasok.md#eu-pontos-fogalmazas-2013-043); [NAV 2024b, 22. o.](forrasok.md#nav-ertheto-hivatal-2-039); [NAV 2024b, 25. o.](forrasok.md#nav-ertheto-hivatal-2-043); [NAV 2024b, 30. o.](forrasok.md#nav-ertheto-hivatal-2-047); [NAV 2024b, 30. o.](forrasok.md#nav-ertheto-hivatal-2-048); [NAV 2024b, 30. o.](forrasok.md#nav-ertheto-hivatal-2-049); [NAV 2024b, 30. o.](forrasok.md#nav-ertheto-hivatal-2-050); [Világos Beszéd kézikönyv 2025, 24. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-058); [Világos Beszéd kézikönyv 2025, 37–38. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-119); [WP260 2018, 10. o.](forrasok.md#wp260-2018-012).

<a id="k045"></a>

### K045 Ige a terpeszkedő szerkezet helyett

Szabály: A főnévből és tartalmatlan igéből álló terpeszkedő szerkezet helyett használd az igét (döntést hoz helyett dönt).

Miért segít: A terpeszkedő szerkezet nem ad hozzá információt, csak hosszabb és hivatalosabb lesz tőle a mondat.

Ellenőrző kérdés: Nincs terpeszkedő szerkezet („döntést hoz” a „dönt” helyett)?

- Rossz: A bizottság a pályázatokról döntést hoz, és a nyertesek részére a támogatás kifizetéséről intézkedik.
- Jó: A bizottság dönt a pályázatokról, és kifizeti a támogatást a nyerteseknek.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: jelölt. Mérés (meres.py): hivatali_fordulatok.

Források: [Európai Bizottság 2013, 8. o.](forrasok.md#eu-pontos-fogalmazas-2013-033); [Európai Bizottság 2013, 10. o.](forrasok.md#eu-pontos-fogalmazas-2013-039); [NAV 2024b, 34. o.](forrasok.md#nav-ertheto-hivatal-2-053); [NAV 2024b, 35. o.](forrasok.md#nav-ertheto-hivatal-2-054); [Világos Beszéd kézikönyv 2025, 24. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-059); [Világos Beszéd kézikönyv 2025, 37–38. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-114).

<a id="k046"></a>

### K046 Kettős tagadás nélkül

Szabály: Ne használj kettős tagadást, a bújtatottat sem (nem + tagadó jelentésű ige vagy szó: nem mellőzhető, nem hiányzik, nem tilos); fogalmazd meg állítóan.

Miért segít: A kettős tagadást az olvasónak kétszer kell megfordítania, és könnyen az ellenkezőjét érti.

Ellenőrző kérdés: Nincs kettős tagadás, rejtett formában sem?

- Rossz: A kérelem nem bírálható el a jövedelemigazolás csatolása nélkül, kivéve, ha nem kötelező csatolni.
- Jó: A kérelemhez csatolja a jövedelemigazolást. Ha nincs jövedelme, ezt elég nyilatkozatban jeleznie.

Kör: általános. Alapértelmezett súlyosság: magas. Ellenőrzés: jelölt. Mérés (meres.py): tagadas.

Források: [Horváth 2021, 109. o.](forrasok.md#horvath-2021-021); [Horváth 2021, 109. o.](forrasok.md#horvath-2021-022); [NAV 2024b, 22–23. o.](forrasok.md#nav-ertheto-hivatal-2-038).

<a id="k047"></a>

### K047 „illetve”, „illetőleg” és „és/vagy” jogi szövegben

Szabály: Jogi szövegben az „illetve” helyett írd ki az egyértelmű kapcsolatot (és, vagy, valamint), az „illetőleg” és az „és/vagy” alakot ne használd.

Miért segít: Az „illetve” jelentheti az „és”-t és a „vagy”-ot is; jogi szövegben ebből vita lesz. A jogszabályszerkesztési rendelet a jogszabálytervezetben ezért korlátozza vagy tiltja ezeket.

Ellenőrző kérdés: Jogi szövegben az „illetve” helyén egyértelmű kötőszó áll, és nincs „illetőleg” vagy „és/vagy”?

- Rossz: A kérelmet a bérlő, illetve a tulajdonos nyújthatja be.
- Jó: A kérelmet a bérlő vagy a tulajdonos nyújthatja be.
- Megjegyzés a példához: A rossz példából nem derül ki, hogy a kérelmet ketten együtt vagy bármelyikük egyedül nyújthatja be; a jó példa ezt eldönti.

Kivételek:

- A rendelet a jogszabály tervezetére kötelező; más jogi szövegnél (szerződés, tájékoztató) a skill ajánlásként alkalmazza.

Kör: csak jogi szövegnél. Alapértelmezett súlyosság: közepes. Ellenőrzés: gépi. Mérés (meres.py): illetve_illetoleg. Keresőminta: „és/vagy”.

Források: [Jszr., 7. § (3)](forrasok.md#jszr-2009-006); [Jszr., 7. § (4)](forrasok.md#jszr-2009-007); [Jszr., 7. § (5)](forrasok.md#jszr-2009-008).
