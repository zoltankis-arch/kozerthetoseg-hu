<!-- GENERÁLT FÁJL. Ne szerkeszd kézzel: a forrása az assets/adatok/ mappa TOML-fájljai. Újragenerálás: python scripts/generalas.py -->

# Szabályok: Szó

Az összes csoport: [szabaly-index.md](szabaly-index.md).

<a id="k029"></a>

### K029 Az olvasó szavai

Szabály: Azt a szót használd, amelyet az olvasó maga is használna; a mesterkélt szakszó helyett a bevett köznyelvi szót.

Miért segít: A nem bennfentes olvasó a szakszó mögötti fogalomrendszert nem ismeri, ezért a mesterkélt szó megakasztja. A bevett köznyelvi szót elsőre érti.

Ellenőrző kérdés: Azokat a szavakat használja a szöveg, amelyeket az olvasó maga is használna?

- Rossz: A behajtásra jogosító dokumentum a gépjármű szélvédője mögött jól látható módon elhelyezendő.
- Jó: A behajtási engedélyt tegye ki a szélvédő mögé, jól láthatóan.

Kivételek:

- Ahol a szakszó jogi következményt hordoz, és a köznyelvi szó mást jelent, a szakszó marad, magyarázattal (lásd K030, K031).

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: jelölt. Mérés (meres.py): hosszu_szavak.

Források: [Horváth 2021, 103. o.](forrasok.md#horvath-2021-002); [Horváth 2021, 104. o.](forrasok.md#horvath-2021-003); [Világos Beszéd kézikönyv 2025, 23. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-052); [Világos Beszéd kézikönyv 2025, 31. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-090); [Világos Beszéd kézikönyv 2025, 32–33. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-098); [Világos Beszéd kézikönyv 2025, 37–38. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-113); [Világos Beszéd 2025, 8. o.](forrasok.md#vilagos-beszed-kisokos-2025-022); [Világos Beszéd 2025, 8. o.](forrasok.md#vilagos-beszed-kisokos-2025-023).

<a id="k030"></a>

### K030 Szakszó csak magyarázattal

Szabály: Ha szakszót kell használnod, magyarázd meg az első előfordulásánál, vagy adj szószedetet; a túlzottan jogi, műszaki vagy szakmai szóhasználatot kerüld.

Miért segít: A szakszó sokszor nem cserélhető le (jogi következménye van), de az olvasó csak akkor tud vele mit kezdeni, ha tudja, mit jelent.

Ellenőrző kérdés: Minden szakszó meg van magyarázva az első előfordulásnál?

- Rossz: Az ingatlanra jelzálogjog került bejegyzésre.
- Jó: Az ingatlanra jelzálogjogot jegyeztek be. Ez azt jelenti, hogy ha a tartozást nem fizetik meg, a hitelező az ingatlan eladásából kaphatja meg a pénzét.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: olvasva.

Források: [Európai Bizottság 2013, 5. o.](forrasok.md#eu-pontos-fogalmazas-2013-014); [Európai Bizottság 2013, 12. o.](forrasok.md#eu-pontos-fogalmazas-2013-045); [Európai Bizottság 2013, 12. o.](forrasok.md#eu-pontos-fogalmazas-2013-046); [Gerencsér 2023, 13–14. o.](forrasok.md#gerencser-2023-004); [NAV 2024a, 55. o.](forrasok.md#nav-ertheto-hivatal-1-034); [NAV 2024b, 41. o.](forrasok.md#nav-ertheto-hivatal-2-060); [Világos Beszéd kézikönyv 2025, 23. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-053); [Világos Beszéd kézikönyv 2025, 23. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-054); [Világos Beszéd kézikönyv 2025, 31. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-090); [Világos Beszéd kézikönyv 2025, 32–33. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-098); [Világos Beszéd kézikönyv 2025, 39. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-124); [Világos Beszéd 2025, 8. o.](forrasok.md#vilagos-beszed-kisokos-2025-022); [WP260 2018, 10. o.](forrasok.md#wp260-2018-013).

<a id="k031"></a>

### K031 Szakszó, ha a köznyelvi szó félrevezet

Szabály: Ha egy köznyelvi szót szaknyelvi jelentésben használnál, és az olvasó a köznyelvi jelentését érti, válassz egyszerű szakszót vagy körülírást.

Miért segít: A köznyelvi szó ismerősnek tűnik, ezért az olvasó nem kérdez vissza, hanem félreérti. Ez rosszabb, mint az ismeretlen szó.

Ellenőrző kérdés: Nincs olyan köznyelvi szó, amelyet az olvasó más jelentésben értene, mint ahogy a szöveg használja?

- Rossz: A biztosító szolgáltatási kötelezettsége nem áll be, ha a kárt szándékosan okozták.
- Jó: A biztosító nem fizet, ha a kárt szándékosan okozták.

Kör: általános. Alapértelmezett súlyosság: magas. Ellenőrzés: olvasva.

Források: [Horváth 2021, 104. o.](forrasok.md#horvath-2021-005).

<a id="k032"></a>

### K032 Az ismertebb szó, akár idegen, akár magyar

Szabály: Az olvasó által ismertebb szót válaszd: a meg nem honosodott idegen szó helyett a magyart, a ritka vagy régies magyar szó helyett az ismert idegent; vigyázz a hamis barátokra.

Miért segít: Az érthetőséget nem a szó eredete dönti el, hanem az, hogy az olvasó ismeri-e. A hamis barát (például az angol actual mintájára használt aktuális) félrevezet.

Ellenőrző kérdés: Mindenhol az olvasó által ismertebb szó áll, és nincs hamis barát?

- Rossz: A helpdesk a ticket lezárásáról e-mailben küld visszaigazolást.
- Jó: Az ügyfélszolgálat e-mailben értesíti, ha lezárta a bejelentését.

Kivételek:

- Szakmai olvasónak, aki maga is az idegen szót használja, az idegen szó maradhat.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: jelölt. Mérés (meres.py): hosszu_szavak.

Források: [Európai Bizottság 2013, 11. o.](forrasok.md#eu-pontos-fogalmazas-2013-044); [Horváth 2021, 105. o.](forrasok.md#horvath-2021-006); [Horváth 2021, 105. o.](forrasok.md#horvath-2021-007); [Horváth 2021, 105. o.](forrasok.md#horvath-2021-008); [NAV 2024b, 41. o.](forrasok.md#nav-ertheto-hivatal-2-060); [Világos Beszéd kézikönyv 2025, 23. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-056); [Világos Beszéd kézikönyv 2025, 37–38. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-113).

<a id="k033"></a>

### K033 Egy fogalom, egy szó végig

Szabály: Ugyanazt a fogalmat a szöveg minden pontján ugyanazzal a szóval nevezd meg; stílusból ne cserélgesd szinonimákra.

Miért segít: Ha a szöveg váltogatja a szót (kérelem, beadvány, folyamodvány), az olvasó joggal hiszi, hogy több különböző dologról van szó.

Ellenőrző kérdés: Ugyanazt a fogalmat végig ugyanaz a szó jelöli?

- Rossz: A kérelmet 30 napon belül bíráljuk el. A beadvány elbírálásáról levélben értesítjük. A folyamodványhoz csatolt iratokat visszaküldjük.
- Jó: A kérelmet 30 napon belül bíráljuk el. A döntésről levélben értesítjük. A kérelemhez csatolt iratokat visszaküldjük.

Kivételek:

- A szóismétlés itt nem hiba. Ami kerülendő, az a felesleges önismétlés: ugyanaz a hosszú név vagy körülírás újra és újra (lásd K035, K040).

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: olvasva.

Források: [Balogh 2023, 187. o.](forrasok.md#balogh-2023-015); [Európai Bizottság 2013, 6. o.](forrasok.md#eu-pontos-fogalmazas-2013-021); [Európai Bizottság 2013, 7. o.](forrasok.md#eu-pontos-fogalmazas-2013-027); [Horváth 2021, 107. o.](forrasok.md#horvath-2021-016); [Jszr., 4. § (1)–(2)](forrasok.md#jszr-2009-003); [NAV 2024b, 41. o.](forrasok.md#nav-ertheto-hivatal-2-061); [Világos Beszéd kézikönyv 2025, 23. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-057).

Ha a források eltérnek: A NAV példatára szerint ne féljünk a szóismétléstől; az uniós útmutató az önismétlés kerülését kéri. A skill döntése: A kettő nem ütközik: a fogalom megnevezése ismétlődhet és ismétlődjön is, a hosszú név vagy a már elmondott tartalom ismételgetése viszont felesleges. A skill a terminust nem cseréli szinonimára, a felesleges ismétlést kihúzza. ([NAV 2024b, 41. o.](forrasok.md#nav-ertheto-hivatal-2-061); [Európai Bizottság 2013, 6. o.](forrasok.md#eu-pontos-fogalmazas-2013-021))

<a id="k034"></a>

### K034 Egy szó, egy jelentés

Szabály: Egy szót a szövegen belül csak egy jelentésben használj; ha két dologra ugyanaz a szó illik, az egyiket nevezd meg másképp.

Miért segít: Ha ugyanaz a szó két dologra vonatkozik (például a kérelemre és a határidő-módosítási kérelemre), az olvasó nem tudja, melyikről szól a következő mondat.

Ellenőrző kérdés: Minden szó egyetlen jelentésben szerepel a szövegben?

- Rossz: A kérelmét keddig adhatja be. A határidő módosítását is kérelmezheti. A kérelmet a hivatalban adja le.
- Jó: A támogatási kérelmét keddig adhatja be. Ha ez nem sikerül, kérhet határidő-hosszabbítást. A támogatási kérelmet a hivatalban adja le.

Kivételek:

- Ezt a mérőszkript nem tudja mérni: a két jelentést csak olvasva lehet észrevenni.

Kör: általános. Alapértelmezett súlyosság: magas. Ellenőrzés: olvasva.

Források: [Európai Bizottság 2013, 7. o.](forrasok.md#eu-pontos-fogalmazas-2013-026); [Világos Beszéd kézikönyv 2025, 23. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-057); [WP260 2018, 9. o.](forrasok.md#wp260-2018-006).

<a id="k035"></a>

### K035 Felesleges szavak és magától értetődő közlések nélkül

Szabály: Hagyd el a jelentés nélküli fordulatokat, a felesleges jelzőket, a tautológiát és azt, ami a helyzetből úgyis egyértelmű.

Miért segít: A felesleges szó hosszabbá teszi az utat a lényegig, és elrejti azt, ami valóban új. A „Tájékoztatjuk, hogy” után az olvasó még mindig nem tudja, miről van szó.

Ellenőrző kérdés: Kimaradtak a jelentés nélküli fordulatok, a felesleges jelzők és a magától értetődő közlések?

- Rossz: Tájékoztatjuk, hogy a jelen levelünkben foglaltak szerint a benyújtott kérelmét a hivatalos honlapunkon közzétett feltételek alapján megvizsgáltuk.
- Jó: Megvizsgáltuk a kérelmét a honlapunkon közzétett feltételek szerint.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: jelölt. Mérés (meres.py): hivatali_fordulatok.

Források: [Európai Bizottság 2013, 5. o.](forrasok.md#eu-pontos-fogalmazas-2013-017); [Európai Bizottság 2013, 6. o.](forrasok.md#eu-pontos-fogalmazas-2013-019); [Európai Bizottság 2013, 6. o.](forrasok.md#eu-pontos-fogalmazas-2013-020); [Európai Bizottság 2013, 6. o.](forrasok.md#eu-pontos-fogalmazas-2013-021); [Gerencsér 2023, 13–14. o.](forrasok.md#gerencser-2023-005); [Horváth 2021, 106. o.](forrasok.md#horvath-2021-012); [Horváth 2021, 107. o.](forrasok.md#horvath-2021-013); [Horváth 2021, 107. o.](forrasok.md#horvath-2021-014); [Horváth 2021, 107. o.](forrasok.md#horvath-2021-015); [Horváth 2021, 108. o.](forrasok.md#horvath-2021-017); [Horváth 2021, 108. o.](forrasok.md#horvath-2021-018); [NAV 2024b, 36. o.](forrasok.md#nav-ertheto-hivatal-2-055); [NAV 2024b, 36–37. o.](forrasok.md#nav-ertheto-hivatal-2-056); [NAV 2024b, 41. o.](forrasok.md#nav-ertheto-hivatal-2-064); [Világos Beszéd kézikönyv 2025, 26. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-074); [Világos Beszéd kézikönyv 2025, 27. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-075); [Világos Beszéd kézikönyv 2025, 27. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-076); [Világos Beszéd kézikönyv 2025, 31. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-094); [Világos Beszéd kézikönyv 2025, 32–33. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-098); [Világos Beszéd kézikönyv 2025, 37–38. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-116); [Világos Beszéd 2025, 9. o.](forrasok.md#vilagos-beszed-kisokos-2025-029).

<a id="k036"></a>

### K036 Egyszerűbb szó a körülményes helyett

Szabály: A körülményes kötőszó vagy szerkezet helyett használd az egyszerűbbet: „amennyiben” helyett „ha”, „tekintettel arra, hogy” helyett „mivel”.

Miért segít: Az egyszerű szó ugyanazt jelenti, csak gyorsabban olvasható; a szakszerűségből semmit nem vesz el.

Ellenőrző kérdés: A körülményes kötőszók és szerkezetek helyén az egyszerűbb áll („ha”, „mivel”)?

- Rossz: Amennyiben a díjat nem fizeti meg, tekintettel arra, hogy a szerződés ezt lehetővé teszi, a szolgáltatást felfüggesztjük.
- Jó: Ha nem fizeti meg a díjat, felfüggesztjük a szolgáltatást. Ezt a szerződés lehetővé teszi.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: jelölt. Mérés (meres.py): hivatali_fordulatok.

Források: [Európai Bizottság 2013, 6. o.](forrasok.md#eu-pontos-fogalmazas-2013-024); [Európai Bizottság 2013, 6. o.](forrasok.md#eu-pontos-fogalmazas-2013-025); [NAV 2024b, 41. o.](forrasok.md#nav-ertheto-hivatal-2-063); [Világos Beszéd kézikönyv 2025, 23. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-055); [Világos Beszéd kézikönyv 2025, 37–38. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-112); [Világos Beszéd kézikönyv 2025, 38. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-117); [Világos Beszéd 2025, 9. o.](forrasok.md#vilagos-beszed-kisokos-2025-030).

<a id="k037"></a>

### K037 Felesleges igekötő nélkül

Szabály: Ha az ige igekötő nélkül is teljes jelentésű, hagyd el az igekötőt (leellenőriz helyett ellenőriz).

Miért segít: A felesleges igekötő szószaporítás, és hivatali ízt ad a szövegnek.

Ellenőrző kérdés: Nincs felesleges igekötő?

- Rossz: Leellenőriztük és beazonosítottuk a befizetést.
- Jó: Ellenőriztük és azonosítottuk a befizetést.

Kör: általános. Alapértelmezett súlyosság: alacsony. Ellenőrzés: gépi. Keresőminta: leellenőriz, kihangsúlyoz és hasonló felesleges igekötős alak.

Források: [Európai Bizottság 2013, 8. o.](forrasok.md#eu-pontos-fogalmazas-2013-034); [Európai Bizottság 2013, 10. o.](forrasok.md#eu-pontos-fogalmazas-2013-041); [NAV 2024b, 38. o.](forrasok.md#nav-ertheto-hivatal-2-057).

<a id="k038"></a>

### K038 Névutó helyett rag

Szabály: Ahol rag is elég, ne használj névutót vagy hosszabb szerkezetet (a hivatal felé helyett a hivatalnak, e-mail útján helyett e-mailben).

Miért segít: A rag rövidebb, és ugyanazt jelenti; a névutók halmozása elnehezíti a mondatot.

Ellenőrző kérdés: Ahol rag is elég, ott nincs névutó vagy hosszabb szerkezet?

- Rossz: A beadvány benyújtása során e-mail útján küldje meg a hivatal felé a meghatalmazást.
- Jó: Amikor beadja a kérelmet, e-mailben küldje el nekünk a meghatalmazást.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: jelölt.

Források: [Európai Bizottság 2013, 10. o.](forrasok.md#eu-pontos-fogalmazas-2013-040); [NAV 2024b, 38–39. o.](forrasok.md#nav-ertheto-hivatal-2-058); [Világos Beszéd kézikönyv 2025, 27. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-075); [Világos Beszéd kézikönyv 2025, 37–38. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-116).

<a id="k039"></a>

### K039 Lehetőség: „lehet” vagy -hat/-het a „lehetőség van” helyett

Szabály: Ha az olvasó lehetőségét írod le, a „lehetőség van valamire” helyett használd a „lehet” vagy a -hat/-het alakot.

Miért segít: A rövidebb forma a lényegi elemeket közel hozza egymáshoz, és megmondja, ki teheti meg.

Ellenőrző kérdés: A lehetőséget „lehet” vagy -hat/-het fejezi ki, nem „lehetőség van”?

- Rossz: Lehetőség van a kérelem elektronikus úton történő benyújtására.
- Jó: A kérelmet elektronikusan is beadhatja.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: gépi.

Források: [NAV 2024b, 40. o.](forrasok.md#nav-ertheto-hivatal-2-059); [WP260 2018, 10. o.](forrasok.md#wp260-2018-010).

Ha a források eltérnek: A NAV példatára a -hat/-het képzőt ajánlja a lehetőség kifejezésére; a WP260 iránymutatás szerint az adatkezelési tájékoztatóban kerülni kell a ható igéket, mert nem derül ki belőlük, mi történik ténylegesen. A skill döntése: A skill a két esetet szétválasztja. Ha az olvasó lehetőségéről van szó (beadhatja, kérheti), a -hat/-het a jó. Ha azt írja le, mit tesz a szöveg kiadója (adatkezelés, díjemelés), kijelentő módot kér: nem „felhasználhatjuk”, hanem „felhasználjuk, erre a célra” (lásd K080). ([NAV 2024b, 40. o.](forrasok.md#nav-ertheto-hivatal-2-059); [WP260 2018, 10. o.](forrasok.md#wp260-2018-010))

<a id="k040"></a>

### K040 Rövidítés és rövid megjelölés

Szabály: A ritkán előforduló kifejezést írd ki; a gyakran ismétlődő hosszú nevet az első előfordulásnál írd ki, zárójelben add meg a rövidítését vagy rövid megjelölését, és utána végig azt használd.

Miért segít: Az ismeretlen rövidítés megállítja az olvasót, a hosszú név ismételgetése pedig elnehezíti a szöveget. Az első előfordulásnál bevezetett rövidítés mindkettőt megoldja.

Ellenőrző kérdés: A rövidítések az első előfordulásnál ki vannak írva, és utána végig ugyanaz a rövid alak áll?

- Rossz: A KKEP keretében nyújtott támogatás feltételeit a KKEP-ÚT tartalmazza. (Mindkét rövidítés feloldás nélkül.)
- Jó: A Kis- és Középvállalkozói Energiaprogram (a továbbiakban: energiaprogram) feltételeit az útmutató tartalmazza. Az energiaprogramba március 31-ig lehet jelentkezni.

Kivételek:

- Ugyanaz a rövidítés más szövegkörnyezetben mást jelenthet; ha kétértelmű, írd ki.
- Könnyen érthető kommunikációban (KÉK) rövidítést nem használunk.

Kör: általános. Alapértelmezett súlyosság: alacsony. Ellenőrzés: olvasva.

Források: [Európai Bizottság 2013, 6. o.](forrasok.md#eu-pontos-fogalmazas-2013-021); [Európai Bizottság 2013, 13. o.](forrasok.md#eu-pontos-fogalmazas-2013-047); [Európai Bizottság 2013, 13. o.](forrasok.md#eu-pontos-fogalmazas-2013-048); [Jszr., 5. §](forrasok.md#jszr-2009-004); [NAV 2024b, 23. o.](forrasok.md#nav-ertheto-hivatal-2-042); [NAV 2024b, 41. o.](forrasok.md#nav-ertheto-hivatal-2-062); [Világos Beszéd kézikönyv 2025, 23. o.](forrasok.md#vilagos-beszed-kezikonyv-2025-056).

<a id="k041"></a>

### K041 Konkrét szó az elvont és a divatszó helyett

Szabály: Az elvont, homályos vagy divatos kifejezés helyett válaszd a konkrétabbat, amely megmondja, pontosan miről van szó.

Miért segít: Az elvont szóból az olvasó nem tudja meg, mi történik vele. A konkrét szó pontosabb, és ellenőrizhető állítást tesz.

Ellenőrző kérdés: Az elvont és divatos kifejezések helyén konkrét szó áll?

- Rossz: Negatív tendencia figyelhető meg a foglalkoztatási lehetőségek terén.
- Jó: Kevesebb az álláshely.

Kör: általános. Alapértelmezett súlyosság: közepes. Ellenőrzés: olvasva.

Források: [Európai Bizottság 2013, 9. o.](forrasok.md#eu-pontos-fogalmazas-2013-035); [Európai Bizottság 2013, 9. o.](forrasok.md#eu-pontos-fogalmazas-2013-036); [Európai Bizottság 2013, 9. o.](forrasok.md#eu-pontos-fogalmazas-2013-037); [WP260 2018, 9. o.](forrasok.md#wp260-2018-006).

<a id="k080"></a>

### K080 Határozatlan kifejezés és ható ige nélkül a kiadó tevékenységéről

Szabály: Ha azt írod le, mit tesz a szöveg kiadója (például hogyan kezeli az adatokat), kerüld a ható igét és a határozatlan szavakat (néhány, gyakran, lehetséges); ha mégis kell, indokold.

Miért segít: A „felhasználhatjuk” vagy a „néhány esetben” után az olvasó nem tudja, mi történik ténylegesen, így nem tud dönteni.

Ellenőrző kérdés: A kiadó saját tevékenységéről szóló részekben nincs indokolatlan ható ige és határozatlan szó?

- Rossz: Adatait esetenként harmadik félnek is átadhatjuk.
- Jó: A szállítási címét átadjuk a futárszolgálatnak, hogy kézbesítse a csomagot. Más harmadik félnek nem adjuk át.

Kör: csak jogi szövegnél. Alapértelmezett súlyosság: közepes. Ellenőrzés: jelölt. Keresőminta: ható ige a kiadó tevékenységéről (jelölt).

Források: [WP260 2018, 10. o.](forrasok.md#wp260-2018-010).
