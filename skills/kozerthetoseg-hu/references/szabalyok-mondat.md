<!-- GENERÁLT FÁJL. Ne szerkeszd kézzel: a forrása az assets/adatok/ mappa TOML-fájljai. Újragenerálás: python scripts/generalas.py -->

# Szabályok: Mondat

Az összes csoport: [szabaly-index.md](szabaly-index.md).

<a id="k019"></a>

### K019 Egy mondat, egy dolog

Szabály: Egy mondat egy gondolatot, egy információt közöljön; két ellentétes közlést ne zsúfolj egy mondatba.

Miért segít: Az olvasó mondatonként dolgozza fel a szöveget. Ha egy mondatban több állítás van, könnyen csak az egyiket jegyzi meg, és az ellentétes közlések egymást teszik nehezen érthetővé.

Ellenőrző kérdés: Minden mondat egy dologról szól?

- Rossz: A bérletet csak személyesen lehet megvásárolni, de a meghosszabbítás online is lehetséges, amennyiben a bérlet még érvényes.
- Jó: A bérletet személyesen vásárolhatja meg. Amíg a bérlet érvényes, online is meghosszabbíthatja.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: olvasva.

Források: [Horváth 2021, 108–109. o.](forrasok.md#horvath-2021-019); [NAV 2024b, 22. o.](forrasok.md#nav-ertheto-hivatal-2-037); [Világos Beszéd kézikönyv 2025, 25. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-065); [Világos Beszéd kézikönyv 2025, 26. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-066); [Világos Beszéd kézikönyv 2025, 31. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-093); [Világos Beszéd kézikönyv 2025, 32–33. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-098); [Világos Beszéd 2025, 8. o.](forrasok.md#vilagos-beszed-kisokos-2025-027).

<a id="k020"></a>

### K020 Mondathossz: átlagosan 15–20 szó

Szabály: A mondatok átlagosan 15–20 szóból álljanak; a 20 szónál hosszabb mondatot nézd meg, bontható-e.

Miért segít: A hosszú mondatban az olvasónak sok mindent kell fejben tartania, mire a végére ér. A küszöb figyelmeztet, nem tilt: a mérőszám jelzés, nem ítélet.

Ellenőrző kérdés: A mondatok átlagosan 15–20 szavasak, és a 20 szónál hosszabbakat megnézted, bonthatók-e?

- Rossz: A kérelem benyújtását követően a hatóság a kérelemben foglaltakat a rendelkezésére álló nyilvántartások alapján megvizsgálja, és amennyiben hiányosságot állapít meg, a kérelmezőt határidő tűzésével hiánypótlásra hívja fel. (27 szó)
- Jó: Megvizsgáljuk a kérelmét. Ha valami hiányzik, levélben kérjük, hogy pótolja, és megadjuk a határidőt. (14 szó, két mondatban)

Kivételek:

- Felsorolást tartalmazó mondat hosszabb lehet, ha listába tördeled.
- A szám önmagában nem dönt: egy 22 szavas, világos szórendű mondat jobb lehet két rosszul összekötött rövidnél.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: jelölt. Mérés (meres.py): mondathossz.

Források: [Balogh 2023, 186–187. o.](forrasok.md#balogh-2023-014); [Európai Bizottság 2013, 6. o.](forrasok.md#eu-pontos-fogalmazas-2013-022); [NAV 2024a, 10. o.](forrasok.md#nav-ertheto-hivatal-1-005); [Üveges 2026, 9. o.](forrasok.md#uveges-2026-003); [Világos Beszéd kézikönyv 2025, 25. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-065); [Világos Beszéd kézikönyv 2025, 31. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-093); [Világos Beszéd kézikönyv 2025, 32–33. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-098); [Világos Beszéd 2025, 8. o.](forrasok.md#vilagos-beszed-kisokos-2025-027).

Ha a források eltérnek: A Világos Beszéd kisokosa szerint egy mondat legfeljebb 15–20 szóból álljon, a kézikönyv szerint húsz szónál semmiképp se legyen hosszabb; az uniós útmutató ugyanezt átlagként adja meg. Üveges korpuszában a szakértők által közérthetőre átírt hivatali mondatok átlaga is 25 token fölött van. A skill döntése: A skill az átlagot követi (15–20 szó), és a 20 szó feletti mondatot jelöltként mutatja, nem hibaként. Ok: jogi és hivatali szövegben egy pontos feltétel gyakran hosszabb mondatot kíván, és Üveges eredménye szerint a felszíni hossz önmagában nem dönti el az érthetőséget. ([Világos Beszéd 2025, 8. o.](forrasok.md#vilagos-beszed-kisokos-2025-027); [Világos Beszéd kézikönyv 2025, 25. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-065); [Európai Bizottság 2013, 6. o.](forrasok.md#eu-pontos-fogalmazas-2013-022); [Üveges 2026, 9. o.](forrasok.md#uveges-2026-003))

<a id="k021"></a>

### K021 Az alany és az állítmány elöl, egymás közelében

Szabály: A mondat elején álljon, kire vonatkozik (alany) és mit kell tennie (állítmány), egymáshoz közel; a bővítmények csak utánuk jöjjenek.

Miért segít: Ha az állítmány a mondat végére kerül, az olvasónak az egész mondatot fejben kell tartania, mire megtudja, mi a lényeg.

Ellenőrző kérdés: A mondatok elején, egymás közelében áll az alany és az állítmány?

- Rossz: A bérlőnek a lakásban végzett, a bérbeadó előzetes írásbeli hozzájárulásához kötött átalakítási munkák megkezdése előtt értesítési kötelezettsége áll fenn.
- Jó: A bérlőnek értesítenie kell a bérbeadót, mielőtt átalakítási munkába kezd. Ehhez a bérbeadó előzetes írásbeli hozzájárulása kell.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: olvasva.

Források: [Balogh 2023, 183. o.](forrasok.md#balogh-2023-008); [Horváth 2021, 105. o.](forrasok.md#horvath-2021-009); [NAV 2024b, 20–21. o.](forrasok.md#nav-ertheto-hivatal-2-031); [NAV 2024b, 21. o.](forrasok.md#nav-ertheto-hivatal-2-033); [NAV 2024b, 22. o.](forrasok.md#nav-ertheto-hivatal-2-034); [Világos Beszéd kézikönyv 2025, 26. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-067); [Világos Beszéd 2025, 8. o.](forrasok.md#vilagos-beszed-kisokos-2025-028).

<a id="k022"></a>

### K022 Feltételes mondat a feltétellel kezdődjön

Szabály: Ha egy mondat csak bizonyos esetben érvényes, a feltétel álljon az elején.

Miért segít: Az olvasó a mondat elején eldöntheti, vonatkozik-e rá; ha nem, továbbléphet.

Ellenőrző kérdés: A feltételes mondatok a feltétellel kezdődnek?

- Rossz: Csatolja a gyámhatóság engedélyét, ha a kérelmező kiskorú.
- Jó: Ha a kérelmező kiskorú, csatolja a gyámhatóság engedélyét.

Kör: általános. Alapértelmezett súlyosság: magas. Ellenőrzés: olvasva.

Források: [NAV 2024b, 22. o.](forrasok.md#nav-ertheto-hivatal-2-035); [Világos Beszéd kézikönyv 2025, 24. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-060); [Világos Beszéd kézikönyv 2025, 26. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-070).

<a id="k023"></a>

### K023 Kevesebb tagmondat

Szabály: A kettőnél több tagmondatból álló mondatot bontsd egyszerűbb mondatokra, vagy vond össze a tagmondatokat, ha ettől világosabb lesz.

Miért segít: Minden újabb tagmondat újabb viszonyt kér az olvasótól (ki, mi, mire vonatkozik). A többszörösen összetett mondatban ezek a viszonyok összecsúsznak.

Ellenőrző kérdés: A kettőnél több tagmondatú mondatokat megnézted, egyszerűbbé tehetők-e?

- Rossz: Felhívjuk figyelmét, hogy amennyiben a számlát, amelyet a szolgáltató a tárgyhónapot követő 5. napig állít ki, nem fizeti meg, a szolgáltató, akinek erre a szerződés jogot ad, felfüggesztheti a szolgáltatást.
- Jó: A szolgáltató minden hónap 5-ig állítja ki a számlát. Ha nem fizeti meg, a szolgáltató felfüggesztheti a szolgáltatást; ehhez a szerződés jogot ad neki.

Kivételek:

- Nem kell mindenáron egyszerű mondatra bontani: ha a bontás után az összetartozó elemek távol kerülnek egymástól, az összetett mondat a jobb.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: jelölt. Mérés (meres.py): mondathossz, huspacy.

Források: [Balogh 2023, 186–187. o.](forrasok.md#balogh-2023-014); [Gerencsér 2023, 13–14. o.](forrasok.md#gerencser-2023-005); [Horváth 2021, 110. o.](forrasok.md#horvath-2021-023); [NAV 2024b, 22. o.](forrasok.md#nav-ertheto-hivatal-2-036); [Világos Beszéd kézikönyv 2025, 25. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-065); [WP260 2018, 9. o.](forrasok.md#wp260-2018-005).

Ha a források eltérnek: A NAV a kettőnél több tagmondatú mondatot bontaná, a Világos Beszéd kézikönyve legfeljebb három tagmondatot enged egy mondatban. A skill döntése: A skill már a kettőnél több tagmondatú mondatot is jelöli, de csak megvizsgálandó jelöltként: a kivétel szerint az összetett mondat maradhat, ha a bontás rontana rajta. Ok: a jelölés csak figyelmeztet, a bontásról az író dönt a szöveg ismeretében. ([Világos Beszéd kézikönyv 2025, 25. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-065); [NAV 2024b, 22. o.](forrasok.md#nav-ertheto-hivatal-2-036))

<a id="k024"></a>

### K024 Nincs közbevetés és beágyazott hivatkozás a mondat közepén

Szabály: Ne szakítsa meg a mondatot zárójeles vagy gondolatjeles közbevetés, jogszabályi utalás vagy a szöveg más pontjára mutató hivatkozás.

Miért segít: A közbevetés kettévágja a mondatot: az olvasónak meg kell jegyeznie az első felét, amíg a betoldást olvassa. Az egymásba ágyazott zárójelek ezt többszörözik.

Ellenőrző kérdés: Egyetlen mondatot sem szakít meg zárójeles vagy gondolatjeles közbevetés vagy jogszabályi utalás?

- Rossz: Az érintett (a GDPR 4. cikk 1. pontja szerinti azonosított vagy azonosítható természetes személy (a továbbiakban: érintett)) kérheti adatai törlését.
- Jó: Kérheti, hogy töröljük az adatait. Érintett az, akinek a személyes adatait kezeljük (GDPR 4. cikk 1. pont).

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: jelölt. Mérés (meres.py): zarojelmelyseg.

Források: [Balogh 2023, 186–187. o.](forrasok.md#balogh-2023-014); [NAV 2024b, 22. o.](forrasok.md#nav-ertheto-hivatal-2-036); [Világos Beszéd kézikönyv 2025, 26. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-068); [Világos Beszéd 2025, 8. o.](forrasok.md#vilagos-beszed-kisokos-2025-028).

<a id="k025"></a>

### K025 A lényeg előre: a szórend jelentést és hangsúlyt hordoz

Szabály: Tedd előre a mondat lényeges részét; a magyarban a hangsúlyos elem az ige elé kerül, ezért figyeld, mit emel ki a választott szórend.

Miért segít: Ugyanazok a szavak más szórendben mást hangsúlyoznak, néha mást is jelentenek. A rossz szórend a lényeget a mondat végére dugja.

Ellenőrző kérdés: A mondatok lényeges része elöl áll, és a szórend azt emeli ki, amit ki akarsz emelni?

- Rossz: A szerződés megkötésétől számított 14 napon belül indoklás nélkül, a szolgáltatónak küldött nyilatkozattal elállhat.
- Jó: Elállhat a szerződéstől 14 napon belül, indoklás nélkül. Ehhez küldjön nyilatkozatot a szolgáltatónak.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: olvasva.

Források: [Európai Bizottság 2013, 7. o.](forrasok.md#eu-pontos-fogalmazas-2013-029); [Európai Bizottság 2013, 7. o.](forrasok.md#eu-pontos-fogalmazas-2013-030); [Horváth 2021, 106. o.](forrasok.md#horvath-2021-010); [Horváth 2021, 106. o.](forrasok.md#horvath-2021-011); [Horváth 2021, 109. o.](forrasok.md#horvath-2021-020); [NAV 2024a, 55. o.](forrasok.md#nav-ertheto-hivatal-1-033); [NAV 2024b, 21. o.](forrasok.md#nav-ertheto-hivatal-2-032); [Világos Beszéd kézikönyv 2025, 26. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-069); [Világos Beszéd kézikönyv 2025, 31. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-093).

<a id="k026"></a>

### K026 Állító mondat a tagadó helyett

Szabály: Amit lehet, állító mondatban fogalmazz meg; a tagadást akkor használd, ha a tagadás maga a közlés.

Miért segít: A tagadó mondat megértéséhez az olvasónak előbb el kell képzelnie az állítást, majd meg kell fordítania.

Ellenőrző kérdés: Ami állítóan is megfogalmazható, az állító mondatban áll?

- Rossz: Nem fogadható el a kérelem, ha nem tartalmazza az aláírást.
- Jó: A kérelmet aláírva fogadjuk el.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: jelölt. Mérés (meres.py): tagadas.

Források: [Európai Bizottság 2013, 7. o.](forrasok.md#eu-pontos-fogalmazas-2013-028); [NAV 2024b, 22–23. o.](forrasok.md#nav-ertheto-hivatal-2-038); [Világos Beszéd kézikönyv 2025, 37–38. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-119).

<a id="k027"></a>

### K027 Logikai kötőszavak, halmozás nélkül

Szabály: A mondatok és bekezdések kapcsolatát (ok, következmény, ellentét) mondd ki kötőszóval, de azonos értelmű kötőszót ne halmozz.

Miért segít: A kötőszó mutatja meg, hogyan függ össze két állítás. Ha hiányzik, az olvasónak kell kitalálnia; ha halmozódik („de viszont”), zavaró.

Ellenőrző kérdés: Kiderül a mondatok kapcsolata (ok, következmény, ellentét), és nincs halmozott kötőszó?

- Rossz: A határidő lejárt. Az ügyet lezártuk. De viszont kérheti az igazolást.
- Jó: A határidő lejárt, ezért az ügyet lezártuk. Igazolási kérelmet azonban beadhat.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: olvasva.

Források: [Európai Bizottság 2013, 6. o.](forrasok.md#eu-pontos-fogalmazas-2013-023); [NAV 2024b, 17. o.](forrasok.md#nav-ertheto-hivatal-2-023).

<a id="k028"></a>

### K028 Magyar mondatszerkezet idegen minták helyett

Szabály: Kerüld az idegen nyelvből átvett mondatszerkezeteket; a kiemelésre a magyar szórend és a hangsúly való.

Miért segít: A tükörfordított szerkezet idegenül hat, és lassítja az olvasást, mert az olvasó nem a megszokott magyar mintát kapja.

Ellenőrző kérdés: A mondatok magyar szerkezetűek, nincs bennük idegen mintára épült fordulat?

- Rossz: Ami az ügyben igazán fontos, az az, hogy a határidőt betartsa.
- Jó: Az ügyben a határidő betartása a legfontosabb.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: olvasva.

Források: [Európai Bizottság 2013, 7. o.](forrasok.md#eu-pontos-fogalmazas-2013-031); [NAV 2024b, 6. o.](forrasok.md#nav-ertheto-hivatal-2-005).

<a id="k082"></a>

### K082 A felsorolás elemei közötti kapcsolat egyértelmű

Szabály: Jogi szövegben a felsorolásnál mondd ki egyértelműen, hogy az elemek közül mindnek, egynek sem, pontosan egynek vagy legalább egynek kell teljesülnie.

Miért segít: A felsorolás végén álló „és” vagy „vagy” könnyen elsikkad, és a joghatás attól függ, melyik kapcsolat érvényes.

Ellenőrző kérdés: Jogi felsorolásnál kiderül, hogy az elemek közül mindnek, egynek vagy legalább egynek kell teljesülnie?

- Rossz: Jogosult az, aki
a) a településen lakik,
b) 65 évesnél idősebb,
c) egyedül él.
- Jó: Jogosult az, akire az alábbiak közül legalább kettő igaz:
a) a településen lakik,
b) 65 évesnél idősebb,
c) egyedül él.
- Megjegyzés a példához: A rossz példából nem derül ki, hogy mindhárom feltétel kell-e, vagy elég egy is.

Kör: csak jogi szövegnél. Alapértelmezett súlyosság: magas. Ellenőrzés: olvasva.

Források: [Jszr., 7. § (1)–(2)](forrasok.md#jszr-2009-005); [Világos Beszéd kézikönyv 2025, 26. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-071).
