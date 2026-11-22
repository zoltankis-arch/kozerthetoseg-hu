# kozerthetoseg-hu

[![Ellenőrzés](https://github.com/zoltankis-arch/kozerthetoseg-hu/actions/workflows/ellenorzes.yml/badge.svg)](https://github.com/zoltankis-arch/kozerthetoseg-hu/actions/workflows/ellenorzes.yml)
[![Verzió](https://img.shields.io/badge/verzi%C3%B3-1.5.1-blue)](CHANGELOG.md)
[![Licenc: MIT és CC BY 4.0](https://img.shields.io/badge/licenc-MIT%20%2B%20CC%20BY%204.0-green)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-specifik%C3%A1ci%C3%B3-informational)](https://agentskills.io/specification)

Agent Skill, amely magyar szövegek közérthetőségét vizsgálja és javítja, forrásokkal alátámasztva.

Hivatali levelet, tájékoztatót, adatkezelési tájékoztatót, ÁSZF-et vagy határozatot néz át, és közérthetőbbre írja. Minden javaslata a 83 szabály (K001–K083) egyikére épül, minden szabály nyilvános forrásra, oldalszámmal. Jogi tanácsot nem ad, és kötelező szöveget (jogszabályt, előírt formulát) nem ír át.

A vizsgálat keretét az ISO 24495-1:2023 közérthetőségi szabvány négy elve adja. A skill mindegyiket kérdésként teszi fel a szövegnek:

1. Megkapja-e az olvasó, amire szüksége van? (releváns-e a tartalom)
2. Megtalálja-e? (felépítés, címek, kinézet)
3. Megérti-e? (mondat, szó, szerkezet)
4. Tudja-e használni? (teendő, határidő, segítség)

### Előtte és utána

Egy hatósági hiánypótlási felhívás egyetlen mondata, átírás előtt (37 szó):

> Fentiekre tekintettel felhívjuk, hogy a jelen felhívás kézhezvételétől számított 15 napon belül a hiányzó tervezői nyilatkozat benyújtására kerüljön sor, ellenkező esetben az eljárás a 2016. évi CL. törvény 47. § (1) bekezdés b) pontja alapján megszüntetésre kerül.

Átírás után:

> Az építési engedély iránti kérelméhez még egy irat hiányzik: a tervezői nyilatkozat. Nyújtsa be a levél kézhezvételétől számított 15 napon belül. Ha nem nyújtja be határidőre, megszüntetjük az eljárást (2016. évi CL. törvény 47. § (1) bekezdés b) pontja).

A teendő és a határidő a levél elejére került (K002, K003). A hosszú mondatból három rövid lett (K020), a „kerül”-szerkezetek helyére cselekvő ige (K043), a jogszabályhely a mondat végére (K012). Az átírás után a skill tételesen ellenőrizte, hogy a 15 nap, a kezdőnapja, a jogkövetkezmény és a jogszabályhely változatlan maradt. A teljes levél és a hűségtáblázat: [examples/hianypotlasi-felhivas/](examples/hianypotlasi-felhivas/).

### Milyen forrásokra épül?

A skill 17 nyilvános forrást dolgoz fel; az öt elsődleges útmutatót fejezetről fejezetre, összesen 467 tételben. Szövegrészt nem vesz át belőlük, csak a szabályt és a mintázatot.

- Útmutatók: Világos Beszéd, *Hogyan írjunk közérthetően?* kisokos és kézikönyv (Budapest Főváros, 2025); NAV, *Az érthető hivatal* 1. és 2. kötet (2024); Európai Bizottság, *A pontos fogalmazás művészete* (2013).
- Tanulmányok: Horváth Péter (2021) a jogi szöveg tömörségéről; Balogh Dorka (2023) a jogi szövegtípusokról; Gerencsér Balázs Szabolcs (2023) a plain language modellről a törvényalkotásban; Üveges István (2026) a közérthetőség gépi felismeréséről.
- Iránymutatások: az adatvédelmi munkacsoport WP260 iránymutatása az átláthatóságról (2018); az Inclusion Europe könnyen érthető kommunikációs alapelvei (2012).
- Jogszabályok és ítélet: Jat., Jszr., Air., Ptk. 6:102–6:103. §, GDPR 12. cikk, és az EU Bíróságának Kásler-ítélete (C-26/13).

Linkekkel és tételszámokkal: [docs/forrasok.md](docs/forrasok.md). A skill-lel és nélküle futtatott tesztek eredménye: [eredmenyek/](eredmenyek/iteracio-2/osszesites.md).

> In English: an [Agent Skills](https://agentskills.io/specification) skill that checks and rewrites Hungarian texts in plain language. Every rule is traced to a public source with page numbers. It gives no legal advice and does not rewrite mandatory texts. Code: MIT; content: CC BY 4.0.

## Hogyan telepítem?

A repó egyben plugin-piactér (marketplace) is, egyetlen pluginnal. A Claude és a Codex innen pluginként telepíti, a skill a `skills/kozerthetoseg-hu/` mappában van.

### Claude (asztali alkalmazás, Cowork, claude.ai)

1. A bal oldali sávban nyisd meg a Customize menüt, és válaszd a Plugins lapot.
2. Válaszd az Add marketplace lehetőséget, és add meg: `zoltankis-arch/kozerthetoseg-hu`.
3. A listában megjelenik a „Közérthetőség magyarul” plugin. Kattints az Install gombra.

A plugin a fiókodhoz kerül, így a csevegésben, a Coworkben és a Claude Code-ban is elérhető. Frissítés: a piactérnél a Check for updates, vagy a Sync automatically.

### Claude Code

```
/plugin marketplace add zoltankis-arch/kozerthetoseg-hu
/plugin install kozerthetoseg-hu@kozerthetoseg-hu
```

### Codex

```
codex plugin marketplace add zoltankis-arch/kozerthetoseg-hu
codex plugin add kozerthetoseg-hu@kozerthetoseg-hu
```

Más eszközök (ChatGPT, ZIP-feltöltés, az Agent Plugins vagy az Agent Skills szabványt követő kliensek): [docs/telepites.md](docs/telepites.md). A szkriptekhez Python 3.11 vagy újabb kell, külső csomag nem.

## Hogyan használom?

Írd az asszisztensnek, mit szeretnél, a szöveggel együtt. Például: „Nézd át közérthetőség szempontjából ezt a levelet. Lakossági ügyfélnek megy.” A parancsot nem kell megnevezned.

| Parancs | Mit csinál |
|---|---|
| `audit` | Jelentést ad: hol a gond, melyik szabályt sérti, miért baj az olvasónak, mi a javaslat, mennyire sürgős. |
| `atiras` | Átírja a szöveget, és ellenőrzi, hogy minden tény, szám, határidő és feltétel megmaradt-e. |
| `meres` | Felszíni mérés (mondathossz, „kerül”-szerkezetek, körülményes kifejezések), szabályhoz kötött jelzésekkel. |
| `proba` | Olvasói próbát tervez 6–9 fővel. |
| `forras-felvetel` | Új forrást vesz fel a tudásbázisba. |
| `ellenorzes` | Ellenőrzi, hogy a tudásbázis teljes és ellentmondásmentes. |

Egy `audit`-sor:

| Hol | Szabály | Mi a baj az olvasónak | Javaslat |
|---|---|---|---|
| „elbírálásra került” | K043 | Nem derül ki, ki döntött, és mi a döntés. | „Elbíráltuk a kérelmét: …” |

Előtte–utána példák: [examples/](examples/).

A mérőszkript asszisztens nélkül is fut, például dokumentációs CI-ben:

```
python skills/kozerthetoseg-hu/scripts/meres.py levél.md --max-jelzes 0 --szint magas
```

## Hogyan járulhatok hozzá?

Hibát, szabályjavaslatot vagy új forrást az [Issues](https://github.com/zoltankis-arch/kozerthetoseg-hu/issues) oldalon jelezhetsz. Pull requestet szívesen fogadunk. A lépések: [CONTRIBUTING.md](CONTRIBUTING.md). Köszönet a források szerzőinek és kiadóinak.

## Licenc

A kód MIT, a szöveges tartalom [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.hu) licenc alatt áll (`MIT AND CC-BY-4.0`, részletek: [LICENSE](LICENSE)). © 2026 Kis Zoltán. Hivatkozás: [CITATION.cff](CITATION.cff).
