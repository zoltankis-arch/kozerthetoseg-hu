# Parancs: `atiras`

Közérthetőre írja át a szöveget, majd hűségellenőrzést végez: megnézi, hogy minden tény, szám, határidő, feltétel, kivétel, modalitás és jogi kifejezés megmaradt-e.

## Mikor kell

Ha a hívó átírást, egyszerűsítést, közérthetőbb változatot kér egy magyar szövegből. Ha csak véleményt kér, az `audit` fut.

Kötelező szöveget (jogszabály, előírt formula, jogszabályban megállapított feltétel, kamarai egységes szöveg) a parancs nem ír át: kimondja, hogy kötelező, és hogy a forrásával kell egyeznie. A köré írt tájékoztatót átírhatja, vagy rövid magyarázatot írhat mellé.

## Bemenet

- Az átírandó szöveg.
- Olvasó és cél; ha hiányzik, egy kérdésben kérdezz rá.
- Elhagyható: megszólítás (alapértelmezés a magázás, ha a szöveg nem dönt), terjedelmi korlát, kötelezően megtartandó elemek listája.

## Lépések

1. Végezd el az audit 1–4. lépését (olvasó és cél, szövegtípus, KÉK-határ, a négy kérdés). Kötelező szövegnél itt állj meg, és csak a jelzést add.
2. Leltár az átírás előtt: gyűjtsd ki a szövegből az összes tényt, számot, összeget, dátumot és határidőt, feltételt, kivételt, jogkövetkezményt, jogszabályhelyet, jogi kifejezést és modalitást. Ez a hűségellenőrzés alapja.

   <a id="modalitas"></a>Modalitás: minden olyan elem, amely megmondja, kötelező, lehetséges, megengedett vagy tilos-e valami: „kell”, „köteles”, „jogosult”, „-hat/-het”, „lehet”, „tilos”, „nem kötelező”, „kérjük”. Ezeket elemenként vedd fel a leltárba, mert a közérthetőbb igei alak gyakran észrevétlenül megváltoztatja őket („felhasználhatja” → „felhasználja”: a lehetőségből tény lesz; „köteles megfizetni” → „fizesse meg”: a kötelezettség marad, de a jogi minősítés eltűnik). Ha a modalitás megváltozik, az átírás hibás, akkor is, ha olvashatóbb; ha szándékos, indokold, és jogi szövegnél jelöld jogászi ellenőrzésre.
3. Átírás a [szabaly-index.md](szabaly-index.md), a vonatkozó csoportfájlok és a [szotar.md](szotar.md) szerint (a szótár „Mikor ne cseréld” oszlopát is nézd), ebben a sorrendben: tartalom és felépítés (fő üzenet, teendő, sorrend, alcímek), mondatok, szavak és szerkezetek, végül forma. Jogi szövegnél a [szovegtipusok.md](szovegtipusok.md#szocsere) szerint a szerkezeti átírás az elsődleges; jogi kifejezést csak magyarázattal együtt cserélj, ha egyáltalán. Ha a szöveg nem jogi és nem kötelező, a jogi hangzású szót (például „jogosult”, „kötelezett”) cseréld köznyelvire, ha a szöveg nem a jogi jelentésében használja (K031), és a cserét sorold a fő változtatások közé.
4. <a id="olvasoi-atolvasas"></a>Olvasói átolvasás. Olvasd végig az átírt szöveget az olvasó helyében, és nézd meg mondatonként:
   - Valódi cselekvő (K044): tud-e cselekedni az alany? Ha az alany képes vagy elvont („a pályázat támogatást kaphat”, „a rendszer úgy dönt”), az legyen az alany, aki valóban cselekszik („aki pályázik”), ha ez a forrásból egyértelmű. Ha nem az, írj általános alanyt, vagy jelezd a hiányt.
   - Az olvasó oldala (K008): azt írja-e le a mondat, mit lát, kap vagy tesz az olvasó? A kiadó belső művelete helyett az olvasó tapasztalata álljon („a döntést postai úton megküldjük” helyett „a döntést postán kapja meg”).
   - Az olvasó szavai (K029): a kiadó belső fogalmai és folyamatlépései helyett azt a szót használod-e, amelyet az olvasó mondana? („a jogviszony megszűnését követő hónap” helyett „a kilépése utáni hónap”, ha a kettő ugyanazt jelöli.) Ha a köznyelvi szó nem pontosan ugyanaz, de a különbség nem változtat azon, mit kell az olvasónak tennie vagy mire számíthat, cseréld, és a jelzések között kérd a kiadó ellenőrzését. A szakszó csak akkor maradjon, ha a különbség az olvasó dolgát megváltoztatná: kódnál vagy azonosítónál például a „karakter” nem cserélhető „betű”-re, mert a magyar „sz” vagy „cs” egy betű, de két karakter. A cserét a hűségtáblázatban „átfogalmazva” állapottal és egymondatos indoklással jelöld.
   - Ismétlés (K035): szerepel-e ugyanaz az esemény kétszer, más szerepben (például egyszer feltételként, egyszer egy határidő kezdeteként)? Ha igen, vond össze egy tagmondatba („Amint értesülünk arról, hogy …”), ha a jelentés nem változik; ha az összevonás megváltoztatná, mikor indul a határidő, hagyd külön, és mondd ki egyértelműen, miben különbözik a kettő.
   - Hivatali ige (K036): maradt-e az átírásban a forrás hivatali igéje (feltüntet, eszközöl, megküld, kiegyenlít)? Ha van egyszerűbb, cseréld.
   - Mi következik az olvasóra (K006, K007): ha a mondat már érthető, de az olvasó nem tudja, mi következik belőle rá nézve, és ez a forrásból egyenesen adódik, mondd ki. Ha nem adódik, ne találd ki: a jelzések között írd le, mi hiányzik.
   - Természetes magyar mondat (K028): felolvasva úgy hangzik-e, ahogy egy ember mondaná? Figyelj a névelőre („Ha a kérelmét”, nem „Ha kérelmét”) és a szórendre. A hivatali határozói igenév („az adatokat ellenőrizve”) és határozószó („hiánytalanul benyújtotta”) helyett írj mellékmondatot („miután ellenőriztük az adatokat”), ha így természetesebb, és a jelentés nem változik.

   Ha egy kérdésre a válasz nem, javíts, és csak utána mérj. A terjedelmi korlát ezt a lépést nem írja felül: ha a kettő ütközik, tartsd a korlátot, és a jelzésekben mondd meg, mit nem tudtál megoldani.
5. Mérés az átírt szövegen (`scripts/meres.py`), összevetve az eredetivel.
6. Hűségellenőrzés: menj végig a 2. lépés leltárán, és jelöld minden elemnél, hogy megvan-e változatlanul, átfogalmazva (azonos tartalommal), megváltozott-e, vagy kimaradt. Ami megváltozott vagy kimaradt, külön listában szerepeljen, indoklással.
7. Önellenőrzés az [ellenorzo-lista.md](ellenorzo-lista.md) kérdéseivel: azokat a csoportokat nézd végig, amelyek a szövegre vonatkoznak. Ha egy kérdésre nem a válasz, javíts, vagy írd a változtatások listájához, miért marad.
8. Jogi szövegnél: zárómondat a [jogi.md](jogi.md) szerint.

## Kimenet formája

<a id="kimenet"></a>

A kimenet négy része, ebben a sorrendben:

1. Az átírt szöveg.
2. A fő változtatások listája, a szabályazonosítókkal (például „K043: a „megküldésre kerül” helyett cselekvő ige”). Ahogy a NAV a mintái bemutatásánál is teszi: az eredeti és az átírt elem mellett álljon, mit és miért változtattál.
3. Hűségtáblázat:

   | Elem | Eredetiben | Átírtban | Állapot |
   |---|---|---|---|
   | határidő | „a kézhezvételtől számított 15 napon belül” | „a levél kézhezvételétől számított 15 napon belül” | megvan |
   | modalitás | „befizetése kötelező” | „Fizesse be” | átfogalmazva: a kötelezettség megmaradt |

   Az állapot lehet: megvan, átfogalmazva, megváltozott, kimaradt. A megváltozott és kimaradt elemeket a táblázat alatt külön is sorold fel, indoklással.
4. Mérés előtte–utána, és jogi szövegnél a zárómondat.

## Mit nem csinál

- Nem ír át kötelező szöveget.
- Nem told hozzá új tényt, számot vagy feltételt. Ha az olvasónak szüksége volna egy hiányzó adatra (például a határidőre), jelöld helyőrzővel („[határidő: kérdezd meg a kiadótól]”), ne találd ki.
- Szemléltető példát írhat, ha az a forrás szabályából egyértelműen levezethető, és nem állít vele új tényt (például minta kód egy kitalált dátummal). A példát jelölje példaként, és a jelzések között kérje, hogy a kiadó ellenőrizze. Ha a terjedelmi korlát miatt a példa kimarad, ezt is jelezze.
- Nem dönti el, hogy a jogi tartalom helyes-e; a hűségellenőrzés csak azt mutatja meg, hogy az átírás megtartotta-e.
- Nem készít könnyen érthető (KÉK) változatot.

## Példa

Bemenet: „Tájékoztatjuk, hogy a 2026. évi gépjárműadó befizetésére a határozat kézhezvételétől számított 15 napon belül kerül sor; amennyiben a befizetés elmarad, késedelmi pótlék kerül felszámításra.”

Átírt szöveg: „Fizesse be a 2026-os gépjárműadót a határozat kézhezvételétől számított 15 napon belül. Ha nem fizet határidőre, késedelmi pótlékot számítunk fel.”

Hűség: adónem és év megvan; határidő (15 nap a kézhezvételtől) megvan; jogkövetkezmény (késedelmi pótlék) megvan; modalitás (a befizetés kötelező) megvan, felszólító módban. Megváltozott vagy kimaradt elem nincs.
