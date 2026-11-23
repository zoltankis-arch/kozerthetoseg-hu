# Összehasonlító evalok

Generált fájl (tools/eval_osszesit.py); kézzel ne szerkeszd.

14 eval futott mindkét változatban: a skill-lel és nélküle, ugyanazzal a modellel.

| | Skill-lel | Skill nélkül |
|---|---|---|
| Teljesült elvárások | 61/62 (98%) | 22/62 (35%) |
| Vak bíráló szerint jobb | 14 | 0 |
| Magas és közepes jelzés 100 szóra az átírásokban (9 átírás) | 10,8 | 9,6 |

Döntetlen a vak bírálatban: 0.

## Mit nem mutatnak ezek a számok?

- Evalonként és változatonként egy futás van, ezért a különbség egy része véletlen lehet.
- Az elvárások egy része a skill saját fogalmaira épül (szabályazonosító, mérőszkript, jogi zárómondat). Ezeket az alapváltozat nem ismerheti, így az elvárásszám a skill javára torzít.
- A vak bíráló látta az elvárásokat, ezért az ítéletét ugyanez a torzítás érheti.
- A jelzésszám is a skill javára torzíthat, mert a skill ismeri a mérőszkriptet. Ha mégis a skill átírásainál magasabb, azt érdemes szövegenként megnézni.
- Ahol csak skill-lel futott az eval (például új forrás felvétele), ott nincs összevetés.

## Evalonként

| # | Eval | Típus | Skill-lel | Skill nélkül | Vak bíráló |
|---|---|---|---|---|---|
| 1 | ugyvedi szolgaltatasleiras audit | alap | 7/7 | 0/7 | skill-lel |
| 2 | adatkezelesi tajekoztato atiras | alap | 7/7 | 1/7 | skill-lel |
| 3 | hatosagi level hatarido | alap | 6/6 | 5/6 | skill-lel |
| 4 | aszf egyoldalu modositas | alap | 5/5 | 1/5 | skill-lel |
| 5 | jogszabaly nem irhato at | alap | 4/4 | 0/4 | skill-lel |
| 6 | kamarai egyseges formula | alap | 4/4 | 2/4 | skill-lel |
| 7 | kek hatar | alap | 3/3 | 0/3 | skill-lel |
| 8 | mar kozertheto szoveg | alap | 3/3 | 3/3 | skill-lel |
| 9 | angol szoveg | alap | 2/2 | 1/2 | skill-lel |
| 10 | forras felvetel mintaforras | alap | – | – | – |
| 11 | meres hatosagi level | alap | 3/4 | 0/4 | skill-lel |
| 12 | proba adatkezelesi tajekoztato | alap | 5/5 | 2/5 | skill-lel |
| 13 | nyomaspróba: rovidites kivetelekkel | nyomasproba | 5/5 | 4/5 | skill-lel |
| 14 | nyomaspróba: torvenyszoveg atirasa kerésre | nyomasproba | 3/3 | 0/3 | skill-lel |
| 15 | nyomaspróba: kitalalt hatarido | nyomasproba | 4/4 | 3/4 | skill-lel |
