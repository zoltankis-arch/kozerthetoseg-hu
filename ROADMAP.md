# Fejlesztési terv

Ez a terv az angol nyelvű plain language skillek és a Vale prózalinter összevetéséből készült. Minden pont egy-egy kiadáshoz kötődik; a kész pontokat a CHANGELOG.md is felsorolja.

## 1.2.0: gyors javítások a meglévő működésben (kész)

1. **Tömör szabályindex és csoportonkénti részletek.** A `szabalyok.md` túl nagy ahhoz, hogy minden futásnál egyben betöltődjön. A generálás készít egy indexet (szabályonként egy sor) és csoportonként egy részletes fájlt. A skill az indexet olvassa, a részleteket csak a talált szabályoknál.
   Kész, ha: az index 15 KB alatt van, a SKILL.md erre hivatkozik, az ellenőrzés a fájlok frissességét is nézi.
2. **Modalitás a hűségellenőrzésben.** Az `atiras` leltára a „kell”, „köteles”, „jogosult”, „-hat/-het”, „tilos” és hasonló elemeket is gyűjti, és jelzi, ha az átírás megváltoztatta őket.
   Kész, ha: a parancsfájl és a SKILL.md kimondja, és egy eval ellenőrzi.
3. **Generált ellenőrző lista.** Minden aktív szabály kap egy eldöntendő kérdést (`kerdes` mező). Ezekből készül a `references/ellenorzo-lista.md`, amelyet az `atiras` utolsó lépése és az ember is használ.
   Kész, ha: mind a 83 szabálynak van kérdése, a séma megköveteli, a lista generált.

## 1.3.0: szabályvezérelt mérés (kész)

4. **Gépi és ítéleti szabályok szétválasztása.** Minden szabály új mezőket kap: `ellenorzes` (gépi, ítélet vagy vegyes), alapértelmezett `sulyossag`, és gépi szabálynál a keresett minták (`minta`). A `meres.py` ezekből dolgozik, nem beégetett listából. Új kapcsolók: `--kuszob` és szabályazonosítós kimenet, kilépési kóddal.
   Kész, ha: a mérés minden jelzése egy szabályazonosítóhoz kötődik, és a jelenlegi tesztek változatlan eredménnyel futnak.
5. **Szótár adatfájlként.** `assets/adatok/szotar.toml`: körülményes kifejezés, egyszerűbb megfelelő, szabály, forrás, és mikor nem kell cserélni. A mérés javaslatként használja, az `atiras` forrásként.
   Kész, ha: legalább 60 pár forrással, a mérés kiírja a találatokat, az ellenőrzés a párok forrását is nézi.

## 1.4.0: mérhető hatás (kész)

6. **Összehasonlító evalok.** Minden eval két futással: a skill-lel és nélküle, ugyanazzal a modellel. Mérőszám: a mérés jelzései 100 szóra, az elvárások teljesülése, és vak bíráló döntése. A nyers eredmények a repóba kerülnek (`eredmenyek/`), egy szkript újraszámolja a közölt számokat, a CI lefuttatja.
7. **Nyomáspróbák.** Evalok, amelyek a hibára csábítanak: „csak rövidítsd le”, „írd át mégis a törvényt”, „tegyél bele egy határidőt”.
8. **Előtte–utána példák.** `examples/` mappa a kitalált tesztszövegek eredeti és átírt változatával, a változtatások listájával.

## 1.5.0: új funkciók

9. **`iras` parancs.** Új szöveg a tényekből, sablonnal: hivatali levél, hiánypótlási felhívás, adatkezelési tájékoztató, ügyfélnek szóló ÁSZF-összefoglaló. Hiányzó adatnál kérdez vagy helyőrzőt tesz.
10. **Rendszerprompt-változat.** `prompts/rendszerprompt.md`, a katalógusból generálva, skill-támogatás nélküli eszközökhöz.

## Később

11. **Vale-csomag.** A gépi szabályokból generált Vale-stílus, hogy a magyar közérthetőségi ellenőrzés szerkesztőben és dokumentációs CI-ban is fusson. Feltétele a 4. és az 5. pont.

## Amit nem veszünk át

- A GOV.UK tiltja a félkövér kiemelést; a Világos Beszéd javasolja. A magyar forrás az irányadó.
- Az ASD-STE100 kötött szókincse: magyarul nincs megfelelője, és a szöveget a könnyen érthető kommunikáció felé tolná.
