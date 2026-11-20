# kozerthetoseg-hu

[![Ellenőrzés](https://github.com/zoltankis-arch/kozerthetoseg-hu/actions/workflows/ellenorzes.yml/badge.svg)](https://github.com/zoltankis-arch/kozerthetoseg-hu/actions/workflows/ellenorzes.yml)
[![Verzió](https://img.shields.io/badge/verzi%C3%B3-1.3.0-blue)](CHANGELOG.md)
[![Licenc: MIT és CC BY 4.0](https://img.shields.io/badge/licenc-MIT%20%2B%20CC%20BY%204.0-green)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-specifik%C3%A1ci%C3%B3-informational)](https://agentskills.io/specification)

A kozerthetoseg-hu megnézi, mennyire érthető egy magyar szöveg, és közérthetőbbre írja: hivatali levelet, tájékoztatót, adatkezelési tájékoztatót, ÁSZF-et, határozatot. Minden javaslata egy szabályra épül, minden szabály nyilvános forrásra, oldalszámmal.

Nyelvészeknek, jogászoknak, hivatali szövegíróknak és fejlesztőknek készült.

## Mi az a skill?

A skill egy mappa utasításokkal, szabályokkal és szkriptekkel. Egy mesterséges intelligenciával működő asszisztens, például a Claude, akkor tölti be, amikor a feladat illik hozzá. Ez a skill az [Agent Skills](https://agentskills.io/specification) szabványt követi, ezért más, a szabványt ismerő eszközben is használható.

A mérőszkript asszisztens nélkül, önmagában is fut (lásd lent).

## Hogyan kezdjem?

1. Telepítsd a skillt (lásd: [Hogyan telepítem?](#hogyan-telepítem)).
2. Írd az asszisztensnek, mit szeretnél, a szöveggel együtt. Például: „Nézd át közérthetőség szempontjából ezt a levelet. Lakossági ügyfélnek megy.”
3. Az asszisztens megkérdezheti, ki a szöveg olvasója. Ha megmondod, pontosabb lesz a jelentés.

## Mit tud?

Hat parancsa van. A parancsot nem kell megnevezned: ha véleményt kérsz, jelentést kapsz; ha átírást, átírt szöveget.

| Parancs | Mit csinál |
|---|---|
| `audit` | Jelentést ad a szövegről, de nem írja át. Minden észrevételnél megmondja, hol van a gond, melyik szabályt sérti, miért baj az olvasónak, hogyan lehetne jobb, és mennyire sürgős. |
| `atiras` | Átírja a szöveget. Utána ellenőrzi, hogy minden tény, szám, határidő, feltétel és jogi kifejezés megmaradt-e. |
| `meres` | Lefuttatja a mérőszkriptet: mondathossz, főnévvé tett igék, „kerül”-szerkezetek, a szótár körülményes kifejezései és hasonlók. Minden jelzést egy szabályhoz köt, súlyossággal. A szám jelzés, nem ítélet. |
| `proba` | Olvasói próbát tervez: 6–9 ember a célcsoportból elolvassa a szöveget, és saját szavaival elmondja, mit értett. |
| `forras-felvetel` | Új forrást vesz fel a skill tudásbázisába, szabványos lépésekkel. |
| `ellenorzes` | Ellenőrzi, hogy a tudásbázis teljes és ellentmondásmentes. |

A tudásbázis két részből áll: a szabálykatalógusból (83 szabály, K001–K083) és a forrásleltárból. A leltár a források minden szabályát és ajánlását külön tételként tartja nyilván.

### Példák

`audit`. Bemenet: „A kérelem elbírálásra került, a határozat postai úton megküldésre kerül.” Kimenet (részlet):

| Hol | Szabály | Mi a baj az olvasónak | Javaslat | Prioritás |
|---|---|---|---|---|
| „elbírálásra került” | K043: cselekvő ige az „-ásra/-ésre kerül” helyett | Nem derül ki, ki döntött, és mi a döntés. | „Elbíráltuk a kérelmét: …” | magas |

`atiras`. Bemenet: „…befizetésére a határozat kézhezvételétől számított 15 napon belül kerül sor…” Kimenet: „Fizesse be a határozat kézhezvételétől számított 15 napon belül.” Mellette egy táblázat mutatja, hogy a határidő változatlanul megmaradt.

`meres`. Egy hiánypótlási felhívásra (részlet):

```
python kozerthetoseg-hu/scripts/meres.py kozerthetoseg-hu/evals/szovegek/03-hatosagi-level.md

> A mérőszám jelzés, nem ítélet. …
| Leghosszabb mondat | 37 szó |
| 20 szó feletti mondatok | 2 |
| „-ásra/-ésre kerül” | 5 |
```

`proba`. Bemenet: egy parkolási tájékoztató. Kimenet: 7 résztvevő a kerület autótartó lakói közül, megállási pontok és kérdések. A résztvevők a megállási pontoknál saját szavaikkal elmondják, amit olvastak. Egy kérdés: „Ha az engedélye március 3-án jár le, mikortól kérheti az újat?”

`forras-felvetel`. Bemenet: egy új útmutató. Kimenet: új forrásfájl a leltárral; a tételek meglévő vagy új szabályokhoz rendelve; frissített referenciák; hibátlan ellenőrzés és javaslat a verzióemelésre.

`ellenorzes`:

```
python kozerthetoseg-hu/scripts/ellenorzes.py

Rendben: 17 forrás, 467 leltártétel, 83 aktív és 0 visszavont szabály.
```

## Hogyan telepítem?

A skill maga a repó `kozerthetoseg-hu/` mappája.

### claude.ai

1. Töltsd le a repót: a GitHubon a zöld Code gomb, majd Download ZIP.
2. Csomagold ki. A kicsomagolt `kozerthetoseg-hu-main` mappában van a `kozerthetoseg-hu` mappa.
3. Ezt a belső mappát tömörítsd ZIP-be.
4. Töltsd fel a claude.ai beállításaiban, a skillek között.

### Claude Code

Másold a mappát a `~/.claude/skills/` (személyes) vagy a projekt `.claude/skills/` mappájába:

```
git clone https://github.com/zoltankis-arch/kozerthetoseg-hu
cp -r kozerthetoseg-hu/kozerthetoseg-hu ~/.claude/skills/
```

### Codex

A plugint a Codex CLI-vel vagy a ChatGPT asztali alkalmazásának Codex nézetében telepítheted. Az alábbi két útmutató első lépése a piactér hozzáadása a terminálban.

#### Telepítés a Codex CLI-vel

Futtasd ezt a két parancsot a terminálban:

```sh
codex plugin marketplace add zoltankis-arch/kozerthetoseg-hu
codex plugin add kozerthetoseg-hu@kozerthetoseg-hu
```

#### Telepítés a ChatGPT asztali alkalmazásában

1. Futtasd az első parancsot a terminálban a piactér hozzáadásához.
2. Indítsd újra a ChatGPT asztali alkalmazását, és válaszd a **Codex** nézetet.
3. A **Plugins** lapon keresd meg és telepítsd a **Közérthetőség magyarul** plugint.

Telepítés után nyiss új beszélgetést a Codexben, illeszd be a szöveget, és kérd például ezt: „Nézd át közérthetőség szempontjából ezt a levelet. Lakossági ügyfélnek megy.”

Közvetlenül is telepítheted a skillt. Másold a repó teljes belső `kozerthetoseg-hu/` mappáját a `~/.agents/skills/` mappába (személyes használatra) vagy a projekt `.agents/skills/` mappájába. Ezután nyiss új beszélgetést a Codexben.

### ChatGPT Work

Ha a ChatGPT-munkaterületeden elérhető a skillek feltöltése, a skillt közvetlenül is kipróbálhatod:

1. Tömörítsd ZIP-fájlba a repó teljes belső `kozerthetoseg-hu/` mappáját a `SKILL.md`-vel és a mellette lévő fájlokkal együtt.
2. A ChatGPT-ben nyisd meg a **Plugins** felület **Skills** lapját, majd válaszd a **Create → Upload from your computer** lehetőséget, és töltsd fel a ZIP-fájlt.
3. Nyiss egy új beszélgetést a **Work** nézetben, és a `@` menüből válaszd ki a skillt.

A mérőszkript futtatásához a Work környezetében is Python 3.11 vagy újabb verzió kell. [Az OpenAI útmutatója a skillek feltöltéséhez](https://help.openai.com/en/articles/20001066-skills-in-chatgpt)

### Más, az Agent Skills szabványt követő eszköz

Add hozzá a mappát az eszköz leírása szerint. A skill nem függ a Claude-tól.

### Csak a mérőszkript, asszisztens nélkül

```
python kozerthetoseg-hu/scripts/meres.py levél.md
```

Dokumentációs CI-ben: a `--max-jelzes 0 --szint magas` kapcsolókkal a szkript 1-es kóddal lép ki, ha magas súlyosságú jelzést talál.

### Mi kell a szkriptekhez?

Python 3.11 vagy újabb kell, külső csomag és internet nem. A HuSpaCy nem kötelező; ha telepítve van, a `meres.py --huspacy` a mondatszerkezet mélységét és a beágyazott tagmondatokat is méri.

## Mire épül a tudásbázis?

A tudásbázis 17 nyilvános forrásra épül. Ezek közül öt gyakorlati útmutató az elsődleges, ezeket fejezetről fejezetre leltároztuk. A többi forrás a jogi modult, a szövegtípusok kezelését és a mérés korlátait alapozza meg.

A források minden szabálya, ajánlása és példája egy-egy leltártétel, saját szavakkal, oldalszámmal. Minden tétel vagy egy szabályhoz tartozik, vagy egy referenciafájl adott pontjához, vagy indoklással ki van hagyva.

Ha két forrás ellentmond egymásnak, például a mondathossz küszöbén, a szabály kimondja, melyiket követi a skill és miért.

A forrásokból a skill nem vesz át szövegrészt. A mintázatot veszi át, a példákat maga írja.

### A felhasznált források

A „Tétel” oszlop azt mutatja, hány szabály, ajánlás, tilalom vagy példa került a forrásból a leltárba. Összesen 467 tétel.

#### Elsődleges útmutatók

| Forrás | Mire használja a skill | Tétel | Elérés |
|---|---|---|---|
| Világos Beszéd: Hogyan írjunk közérthetően? Kisokos. Budapest Főváros Főpolgármesteri Hivatal, 2025. | A szabálykatalógus gerince: felépítés, megfogalmazás, kinézet, nyomtatványok. | 51 | [PDF](https://budapest.hu/api/file/doc/hogyan-irjunk-kozerthetoen-kisokos.pdf) |
| Világos Beszéd: Hogyan írjunk közérthetően? Kézikönyv. Budapest Főváros Főpolgármesteri Hivatal, 2025. | A kisokos szabályainak indoklása és példái, ellenőrző lista, közérthető szótár. | 125 | [PDF](https://budapest.hu/api/file/doc/hogyan-irjunk-kozerthetoen-kezikonyv.pdf) |
| NAV: Az érthető hivatal 1. Nemzeti Adó- és Vámhivatal, 2024. | Hogyan vezeti be egy hivatal a közérthető írást: ellenőrzés, sablonok, a szövegtípusok elhatárolása. | 38 | [NAV](https://nav.gov.hu/kiadvanyok/kozerthetosegi-program) |
| NAV: Az érthető hivatal 2. Nemzeti Adó- és Vámhivatal, 2024. | Gyakorlati fogások hivatali szöveghez: felépítés, szerkezetek, szavak, számok, írásjelek, táblázatok. | 83 | [NAV](https://nav.gov.hu/kiadvanyok/kozerthetosegi-program) |
| Európai Bizottság, Fordítási Főigazgatóság: A pontos fogalmazás művészete. Az Európai Unió Kiadóhivatala, 2013. | Tervezés, az olvasó szempontja, mondat- és szóhasználat, rövidítések, ellenőrzés. | 53 | [doi:10.2782/56340](https://doi.org/10.2782/56340) |

#### Tanulmányok

| Forrás | Mire használja a skill | Tétel | Elérés |
|---|---|---|---|
| Horváth Péter: Mitől közérthető és tömör egy jogi szöveg? Jog–Állam–Politika 13 (2021) 1, 103–113. | Jogi szöveg tömörítése; mikor kell szakszó a köznyelvi szó helyett. | 27 | [PDF](https://jap.sze.hu/images/lapsz%C3%A1mok/2021/1/JAP_2021_01_horvath-peter.pdf) |
| Balogh Dorka: Jogi szövegtípusok és közérthetőség. Glossa Iuridica 10 (2023) 3, 177–196. | A jogi szövegtípusok, és hogy melyikben mit szabad átírni. | 26 | [doi:10.55194/GI.2023.3.10](https://doi.org/10.55194/GI.2023.3.10) |
| Gerencsér Balázs Szabolcs: Közérthető jogi nyelv (plain language): alkalmazható-e az eredeti modell a mai magyar törvényalkotásban? Parlamenti Szemle 8 (2023) 1, 7–18. | A kötelező és a tájékoztató szöveg elválasztása; olvasói próba 6–9 fővel. | 15 | [Szakcikk Adatbázis](https://szakcikkadatbazis.hu/doc/3232914) |
| Üveges István: Sentence-level detection of Hungarian plain language with feature-guided augmentation. Language and Cognition 18 (2026), e16. | A mérőszkript korlátai: mit árulnak el a felszíni jegyek a közérthetőségről. | 6 | [doi:10.1017/langcog.2026.10066](https://doi.org/10.1017/langcog.2026.10066) |

#### Iránymutatások

| Forrás | Mire használja a skill | Tétel | Elérés |
|---|---|---|---|
| A 29. cikk szerinti adatvédelmi munkacsoport: Iránymutatás az (EU) 2016/679 rendelet szerinti átláthatóságról (WP260 rev.01), 2018. | Adatkezelési tájékoztató: világos nyelv, konkrét cél, határozatlan kifejezések kerülése. | 16 | [NAIH](https://www.naih.hu/files/wp260rev01_hu.pdf) |
| Inclusion Europe: Információ mindenkinek. A könnyen érthető kommunikáció európai alapelvei, 2012. | A KÉK-határ: mikor kell könnyen érthető szöveg a közérthető helyett. | 9 | [PDF](https://easy-to-read.inclusion-europe.eu/wp-content/uploads/2014/12/HU_Information_for_all.pdf) |

#### Jogszabályok és bírósági döntés

| Forrás | Mire használja a skill | Tétel | Elérés |
|---|---|---|---|
| 61/2009. (XII. 14.) IRM rendelet a jogszabályszerkesztésről (Jszr.) | Egy fogalom, egy kifejezés; az „illetve” és az „illetőleg” jogi szövegben. | 9 | [NJT](https://njt.jog.gov.hu/jogszabaly/2009-61-20-1U) |
| 2010. évi CXXX. törvény a jogalkotásról (Jat.) | A jogszabály legyen egyértelműen értelmezhető. | 1 | [Jogtár](https://net.jogtar.hu/jogszabaly?docid=a1000130.tv) |
| 2017. évi CLI. törvény az adóigazgatási rendtartásról (Air.) | A közérthetőség mint az adóhatóság alapelve. | 2 | [Jogtár](https://net.jogtar.hu/jogszabaly?docid=a1700151.tv) |
| 2013. évi V. törvény a Polgári Törvénykönyvről (Ptk.), 6:102–6:103. § | A szerződési kikötés legyen világos és érthető. | 3 | [Jogtár](https://net.jogtar.hu/jogszabaly?docid=a1300005.tv) |
| (EU) 2016/679 rendelet (GDPR), 12. cikk | Tömör, átlátható, érthető tájékoztatás az adatkezelésről. | 1 | [EUR-Lex](https://eur-lex.europa.eu/legal-content/HU/TXT/HTML/?uri=CELEX:32016R0679) |
| Az Európai Unió Bírósága, C-26/13. sz. ügy (Kásler és Káslerné Rábai), 2014. | Mit jelent az „érthető”: a fogyasztó előre látja a kikötés következményeit. | 2 | [EUR-Lex](https://eur-lex.europa.eu/legal-content/HU/TXT/HTML/?uri=CELEX:62013CJ0026) |

A teljes bibliográfiai adatok, a felhasználási feltételek és tételenként a leltár: [forrasok.md](kozerthetoseg-hu/references/forrasok.md). A szabálykatalógus: [szabalyok.md](kozerthetoseg-hu/references/szabalyok.md). Melyik tétel hová került: [lefedettseg.md](kozerthetoseg-hu/references/lefedettseg.md).

## Mit nem tud?

- Nem ad jogi tanácsot. Jogi szövegnél a jogi tartalom változatlanságáért a szakember felel.
- Kötelező szöveget (jogszabályt, előírt formulát, kamarai egységes szöveget) nem ír át, csak jelzi, hogy kötelező.
- A mérőszám jelzés, nem ítélet. A felszíni jegyekből nem dönthető el megbízhatóan, hogy egy mondat közérthető-e. Üveges (2026) magyar hivatali szövegeken az erre épített gépi modell F1 = 0,58 eredményt ért el; az 1 jelentené a hibátlan felismerést.
- Könnyen érthető (KÉK) szöveget nem készít. A KÉK értelmi fogyatékossággal élő vagy alacsony nyelvi kompetenciájú olvasóknak szól, és más szabályokat követ. A skill felismeri, ha ilyen szöveg kell, és jelzi.
- Nem pótolja az olvasói próbát.

## Hogyan bővíthetem?

Új forrás felvétele öt lépés:

1. Forrásrekord: a bibliográfiai adatok és a felhasználási feltétel.
2. Leltár: fejezetről fejezetre minden szabály, ajánlás, tilalom és példa, oldalszámmal, saját szavakkal.
3. Összevonás: ha egy tétel meglévő szabályt mond ki, ahhoz a szabályhoz kapcsolódik; az ellentmondás külön bejegyzést kap.
4. Leképezés: minden tétel célt kap (szabály, referencia vagy indokolt kihagyás).
5. Példák: a skill a mintázatot veszi át, nem a szöveget.

A szkriptek ezt adatfelvitellé teszik, az ellenőrzés gépileg mutatja meg, hogy semmi nem maradt ki. A parancssorok és az új szabály vagy parancs felvétele: [CONTRIBUTING.md](CONTRIBUTING.md).

### Miért így épül fel? (fejlesztőknek)

- Az adat és a szöveg külön van. A szabályok és a források TOML-fájlokban élnek, a `references/` Markdown-fájljait szkript generálja belőlük. Egy új forrás felvétele így adatfelvitel, és a lefedettség gépileg ellenőrizhető.
- A TOML-t a Python 3.11 óta a standard könyvtár olvassa, a skill futtatásához nem kell külső csomag. A JSON Schema fájlok dokumentálják a mezőket; az ellenőrzés külső függőség nélkül validál.
- Minden adat a skill mappáján belül van, ezért a skill bárhová telepítve önálló, és a bővítés telepítés után is működik.

## Licenc és hivatkozás

A kód (szkriptek, tesztek, CI) az MIT licenc alatt áll. A szöveges tartalom (szabályok, referenciák, dokumentáció) a [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.hu) licenc alatt áll. Áttekintés: [LICENSE](LICENSE); a licencek szövege: [LICENSE-MIT](LICENSE-MIT) és [LICENSE-CC-BY-4.0](LICENSE-CC-BY-4.0).

Ha hivatkozol a skillre, a [CITATION.cff](CITATION.cff) szerint tedd.

Szerző: Kis Zoltán ([github.com/zoltankis-arch](https://github.com/zoltankis-arch)). Biztonsági hibát a [SECURITY.md](SECURITY.md) szerint jelezz.

## Köszönet

A skill ezekre a munkákra épül; a hibák a skill hibái. Köszönet a források szerzőinek és kiadóinak:

- a Világos Beszédnek és Budapest Főváros Főpolgármesteri Hivatalának;
- a Nemzeti Adó- és Vámhivatal Közérthetőségi Programirodájának;
- az Európai Bizottság Fordítási Főigazgatóságának;
- Horváth Péternek, Balogh Dorkának, Gerencsér Balázs Szabolcsnak és Üveges Istvánnak;
- a 29. cikk szerinti adatvédelmi munkacsoportnak és az Inclusion Europe-nak.

## In English

kozerthetoseg-hu is an [Agent Skills](https://agentskills.io/specification) skill for checking and improving the plain-language quality of Hungarian texts such as official letters, notices, privacy notices, terms and conditions and administrative decisions. It has six commands: audit, rewrite with a fidelity check, surface metrics, a reader-test plan, adding a new source, and a consistency check. A separate legal module loads only for legal texts.

Every rule is traced to a public source with page numbers. The catalogue rests on a chapter-by-chapter inventory of five Hungarian and EU guides, plus supporting research and legislation. The skill gives no legal advice and does not rewrite mandatory texts. It treats metrics as signals, not verdicts, and it recognises but does not produce easy-to-read (KÉK) texts. The scripts need only Python 3.11+. Code: MIT; content: CC BY 4.0.
