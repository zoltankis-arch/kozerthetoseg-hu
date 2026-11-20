---
name: kozerthetoseg-hu
description: >-
  Magyar szövegek közérthetőségének vizsgálata és javítása forrásokkal
  alátámasztott szabálykatalógus alapján: jelentés, átírás hűségellenőrzéssel,
  felszíni mérés, olvasói próbaterv és új forrás felvétele. Használd, ha egy
  magyar szöveget közérthetőbbé, érthetőbbé kell tenni, egyszerűsíteni kell,
  vagy meg kell nézni, mennyire közérthető: hivatali levél, tájékoztató,
  ügyfél-tájékoztató, adatkezelési tájékoztató, ÁSZF, szerződés, határozat,
  jogi szöveg, nyomtatvány, weboldal szövege. Akkor is, ha a kérés plain
  language-et, közérthetőséget, egyszerűsítést vagy egyszerűbb fogalmazást
  említ. Jogi
  szövegnél jogi modult tölt be, és nem ad jogi tanácsot. Ne indítsd nem
  magyar szövegre, gép–gép kimenetre (JSON, napló, kód) és szépirodalomra.
license: MIT (szkriptek, tesztek) és CC-BY-4.0 (szöveges tartalom), lásd LICENSE.txt
compatibility: A szkriptekhez Python 3.11 vagy újabb kell, külső csomag és hálózat nélkül. A HuSpaCy opcionális.
metadata:
  version: "1.3.0"
  author: "Kis Zoltán (https://github.com/zoltankis-arch)"
  language: "hu"
  forraskatalogus: "1.3.0"
---

# Közérthetőség magyarul

A skill azért dolgozik, hogy az olvasó megkapja, megtalálja, megértse és használni tudja a szöveget. Minden javaslata egy szabályra épül, minden szabály egy vagy több nyilvános forrásra (útmutató, tanulmány, jogszabály), oldalszámmal.

## Mikor ne fusson

- A szöveg nem magyar: mondd meg, hogy a skill magyar szövegre készült, és ne értékeld.
- Gép–gép kimenet (JSON, napló, séma, kód): nem olvasónak szól.
- Szépirodalom: ott a nehezebb nyelv a mű része.
- Ha a hívó kifejezetten könnyen érthető (KÉK) szöveget kér: a skill felismeri és jelzi az igényt, de KÉK-szöveget nem készít ([kek-hatar.md](references/kek-hatar.md)).

## Parancsok

Minden parancs saját referenciafájlt kap, egységes szerkezettel. Olvasd el a parancs fájlját, mielőtt futtatod. Ha a hívó nem nevez meg parancsot, a kérésből válaszd ki: véleményt kér → `audit`; átírást kér → `atiras`.

A példákban a `scripts/`, `references/`, `assets/` és `evals/` útvonalak a `SKILL.md` mappájából indulnak. Ha más mappában futtatod a parancsot, a szkripthez és a bemeneti fájlhoz is a teljes elérési utat add meg.

| Parancs | Mit csinál | Részletek |
|---|---|---|
| `audit` | Jelentést ad, nem ír át: hol, melyik szabály, miért baj az olvasónak, javasolt átírás, prioritás | [parancs-audit.md](references/parancs-audit.md) |
| `atiras` | Átírja a szöveget, utána hűségellenőrzést végez: minden tény, szám, határidő, feltétel, kivétel, modalitás és jogi kifejezés megvan-e | [parancs-atiras.md](references/parancs-atiras.md) |
| `meres` | Lefuttatja a mérőszkriptet, és jelzésként értelmezi az eredményt; minden jelzés egy szabályhoz kötődik, súlyossággal | [parancs-meres.md](references/parancs-meres.md) |
| `proba` | Olvasói próbatervet ír 6–9 fős, visszamondásos módszerrel | [parancs-proba.md](references/parancs-proba.md) |
| `forras-felvetel` | Új forrást dolgoz fel öt lépésben, újragenerál, ellenőriz, verzióemelést javasol | [parancs-forras-felvetel.md](references/parancs-forras-felvetel.md) |
| `ellenorzes` | Teljességi és konzisztencia-ellenőrzés: séma, azonosítók, lefedettség, hivatkozások | [parancs-ellenorzes.md](references/parancs-ellenorzes.md) |

## Közös munkafolyamat (`audit` és `atiras`)

1. Olvasó és cél. Ki olvassa a szöveget, mit tud már, mit kell tennie utána. Ha a hívó nem mondja meg, egyetlen kérdésben kérdezz rá. Ha nincs kit kérdezni, írd le, milyen olvasót feltételeztél, és haladj tovább.
2. Szövegtípus. Sorold be a [szovegtipusok.md](references/szovegtipusok.md) szerint: előíró normaszöveg, eljárási vegyes szöveg (határozat, beadvány, panasz), leíró metajogi szöveg vagy nem jogi tájékoztató. Döntsd el azt is, kötelező szöveg-e (jogszabály, előírt formula, jogszabályban megállapított feltétel, kamarai egységes szöveg). Kötelező szöveget a skill nem ír át: kimondja, hogy kötelező, és hogy a forrásával kell egyeznie.
3. KÉK-határ. Ha az olvasó értelmi fogyatékossággal élő vagy alacsony nyelvi kompetenciájú, mondd ki, hogy ehhez könnyen érthető kommunikáció kell, ami más szabályrendszer ([kek-hatar.md](references/kek-hatar.md)).
4. A négy kérdés mint keret (ISO 24495-1): megkapja-e az olvasó, amire szüksége van; megtalálja-e; megérti-e; tudja-e használni.
5. Vizsgálat a szabálykatalógus szerint. Először a tömör [szabaly-index.md](references/szabaly-index.md) fájlt olvasd el; a példákat, kivételeket és forrásokat csak a szövegre vonatkozó szabályoknál nyisd meg a csoportfájlban (`references/szabalyok-<csoport>.md`). A teljes `szabalyok.md`-t ne töltsd be. Hivatkozz a szabály azonosítójára (K001–K083).
6. Mérés, jelzésként: `python scripts/meres.py <fájl>` ([parancs-meres.md](references/parancs-meres.md)).
7. Jogi szövegnél a jogi modul is ([jogi.md](references/jogi.md)). Ilyenkor a kimenet mindig ezzel zárul: „A skill nem ad jogi tanácsot. A jogi tartalom változatlanságáért a szakember felel.”

## Alapelvek

- Megszólítás: ha a szöveg maga nem dönt, a skill magázást javasol (Ön), és a szöveg végéig azt tartja (K048, K049). Ha a szöveg tegez, a tegezés marad.
- A mérőszám jelzés, nem ítélet. A szkript nem tudja megmérni, hogy egy szó két jelentésben szerepel-e, vagy hogy a fő üzenet elöl áll-e; ezt olvasva kell megnézni.
- Ne találj ki hibát. Ha a szöveg már közérthető, mondd ki; legfeljebb alacsony prioritású javaslatot adj.
- Ne találj ki tényt. Átírásnál új adatot (határidőt, összeget, feltételt) nem írsz bele; ha hiányzik, helyőrzővel jelzed.
- A szerkezeti átírás (sorrend, tagolás, mondat) biztonságosabb a szócserénél; jogi kifejezést csak magyarázattal együtt cserélj, ha egyáltalán.
- A skill nem pótolja az olvasói próbát. Nagy tétnél (sok olvasó, fizetés, határidő) javasold a `proba` parancsot.
- Ha a források ellentmondanak egymásnak, a szabály „Ha a források eltérnek” bekezdése mondja meg, melyiket követed és miért.
- A kimenet nyelve magyar.

## Fájlok

- [references/szabaly-index.md](references/szabaly-index.md): a szabálykatalógus tömör indexe, szabályonként egy sor (generált). Ezt olvasd be először.
- `references/szabalyok-<csoport>.md`: a szabályok részletei csoportonként, példákkal és forrásokkal (generált).
- [references/ellenorzo-lista.md](references/ellenorzo-lista.md): szabályonként egy eldöntendő kérdés (generált).
- [references/szotar.md](references/szotar.md): körülményes kifejezések egyszerűbb megfelelője, és mikor ne cseréld (generált). Átírásnál használd.
- [references/szabalyok.md](references/szabalyok.md): a teljes katalógus egy fájlban, emberi olvasásra (generált).
- [references/forrasok.md](references/forrasok.md): a forráskatalógus és a teljes forrásleltár (generált).
- [references/lefedettseg.md](references/lefedettseg.md): melyik forrás melyik tétele hová került (generált).
- [references/szovegtipusok.md](references/szovegtipusok.md): mit szabad átírni szövegtípusonként.
- [references/jogi.md](references/jogi.md): jogi modul; csak jogi szövegnél töltsd be.
- [references/kek-hatar.md](references/kek-hatar.md): mikor kell könnyen érthető kommunikáció.
- [assets/sablonok/jelentes.md](assets/sablonok/jelentes.md): az audit jelentéssablonja.
- [scripts/](scripts/): `meres.py`, `ellenorzes.py`, `generalas.py`, `uj_forras.py`, `uj_szabaly.py`; mindegyiknek van `--help` kapcsolója.

A szabályok és a források igazság forrása az `assets/adatok/` mappa TOML-fájljai. A generált referenciákat kézzel ne szerkeszd: módosítsd az adatot, majd futtasd a `scripts/generalas.py`-t és a `scripts/ellenorzes.py`-t.
