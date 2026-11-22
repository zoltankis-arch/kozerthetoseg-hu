# kozerthetoseg-hu

[![Ellenőrzés](https://github.com/zoltankis-arch/kozerthetoseg-hu/actions/workflows/ellenorzes.yml/badge.svg)](https://github.com/zoltankis-arch/kozerthetoseg-hu/actions/workflows/ellenorzes.yml)
[![Verzió](https://img.shields.io/badge/verzi%C3%B3-1.4.0-blue)](CHANGELOG.md)
[![Licenc: MIT és CC BY 4.0](https://img.shields.io/badge/licenc-MIT%20%2B%20CC%20BY%204.0-green)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-specifik%C3%A1ci%C3%B3-informational)](https://agentskills.io/specification)

Agent Skill, amely magyar szövegek közérthetőségét vizsgálja és javítja, forrásokkal alátámasztva.

Hivatali levelet, tájékoztatót, adatkezelési tájékoztatót, ÁSZF-et vagy határozatot néz át, és közérthetőbbre írja. Minden javaslata egy szabályra épül, minden szabály nyilvános forrásra, oldalszámmal. A vizsgálat keretét az ISO 24495-1 szabvány négy kérdése adja. Jogi tanácsot nem ad, és kötelező szöveget (jogszabályt, előírt formulát) nem ír át.

> In English: an [Agent Skills](https://agentskills.io/specification) skill that checks and rewrites Hungarian texts in plain language. Every rule is traced to a public source with page numbers. It gives no legal advice and does not rewrite mandatory texts. Code: MIT; content: CC BY 4.0.

## Hogyan telepítem?

A skill a repó `kozerthetoseg-hu/` mappája.

- claude.ai: töltsd le a repót ZIP-ben, a belső `kozerthetoseg-hu` mappát tömörítsd újra, és töltsd fel a beállításokban, a skillek között.
- Claude Code:

  ```
  git clone https://github.com/zoltankis-arch/kozerthetoseg-hu
  cp -r kozerthetoseg-hu/kozerthetoseg-hu ~/.claude/skills/
  ```

- Codex:

  ```
  codex plugin marketplace add zoltankis-arch/kozerthetoseg-hu
  codex plugin add kozerthetoseg-hu@kozerthetoseg-hu
  ```

A ChatGPT asztali alkalmazása, a ChatGPT Work és más eszközök lépései: [docs/telepites.md](docs/telepites.md). A szkriptekhez Python 3.11 vagy újabb kell, külső csomag nem.

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
python kozerthetoseg-hu/scripts/meres.py levél.md --max-jelzes 0 --szint magas
```

## Mire épül?

83 szabályra (K001–K083) és 17 nyilvános forrásra. Az öt elsődleges útmutató: a Világos Beszéd kisokosa és kézikönyve, a NAV két kötete és az EU „A pontos fogalmazás művészete”. Mellettük tanulmányok, iránymutatások és jogszabályok. A forrásokból a skill nem vesz át szövegrészt, csak a mintázatot.

A teljes forráslista linkekkel: [docs/forrasok.md](docs/forrasok.md). A skill-lel és nélküle futtatott tesztek eredménye: [eredmenyek/](eredmenyek/iteracio-2/osszesites.md).

## Hogyan járulhatok hozzá?

Hibát, szabályjavaslatot vagy új forrást az [Issues](https://github.com/zoltankis-arch/kozerthetoseg-hu/issues) oldalon jelezhetsz. Pull requestet szívesen fogadunk. A lépések: [CONTRIBUTING.md](CONTRIBUTING.md). Köszönet a források szerzőinek és kiadóinak.

## Licenc

A kód MIT, a szöveges tartalom [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.hu) licenc alatt áll (`MIT AND CC-BY-4.0`, részletek: [LICENSE](LICENSE)). © 2026 Kis Zoltán. Hivatkozás: [CITATION.cff](CITATION.cff).
