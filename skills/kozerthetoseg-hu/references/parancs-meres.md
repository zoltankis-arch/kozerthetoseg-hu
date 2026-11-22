# Parancs: `meres`

Lefuttatja a mérőszkriptet, és az eredményt jelzésként értelmezi: megmutatja, hol érdemes ránézni a szövegre.

## Mikor kell

Ha a hívó számokat kér a szövegről (mondathossz, főnevesítés, „kerül”-szerkezetek), vagy ha az `audit` és az `atiras` 6., illetve 4. lépése fut.

## Bemenet

- Markdown- vagy sima szövegfájl, vagy a szabványos bemenet. A YAML-frontmattert, a HTML-megjegyzést, a kódblokkot és a sorközi kódot a szkript kihagyja; a címsorokat és a táblázatsorokat nem számolja a mondatok közé.
- Elhagyható kapcsolók: `--json`, `--kuszob N` (mondathossz-küszöb, alapérték 20), `--szohossz N` (hosszú szó határa, alapérték 15), `--huspacy` (ha a HuSpaCy és egy magyar modell telepítve van), `--max-jelzes N` és `--szint magas|kozepes|alacsony` (CI-hez: 1-es kilépési kód, ha a megadott vagy súlyosabb jelzések száma N-nél több).

## Lépések

1. Futtasd: `python scripts/meres.py szoveg.md` (gépi feldolgozáshoz `--json`). A szkript csak a Python 3.11+ standard könyvtárát használja, hálózat nem kell, és ugyanarra a szövegre mindig ugyanazt adja.
2. Olvasd ki a mutatókat és a „Szabályonkénti jelzések” táblázatot. Minden jelzés egy szabályhoz kötődik, a szabály alapértelmezett súlyosságával és az ellenőrzés módjával: a „gépi” jelzés megbízható, a „jelölt” csak arra mutat, hol érdemes ránézni.
3. Minden kiugró értéknél nézd meg magát a mondatot: a szám csak jelölt. Egy 24 szavas, jól tagolt mondat lehet rendben; egy 12 szavas, kettős tagadással nem.
4. Ha a szkript hibával lép ki (nincs fájl, üres bemenet, nincs HuSpaCy), add tovább a magyar hibaüzenetet.

<a id="mit-mer"></a>

### Mit mér, és melyik szabályhoz tartozik

| Mutató | Mit számol | Szabály |
|---|---|---|
| `mondathossz` | átlag, medián, maximum, a küszöb feletti mondatok | K020, K023 |
| `fonevesites` | -ás/-és képzős főnevek (jelöltek), 100 szóra vetítve | K042 |
| `kerul_szerkezet` | „-ásra/-ésre kerül” és fordított sorrendje | K043 |
| `altal_torteno_valo` | „által”, „történő”, „való” és az előttük álló szó | K042 |
| `illetve_illetoleg` | „illetve”, „illetőleg” | K047 |
| `zarojelmelyseg` | a zárójelek legnagyobb mélysége, egymásba ágyazott zárójelek | K024 |
| `hosszu_szavak` | 15 betűnél hosszabb szavak | K029, K032 |
| `hivatali_fordulatok` | rögzített lista: amennyiben, tekintettel arra, eszközöl, foganatosít, sor kerül és társaik | K035, K036, K045, K050 |
| `tagadas` | „nem” + tagadó jelentésű szó (mellőz, nélkül, tilos, kivéve…) | K026, K046 |
| `huspacy` | függőségi mélység, beágyazott tagmondatok (csak `--huspacy` kapcsolóval) | K023 |

<a id="szabalyvezerelt"></a>

### Szabályvezérelt jelzések

A beépített mutatók mellett a szkript két adatforrásból dolgozik:

- a szabályok `minta` mezőjéből: egyszerű keresőminták a gépileg jelezhető szabályokhoz (például „és/vagy”, tagolatlan ötjegyű szám, ható ige a kiadó tevékenységéről);
- a szótárból (`assets/adatok/szotar.toml`, olvasható változata: [szotar.md](szotar.md)): körülményes kifejezés, egyszerűbb megfelelő, és mikor ne cseréld.

Minden szabály `ellenorzes` mezője megmondja, mennyire bízhatsz a jelzésben: `gepi` (a szkript megbízhatóan jelzi), `vegyes` (jelöltet ad, olvasva kell dönteni) vagy `itelet` (csak olvasva ellenőrizhető, a szkript nem jelzi). A `sulyossag` mező az alapértelmezett prioritás; a konkrét esetben az audit eltérhet tőle.

A választás nem véletlen. Balogh (2023) a pszicholingvisztikai irodalom alapján a mondat- és szóhosszt, a szokatlan szórendet, a személytelen szerkezetet és a beágyazott mellékmondatot sorolja a megértést nehezítő jelenségek közé. Üveges (2026) korpuszán a közérthető mondatokkal együtt jár az alacsonyabb lexikai sűrűség, kevesebb visszautaló névmás, kevesebb beágyazott tagmondat és főnevesítés.

<a id="korlatok"></a>

### Korlátok

A mérőszám jelzés, nem ítélet. Üveges (2026) NAV-szövegekből és közérthető átirataikból épített korpuszán (4666 nem közérthető és 4963 közérthető mondat) a felszíni és szintaktikai jegyekre épített logisztikus regresszió F1 = 0,58-at ért el, a finomhangolt nyelvi modell is csak 69 százalékos pontosságot. Ugyanebben a korpuszban a közérthető mondatok átlaga is 25 token fölött van.

A szkript nem tudja megmérni:

- hogy egy szó a szövegen belül két jelentésben szerepel-e (K034);
- hogy az olvasó ismeri-e a szakszót (K029–K032);
- hogy a fő üzenet elöl áll-e, és kiderül-e a teendő (K002–K004).

Ezeket olvasva kell megnézni. A szkript kimenete is kimondja ezt.

A főnevesítési jelölt felszíni minta: néhány lexikalizálódott főnevet (kérdés, bekezdés, szerződés) kihagy, de más, nem igéből képzett szót is jelölhet.

## Kimenet formája

A szkript Markdown-kimenete (vagy JSON), ezzel kezdve: „A mérőszám jelzés, nem ítélet.” Utána legfeljebb öt mondat értelmezés: melyik mutató ugrik ki, melyik mondatokra érdemes ránézni, és melyik szabály szerint.

## Mit nem csinál

- Nem pontoz, nem ad érthetőségi indexet, és nem dönti el, hogy a szöveg közérthető-e.
- Nem ír át.
- Hálózatot nem használ; a HuSpaCy-modellt sem tölti le.

## Példa

`python scripts/meres.py evals/szovegek/03-hatosagi-level.md` egy hiánypótlási felhívásra: átlagos mondathossz 13,8 szó, a leghosszabb mondat 37 szó, 2 mondat 20 szó felett, 5 „kerül”-szerkezet, 3 hivatali fordulat.

Értelmezés: „Az átlagot a rövid tárgysor és a megszólítás lehúzza; a 4. mondat 37 szavas, és egyszerre hordozza a teendőt, a határidőt és a jogkövetkezményt, ezt érdemes bontani (K020, K023). Az öt „kerül”-szerkezet (K043) elrejti, ki döntött és kinek mi a dolga. A „Kérjük tájékoztatásunk szíves tudomásulvételét” elhagyható (K050).”
