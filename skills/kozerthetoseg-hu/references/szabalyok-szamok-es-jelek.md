<!-- GENERÁLT FÁJL. Ne szerkeszd kézzel: a forrása az assets/adatok/ mappa TOML-fájljai. Újragenerálás: python scripts/generalas.py -->

# Szabályok: Helyesírás, számok és írásjelek

Az összes csoport: [szabaly-index.md](szabaly-index.md).

<a id="k056"></a>

### K056 A szakkifejezések helyesírása

Szabály: A nehéz helyesírású szakkifejezéseket ellenőrizd helyesírási szótárban vagy tanácsadó portálon; a helyesírás-ellenőrző program nem szűr ki minden hibát.

Miért segít: A helyesírási hiba rontja a szöveg hitelét, és összetett szavaknál jelentést is változtathat.

Ellenőrző kérdés: A nehéz helyesírású szakkifejezéseket szótárban ellenőrizted?

- Rossz: Az SZJA bevallás és az ÁFA visszatérítés határideje...
- Jó: Az szja-bevallás és az áfa-visszatérítés határideje...

Kör: általános. Alapértelmezett súlyosság: alacsony. Ellenőrzés: olvasva.

Források: [Európai Bizottság 2013, 14. o.](forrasok.md#eu-pontos-fogalmazas-2013-049); [NAV 2024a, 30. o.](forrasok.md#nav-ertheto-hivatal-1-015); [NAV 2024b, 2, 66. o.](forrasok.md#nav-ertheto-hivatal-2-001); [NAV 2024b, 6. o.](forrasok.md#nav-ertheto-hivatal-2-005).

<a id="k057"></a>

### K057 Egységes dátum

Szabály: A dátumot egységes alakban írd (2026. április 4.), az „év”, „hónap”, „nap” szavak nélkül, a toldalékot a szabály szerint kapcsold (április 4-én, április 4-től).

Miért segít: A felesleges szavakkal megtoldott dátum nehezen olvasható, a vegyes formák pedig zavart keltenek.

Ellenőrző kérdés: A dátumok egységes alakban állnak (2026. április 4.)?

- Rossz: 2026. év április hónap 4. napján
- Jó: 2026. április 4-én

Kör: általános. Alapértelmezett súlyosság: alacsony. Ellenőrzés: jelölt. Keresőminta: dátum „év”, „hó”, „nap” szóval.

Források: [NAV 2024b, 52–53. o.](forrasok.md#nav-ertheto-hivatal-2-073).

<a id="k058"></a>

### K058 Számok egységes írása

Szabály: Egy szövegegységen belül a számokat egységesen írd (betűvel vagy számjeggyel); az öt- vagy többjegyű számokat hátulról hármasával tagold, nem törő szóközzel.

Miért segít: A következetlen számírás megakasztja az olvasót, a tagolatlan nagy szám pedig nehezen olvasható ki.

Ellenőrző kérdés: A számok írása egységes, és a nagy számok hármasával tagoltak?

- Rossz: A kerület 3 iskolájában tizenkétezer-ötszáz tanuló és 12500 szülő...
- Jó: A kerület 3 iskolájában 12 500 tanuló...

Kivételek:

- A négyjegyű számot nem kell tagolni, kivéve, ha táblázatban nagyobb számok alatt áll.

Kör: általános. Alapértelmezett súlyosság: alacsony. Ellenőrzés: jelölt. Keresőminta: tagolatlan, legalább ötjegyű szám.

Források: [NAV 2024b, 50. o.](forrasok.md#nav-ertheto-hivatal-2-071); [NAV 2024b, 51. o.](forrasok.md#nav-ertheto-hivatal-2-072).

<a id="k059"></a>

### K059 Pénzösszeg

Szabály: Folyó szövegben a pénznemet írd ki (forint, euró), a rövidítést (Ft, EUR, M Ft) táblázatban használd.

Miért segít: A kiírt pénznem folyó szövegben gördülékenyebben olvasható; táblázatban a rövidítés helyet takarít meg.

Ellenőrző kérdés: Folyó szövegben ki van írva a pénznem?

- Rossz: A díj 12345,-Ft.
- Jó: A díj 12 345 forint.

Kör: általános. Alapértelmezett súlyosság: alacsony. Ellenőrzés: jelölt. Keresőminta: pénznem rövidítése folyó szövegben.

Források: [NAV 2024b, 54–55. o.](forrasok.md#nav-ertheto-hivatal-2-074).

<a id="k060"></a>

### K060 Mértékegység és százalék

Szabály: A mértékegység jele előtt szóköz áll, utána nincs pont; a százalékjel a számhoz tapad; elvont dolgok számánál ne írj „db”-ot.

Miért segít: A mértékegységek írását szabvány határozza meg; a következetes írás könnyebben olvasható.

Ellenőrző kérdés: A mértékegység és a százalékjel írása szabályos?

- Rossz: 120km., 35 %, 12 db határozat
- Jó: 120 km, 35%, 12 határozat

Kör: általános. Alapértelmezett súlyosság: alacsony. Ellenőrzés: jelölt. Keresőminta: „db” elvont dolog mellett vagy hiányzó szóköz a mértékegység előtt.

Források: [NAV 2024b, 56–57. o.](forrasok.md#nav-ertheto-hivatal-2-075).

<a id="k061"></a>

### K061 Kötőjel, gondolatjel, nagykötőjel

Szabály: A kötőjelet szavak összekapcsolására, a gondolatjelet szóközökkel közbevetésre, a nagykötőjelet (–) tól–ig viszonyra és népek, nyelvek, helyek összekapcsolására használd.

Miért segít: A három jel különböző viszonyt jelöl; ha összekeverednek, a szerkezet nehezebben olvasható ki.

Ellenőrző kérdés: A kötőjel, a gondolatjel és a nagykötőjel a helyén van?

- Rossz: a 2025-2026-os időszakban, Budapest-Bécs járat
- Jó: a 2025–2026-os időszakban, Budapest–Bécs járat

Kör: általános. Alapértelmezett súlyosság: alacsony. Ellenőrzés: olvasva.

Források: [NAV 2024b, 42–43. o.](forrasok.md#nav-ertheto-hivatal-2-066).

<a id="k062"></a>

### K062 Vessző az „illetve”, az „és” és a „mint” előtt

Szabály: Az „illetve”, „valamint”, „továbbá” elé tegyél vesszőt; az „és” elé akkor, ha tagmondatot vezet be; a „mint” elé, ha hasonlítást vezet be.

Miért segít: Az „és” előtti vessző a jelentést is megváltoztathatja: eldönti, hogy két cselekvés közös-e.

Ellenőrző kérdés: Megvan a vessző az „illetve”, a tagmondatot bevezető „és” és a hasonlító „mint” előtt?

- Rossz: Postán illetve elektronikusan küldheti el.
- Jó: Postán, illetve elektronikusan küldheti el.

Kör: általános. Alapértelmezett súlyosság: alacsony. Ellenőrzés: jelölt. Keresőminta: hiányzó vessző az „illetve”, „valamint”, „továbbá” előtt.

Források: [NAV 2024b, 45. o.](forrasok.md#nav-ertheto-hivatal-2-068); [NAV 2024b, 46–47. o.](forrasok.md#nav-ertheto-hivatal-2-069); [NAV 2024b, 48. o.](forrasok.md#nav-ertheto-hivatal-2-070).

<a id="k063"></a>

### K063 Felkiáltójel a felszólító mondat végén

Szabály: A felszólító mondat végére tegyél felkiáltójelet; ez helyesírási szabály, nem udvariatlanság.

Miért segít: A felkiáltójel jelzi, hogy a mondat teendőt ad, nem tájékoztat. Sok egymást követő felszólításnál (útmutatóban) megengedőbb a szabály.

Ellenőrző kérdés: A felszólító mondatok végén felkiáltójel áll?

- Rossz: Kérjük, küldje el a nyilatkozatot.
- Jó: Kérjük, küldje el a nyilatkozatot!

Kivételek:

- Lépésenkénti útmutatóban, ahol sok felszólítás követi egymást, a pont is elfogadott.

Kör: általános. Alapértelmezett súlyosság: alacsony. Ellenőrzés: jelölt. Keresőminta: felszólító „kérjük” mondat felkiáltójel nélkül.

Források: [NAV 2024b, 44. o.](forrasok.md#nav-ertheto-hivatal-2-067).
