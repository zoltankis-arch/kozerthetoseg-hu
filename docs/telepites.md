# Telepítés

A repó egy [Agent Plugins](https://agent-plugins.org/) 1.0.0 szerinti plugin. A gyökérben a `plugin.json` manifest van, a skill a `skills/kozerthetoseg-hu/` mappában. Az ezt a szabványt ismerő eszköz a repó gyökeréből pluginként telepíti; a többinél a skill mappáját kell átmásolni.

## Claude pluginként (ajánlott)

A repó Claude-piactér is (`.claude-plugin/marketplace.json`).

- Asztali alkalmazás, Cowork, claude.ai: Customize, Plugins, Add marketplace, majd `zoltankis-arch/kozerthetoseg-hu`, végül Install a „Közérthetőség magyarul” pluginnál.
- Claude Code: `/plugin marketplace add zoltankis-arch/kozerthetoseg-hu`, majd `/plugin install kozerthetoseg-hu@kozerthetoseg-hu`.

## Csak a skill, ZIP-feltöltéssel (claude.ai)

Ha nem pluginként, hanem önálló skillként szeretnéd:

1. Töltsd le a repót: a GitHubon a zöld Code gomb, majd Download ZIP.
2. Csomagold ki. A kicsomagolt `kozerthetoseg-hu-main` mappában a `skills/kozerthetoseg-hu` mappa a skill.
3. Ezt a mappát tömörítsd ZIP-be.
4. Töltsd fel a beállításokban, a skillek között.

## Csak a skill, Claude Code-ba másolva

```
git clone https://github.com/zoltankis-arch/kozerthetoseg-hu
cp -r kozerthetoseg-hu/skills/kozerthetoseg-hu ~/.claude/skills/
```

## Codex

A plugint a Codex CLI-vel vagy a ChatGPT asztali alkalmazásának Codex nézetében telepítheted. Az alábbi két útmutató első lépése a piactér hozzáadása a terminálban.

### Telepítés a Codex CLI-vel

Futtasd ezt a két parancsot a terminálban:

```sh
codex plugin marketplace add zoltankis-arch/kozerthetoseg-hu
codex plugin add kozerthetoseg-hu@kozerthetoseg-hu
```

### Telepítés a ChatGPT asztali alkalmazásában

1. Futtasd az első parancsot a terminálban a piactér hozzáadásához.
2. Indítsd újra a ChatGPT asztali alkalmazását, és válaszd a **Codex** nézetet.
3. A **Plugins** lapon keresd meg és telepítsd a **Közérthetőség magyarul** plugint.

Telepítés után nyiss új beszélgetést a Codexben, illeszd be a szöveget, és kérd például ezt: „Nézd át közérthetőség szempontjából ezt a levelet. Lakossági ügyfélnek megy.”

Közvetlenül is telepítheted a skillt. Másold a repó `skills/kozerthetoseg-hu/` mappáját a `~/.agents/skills/` mappába (személyes használatra) vagy a projekt `.agents/skills/` mappájába. Ezután nyiss új beszélgetést a Codexben.

## ChatGPT Work

Ha a ChatGPT-munkaterületeden elérhető a skillek feltöltése, a skillt közvetlenül is kipróbálhatod:

1. Tömörítsd ZIP-fájlba a repó `skills/kozerthetoseg-hu/` mappáját a `SKILL.md`-vel és a mellette lévő fájlokkal együtt.
2. A ChatGPT-ben nyisd meg a **Plugins** felület **Skills** lapját, majd válaszd a **Create → Upload from your computer** lehetőséget, és töltsd fel a ZIP-fájlt.
3. Nyiss egy új beszélgetést a **Work** nézetben, és a `@` menüből válaszd ki a skillt.

A mérőszkript futtatásához a Work környezetében is Python 3.11 vagy újabb verzió kell. Részletek: [az OpenAI útmutatója a skillek feltöltéséhez](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

## Más, az Agent Plugins vagy az Agent Skills szabványt követő eszköz

Agent Plugins esetén a repó gyökerét add meg pluginként; Agent Skills esetén a `skills/kozerthetoseg-hu/` mappát, az eszköz leírása szerint. A skill nem függ a Claude-tól.

## Mi kell a szkriptekhez?

Python 3.11 vagy újabb kell, külső csomag és internet nem. A HuSpaCy nem kötelező; ha telepítve van, a `meres.py --huspacy` a mondatszerkezet mélységét és a beágyazott tagmondatokat is méri.
