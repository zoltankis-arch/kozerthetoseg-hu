# Változásnapló

Minden lényeges változás ebben a fájlban szerepel. A formátum a
[Keep a Changelog](https://keepachangelog.com/hu/1.1.0/) ajánlását követi,
a verziózás a [Szemantikus verziókezelést](https://semver.org/lang/hu/).

Verzióemelés: új forrás vagy új szabály: minor; megfogalmazás-javítás:
patch; szabály visszavonása vagy parancs átnevezése: major.

## [Kiadatlan]

## [1.4.0] - 2026-11-22

### Hozzáadva

- Összehasonlító evalok: 14 eval skill-lel és nélküle, ugyanazzal a modellel, vak bírálóval. A nyers válaszok, az értékelések és az összesítés az `eredmenyek/iteracio-2/` mappában vannak. A `tools/eval_osszesit.py` újraszámolja a közölt számokat, a CI `--ellenoriz` kapcsolóval futtatja.
- Nyomáspróbák (13–15. eval): felére rövidítés kivételekkel, törvényszöveg átírása kérésre, hiányzó határidő beírása.
- Előtte–utána példák: `examples/`, négy szöveg eredetije, átírása és a változtatások listája.
- README: „Mennyit javít?” szakasz az eredményekkel és a korlátaikkal.

A szabálykatalógus nem változott, ezért a forráskatalógus verziója 1.3.0 marad.

## [1.3.0] - 2026-11-20

### Hozzáadva

- Szabályvezérelt mérés: minden szabály `ellenorzes` (gépi, vegyes, ítélet) és `sulyossag` mezőt kapott, a gépileg jelezhetők `[[minta]]` keresőmintát. A `meres.py` minden jelzést szabályazonosítóhoz köt („Szabályonkénti jelzések” táblázat, JSON-ban `jelzesek`).
- Szótár: `assets/adatok/szotar.toml`, 64 körülményes kifejezés egyszerűbb megfelelővel, forrással és „mikor ne cseréld” megjegyzéssel; olvasható változata a generált `references/szotar.md`. A mérés javaslatként jelzi, az `atiras` forrásként használja.
- `meres.py --max-jelzes N --szint …`: 1-es kilépési kód, ha a jelzések száma túllépi a határt (dokumentációs CI-hez).
- Ellenőrzés: a szótár sémája, regexei és hivatkozásai; a minták regexei; minden gépi vagy vegyes szabályhoz tartozik mérés.
- A szabályindex súlyosságot és ellenőrzési módot is mutat.

## [1.2.0] - 2026-11-20

### Hozzáadva

- Tömör szabályindex (`references/szabaly-index.md`, kb. 10 KB) és csoportonkénti részletfájlok (`references/szabalyok-<csoport>.md`). A skill ezeket tölti be a 96 KB-os teljes katalógus helyett.
- Generált ellenőrző lista (`references/ellenorzo-lista.md`): minden szabály új `kerdes` mezőt kapott, egy eldöntendő kérdést. Az `atiras` utolsó lépése ezzel ellenőriz.
- Modalitás a hűségellenőrzésben: az `atiras` leltára a „kell”, „köteles”, „jogosult”, „-hat/-het”, „tilos” és hasonló elemeket is gyűjti. A 2. eval ezt ellenőrzi.
- Fejlesztési terv: ROADMAP.md.

- SECURITY.md és issue-sablon-beállítás (config.yml).
- Külön licencfájl a két licenc teljes szövegével (LICENSE-MIT, LICENSE-CC-BY-4.0); a LICENSE áttekintést ad.
- Jelvények a README elején.

### Javítva

- Az issue-sablonok a repó meglévő címkéit használják.
- README: a skill saját `audit` és `atiras` parancsával átnézve. Új rész arról, mi az a skill és hogyan kezdd; lépésenkénti telepítés; kérdés formájú alcímek; az elsődleges források helyes száma (öt).
- A referenciákban „jogszabály által” helyett „jogszabályban” (K042).
- README: új rész a tudásbázis 17 forrásáról, forrásonként a hivatkozással, a felhasználás céljával, a tételszámmal és az elérhetőséggel. Egy teszt ellenőrzi, hogy minden forrás szerepel benne.
- A NAV két kötetének forrásrekordja megkapta a kiadó nyilvános oldalát.

## [1.1.0] - 2026-11-20

### Hozzáadva

- Új forrás: Világos Beszéd: Hogyan írjunk közérthetően? Kézikönyv (Budapest Főváros Főpolgármesteri Hivatal, 2025), a kisokos bővített változata. 13 fejezet, 125 leltártétel; a tételek meglévő szabályokba olvadtak, új szabály nem kellett.
- Eltérésbejegyzés a K020 (mondathossz) és a K023 (tagmondatok száma) szabályban: a kézikönyv mondathossz-küszöbe szigorúbb, a tagmondatszáma engedékenyebb.

### Javítva

- A forrássablon és a `forras-felvetel` leírása egyértelműen mondja meg, mit kell írni a licencmezőbe, ha a forrás nem nevez meg licencet.

## [1.0.0] - 2026-11-20

### Hozzáadva

- A skill első kiadása hat paranccsal: `audit`, `atiras`, `meres`, `proba`, `forras-felvetel`, `ellenorzes`.
- Szabálykatalógus 83 szabállyal (K001–K083), 11 csoportban, saját példákkal.
- Forráskatalógus 16 forrással és 342 leltártétellel; a négy elsődleges dokumentum (Világos Beszéd kisokos, NAV: Az érthető hivatal 1–2., Európai Bizottság: A pontos fogalmazás művészete) teljes leltára.
- Jogi modul (Jszr., Jat., Air., Ptk. 6:102–6:103., GDPR 12. cikk, WP260, EUB C-26/13).
- Szövegtípus-döntés (Balogh, Bennion, NAV) és KÉK-határ.
- Szkriptek: `meres.py`, `ellenorzes.py`, `generalas.py`, `uj_forras.py`, `uj_szabaly.py`; pytest-tesztek; CI.

[Kiadatlan]: https://github.com/zoltankis-arch/kozerthetoseg-hu/compare/v1.4.0...HEAD
[1.4.0]: https://github.com/zoltankis-arch/kozerthetoseg-hu/compare/v1.3.0...v1.4.0
[1.3.0]: https://github.com/zoltankis-arch/kozerthetoseg-hu/compare/v1.2.0...v1.3.0
[1.2.0]: https://github.com/zoltankis-arch/kozerthetoseg-hu/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/zoltankis-arch/kozerthetoseg-hu/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/zoltankis-arch/kozerthetoseg-hu/releases/tag/v1.0.0
