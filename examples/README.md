# Előtte–utána példák

Négy kitalált szöveg és a skill átírása. A szövegek az evalok bemenetei (`evals/szovegek/`), az átírások az 1.4.0-s összehasonlító futásból valók (`evals/eredmenyek/iteracio-2/`). Kézzel nem javítottunk rajtuk. A szögletes zárójeles helyőrzők olyan adatot jelölnek, amely a bemenetben nincs meg; ezeket a kiadónak kell kitöltenie.

Mappánként a teljes változtatáslista, a hűségtáblázat és a mérés előtte–utána a `valtozasok.md` fájlban van.

## 1. Hatósági hiánypótlási felhívás

A kérés: „Írd át ezt a hiánypótlási felhívást úgy, hogy egy építtető magánszemély elsőre megértse.”

### Előtte

> Tárgy: Hiánypótlási felhívás
>
> Tisztelt Ügyfél!
>
> Tájékoztatjuk, hogy a 2026. március 2-án benyújtott, építési engedély iránti kérelme elbírálásra került, melynek során megállapításra került, hogy a kérelemhez a tervezői nyilatkozat csatolásra nem került.
>
> Fentiekre tekintettel felhívjuk, hogy a jelen felhívás kézhezvételétől számított 15 napon belül a hiányzó tervezői nyilatkozat benyújtására kerüljön sor, ellenkező esetben az eljárás a 2016. évi CL. törvény 47. § (1) bekezdés b) pontja alapján megszüntetésre kerül.
>
> A hiánypótlás az elektronikus ügyintézési felületen keresztül vagy postai úton teljesíthető.
>
> Kérjük tájékoztatásunk szíves tudomásulvételét.

### Utána

> Tárgy: Hiánypótlási felhívás: egy irat hiányzik az építési engedély iránti kérelméhez
>
> Tisztelt Ügyfél!
>
> Az építési engedély iránti kérelméhez még egy irat hiányzik: a tervezői nyilatkozat. Nyújtsa be a levél kézhezvételétől számított 15 napon belül.
>
> A 2026. március 2-án benyújtott kérelmét megvizsgáltuk. A kérelem mellett nem találtuk a tervezői nyilatkozatot. [Rövid magyarázat arról, mi a tervezői nyilatkozat: a kiadó töltse ki.]
>
> Ha nem nyújtja be határidőre, megszüntetjük az eljárást (2016. évi CL. törvény 47. § (1) bekezdés b) pontja).
>
> Így nyújthatja be a nyilatkozatot:
>
> - az elektronikus ügyintézési felületen, vagy
> - postán: [postacím: a kiadó töltse ki].
>
> Kérdés esetén forduljon hozzánk: [ügyintéző neve, telefonszám, ügyszám: a kiadó töltse ki].
>
> Üdvözlettel:
> [a hatóság neve]

### Mi változott?

- A teendő (a tervezői nyilatkozat benyújtása) és a 15 napos határidő az első két mondatba került; eredetileg a 4. mondat végén állt (K002, K003).
- A leghosszabb mondat 37 szóról 19-re rövidült (K020, K023).
- Az öt „kerül”-szerkezet helyett cselekvő ige áll: „megvizsgáltuk”, „nyújtsa be”, „megszüntetjük” (K043).
- A jogszabályhely a mondat végére, zárójelbe került (K012); a két benyújtási mód felsorolás lett (K013).
- A „Kérjük tájékoztatásunk szíves tudomásulvételét” formula kimaradt (K050).
- A postacím, a kapcsolattartó és a tervezői nyilatkozat magyarázata nincs a bemenetben, ezért helyőrző jelöli őket.
- Jogászi ellenőrzést kér: az „elbírálásra került” helyett írt „megvizsgáltuk”.

Hűségtáblázat és mérés: [hianypotlasi-felhivas/valtozasok.md](hianypotlasi-felhivas/valtozasok.md).

## 2. Webshop adatkezelési tájékoztatója

A kérés: „Írd át közérthetőre ezt az adatkezelési tájékoztató részletet egy webshop vásárlóinak.”

### Előtte

> ## Az adatkezelés célja és jogalapja
>
> Az Adatkezelő az érintett (a továbbiakban: Érintett) személyes adatait (így különösen nevét, e-mail-címét, telefonszámát (amennyiben azt az Érintett megadja (önkéntes adatszolgáltatás))) a szolgáltatás nyújtása, a szolgáltatások fejlesztése, valamint egyéb, az Adatkezelő jogos érdekén alapuló célokból (GDPR 6. cikk (1) bekezdés b) és f) pontja) kezeli, illetve az Érintett hozzájárulása esetén (GDPR 6. cikk (1) bekezdés a) pontja) marketing célú megkeresések küldésére is felhasználhatja.
>
> Az adatok a szerződés megszűnését követő 5 évig kerülnek megőrzésre, ezt követően törlésre kerülnek, kivéve, ha jogszabály ennél hosszabb megőrzési időt ír elő.

### Utána

> ## Milyen adatait kezeljük, és mire használjuk?
>
> Ebben a tájékoztatóban „mi” a [az adatkezelő neve: a webshop tölti ki], „Ön” pedig az, akinek az adatait kezeljük (a jogszabály szerint: érintett).
>
> Kezeljük az Ön személyes adatait, különösen a nevét, az e-mail-címét és a telefonszámát. A telefonszámát csak akkor kezeljük, ha Ön megadja. Megadása nem kötelező.
>
> Az adatait ezekre használjuk:
>
> - a szolgáltatás nyújtására [konkrétan: mit jelent ez a webshopnál; a webshop tölti ki];
> - a szolgáltatásaink fejlesztésére [konkrétan: milyen adatot, hogyan; a webshop tölti ki];
> - egyéb célokra, amelyek a mi jogos érdekünkön alapulnak [konkrétan: mely célokra; a webshop tölti ki].
>
> Ennek jogalapja a szerződés teljesítése és a mi jogos érdekünk (GDPR 6. cikk (1) bekezdés b) és f) pont). Jogos érdek az olyan saját érdekünk, amely miatt kezeljük az adatait, ha az Ön érdekei és jogai nem előbbre valók.
>
> ## Mikor kaphat tőlünk marketing célú megkeresést?
>
> Ha Ön hozzájárul, marketing célú megkereséseket is küldhetünk Önnek. Ennek jogalapja az Ön hozzájárulása (GDPR 6. cikk (1) bekezdés a) pont).
>
> ## Meddig őrizzük az adatait?
>
> A szerződés megszűnése után 5 évig őrizzük az adatait, utána töröljük őket. Ha jogszabály ennél hosszabb megőrzési időt ír elő, akkor addig őrizzük őket.

### Mi változott?

- Két hosszú bekezdés helyett három rövid szakasz, kérdés formájú alcímmel (K002, K010); a három adatkezelési cél felsorolás lett (K013).
- A 63 szavas, négyszintű zárójeles mondat rövid mondatokra bomlott; az átlagos mondathossz 43 szóról 12,4-re csökkent (K020, K024).
- „Adatkezelő” és „Érintett” helyett „mi” és „Ön” (K044, K048).
- A GDPR-hivatkozások a mondat végére kerültek, a jogalapot szavakkal is megmondja (K012, K030).
- A „szolgáltatás nyújtása” és az „egyéb jogos érdekű cél” túl általános; konkrétumot nem talált ki, helyőrzőt tett (K079).
- A szöveg hosszabb lett (91 szóról 196-ra), mert alcímek, felsorolás és magyarázat került bele.
- Három pontot jogásznak kell átnéznie; ezeket a válasz külön felsorolja.

Hűségtáblázat és mérés: [adatkezelesi-tajekoztato/valtozasok.md](adatkezelesi-tajekoztato/valtozasok.md).

## 3. Önkormányzati támogatási tájékoztató, rövidítési kéréssel

A kérés: „Ez a tájékoztató túl hosszú. Rövidítsd le a felére, a lényeg maradjon meg, a részletek nem érdekesek.”

### Előtte

> Tárgy: Tájékoztatás a lakásfelújítási támogatás igénybevételének feltételeiről
>
> Tisztelt Lakos!
>
> Tájékoztatjuk, hogy a kerületi lakásfelújítási támogatás iránti kérelem benyújtására 2026. május 31-ig van lehetőség, amennyiben a kérelmező a kerületben legalább két éve bejelentett lakóhellyel rendelkezik, kivéve, ha a kérelmező a kerületi önkormányzat bérlakásában lakik, mert ebben az esetben a támogatás nem igényelhető. A támogatás összege a felújítási költség 50 százaléka, de legfeljebb 800 000 forint, azzal, hogy a 70. életévüket betöltött kérelmezők esetében a támogatás mértéke a költség 70 százaléka, legfeljebb 1 000 000 forint. A kérelemhez csatolni szükséges a kivitelező árajánlatát, továbbá társasházi lakás esetén a közös képviselő hozzájáruló nyilatkozatát, kivéve, ha a felújítás kizárólag a lakás belső terét érinti.
>
> A kérelem hiányos benyújtása esetén hiánypótlásra egy alkalommal kerül sor, a hiánypótlás elmulasztása a kérelem elutasítását vonja maga után.
>
> Tisztelettel:
> Polgármesteri Hivatal, Szociális Iroda

### Utána

> Tárgy: A lakásfelújítási támogatás feltételei
>
> Tisztelt Lakos!
>
> A kerületi lakásfelújítási támogatást 2026. május 31-ig kérheti.
>
> Kérheti, ha legalább két éve a kerületben van a bejelentett lakóhelye. Ha az önkormányzat bérlakásában lakik, nem igényelheti.
>
> A támogatás a felújítási költség 50 százaléka, legfeljebb 800 000 forint. Ha Ön betöltötte a 70. életévét, a költség 70 százaléka, legfeljebb 1 000 000 forint.
>
> Csatolja a kérelemhez a kivitelező árajánlatát. Ha társasházi lakást újít fel, a közös képviselő hozzájáruló nyilatkozatát is csatolja. Erre nincs szükség, ha a felújítás csak a lakás belső terét érinti.
>
> Ha a kérelem hiányos, egyszer pótolhatja a hiányokat. Ha nem pótolja, elutasítjuk a kérelmet.
>
> Tisztelettel:
> Polgármesteri Hivatal, Szociális Iroda

### Mi változott?

- A skill nem a felére rövidített: 134 szóról 108-ra. Megmondta, hogy a feltételek, a kivételek és az összegek a lényeghez tartoznak, ezért nem hagyhatók el (K004, K077).
- A fő üzenet (a támogatás kérhető, határidő: 2026. május 31.) az első mondat lett (K002).
- A 42 szavas mondat helyett a leghosszabb 15 szó (K020, K023).
- A feltétel a mondat elejére került: „Ha társasházi lakást újít fel, …” (K022).
- Két kétértelmű helyet szakmai jóváhagyásra jelölt: kire vonatkozik a bérlakásos kivétel, és ki kezdeményezi a hiánypótlást (K082).

Hűségtáblázat és mérés: [tamogatasi-tajekoztato/valtozasok.md](tamogatasi-tajekoztato/valtozasok.md).

## 4. Ptk.-szakasz, átírási kéréssel

A kérés: „Írd át ezt közérthetőbbre, hogy az ügyfeleink is megértsék.”

### Előtte

> 2013. évi V. törvény a Polgári Törvénykönyvről
>
> 6:102. § [Tisztességtelen általános szerződési feltétel]
>
> (1) Tisztességtelen az az általános szerződési feltétel, amely a szerződésből eredő jogokat és kötelezettségeket a jóhiszeműség és tisztesség követelményének megsértésével egyoldalúan és indokolatlanul a szerződési feltétel alkalmazójával szerződő fél hátrányára állapítja meg.
>
> (2) Az általános szerződési feltétel tisztességtelen voltának megállapításakor vizsgálni kell a szerződéskötéskor fennálló minden olyan körülményt, amely a szerződés megkötésére vezetett, a kikötött szolgáltatás rendeltetését, továbbá az érintett feltételnek a szerződés más feltételeivel vagy más szerződésekkel való kapcsolatát.

### Utána

> # Mikor tisztességtelen egy általános szerződési feltétel?
>
> *Rövid magyarázat a Polgári Törvénykönyv 6:102. §-ához. A magyarázat nem helyettesíti a törvény szövegét; a törvény szövege a döntő.*
>
> ## Mikor tisztességtelen a feltétel?
>
> Tisztességtelen az a feltétel, amely a szerződésből eredő jogokat és kötelezettségeket
> - a jóhiszeműség és a tisztesség követelményének megsértésével,
> - egyoldalúan és indokolatlanul,
> - a feltételt alkalmazó féllel szerződő fél hátrányára állapítja meg.
>
> (Ptk. 6:102. § (1))
>
> ## Mit kell megvizsgálni?
>
> Annak megállapításakor, hogy a feltétel tisztességtelen-e, meg kell vizsgálni:
> - minden olyan körülményt, amely a szerződés megkötésekor fennállt, és a szerződés megkötésére vezetett;
> - a kikötött szolgáltatás rendeltetését;
> - azt, hogy az adott feltétel hogyan kapcsolódik a szerződés más feltételeihez vagy más szerződésekhez.
>
> (Ptk. 6:102. § (2))

### Mi változott?

- A skill a törvényszöveget nem írta át, mert kötelező normaszöveg: annak a forrással kell egyeznie.
- Helyette külön magyarázatot írt, amely az elején kimondja, hogy nem helyettesíti a törvényt.
- A magyarázatban a feltételek felsorolásba kerültek (K013), a címek kérdések lettek (K010), a mondatok átlagosan 7,2 szavasak az eredeti 21 helyett.
- Jogi kifejezést nem cserélt le; a szerkezetet alakította át.

Hűségtáblázat és mérés: [torvenyszoveg-magyarazattal/valtozasok.md](torvenyszoveg-magyarazattal/valtozasok.md).
