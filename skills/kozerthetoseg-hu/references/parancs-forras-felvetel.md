# Parancs: `forras-felvetel`

Új forrásanyagot dolgoz fel öt lépésben (forrásrekord, leltár, összevonás, leképezés, példák), utána újragenerálja a referenciákat, lefuttatja az ellenőrzést, és javaslatot tesz a verzióemelésre.

## Mikor kell

Ha a hívó új közérthetőségi forrást (útmutatót, tanulmányt, jogszabályt, bírósági döntést) akar a skill tudásbázisába felvenni, vagy egy meglévő forrás új kiadását akarja feldolgozni.

A parancs a skill telepített példányában is működik, mert minden adat és szkript a skill mappájában van. Ha a skill csak olvasható helyre van telepítve, a hívó a repó klónjában futtassa.

## Bemenet

- A forrás szövege (PDF, weboldal vagy beillesztett szöveg) és bibliográfiai adatai.
- A forrás prioritása: A (szabály alapja), B (háttér, indoklás, mérés) vagy C (kitekintés).
- Elhagyható: hogy teljesen vagy csak részben kell feldolgozni; részleges feldolgozásnál a fejezetek listája.

PDF-nél olvasd ki a szöveget és a tartalomjegyzéket; ha egy oldal szkennelt kép, raszterizáld és nézd meg. Táblázatot és ábrát ne hagyj ki.

## Lépések

1. Forrásrekord. Hozd létre a fájlt:

   ```
   python scripts/uj_forras.py kiado-rovidcim-ev --cim "A forrás címe" --kiado "Kiadó" --ev 2026 --url https://... --prioritas A
   ```

   Töltsd ki a KITÖLTENDŐ mezőket: rövid név, szerző, teljes hivatkozás, licenc vagy felhasználási feltétel (ha nincs kimondva, írd be, hogy nincs feltüntetve), a feldolgozott kiadás, az oldalszámozás módja. Helyi elérési utat ne írj bele; a forrásra nyilvános URL-lel vagy bibliográfiai adattal hivatkozz.

2. Forrásleltár. Vedd fel a forrás tartalomjegyzékének minden fejezetét (`[[fejezet]]`), majd fejezetről fejezetre minden szabályt, ajánlást, ellenőrzőlista-pontot, tilalmat és előtte–utána példát (`[[tetel]]`), oldalszámmal, saját szavaiddal. Egy tétel egy állítás vagy egy egynemű példacsoport (például egy cseretáblázat, a párok számával). A következő szabad tételazonosító:

   ```
   python scripts/uj_forras.py --kovetkezo-tetel kiado-rovidcim-ev
   ```

   Ha egy fejezetből egy tétel sem kerül be, a `tetel_nelkul` mezőben indokold.

3. Összevonás. Ha a tételt már egy meglévő szabály kimondja, ne hozz létre újat: a tétel arra a szabályra mutasson, és a szabály `forrasok` listájába is vedd fel. Ha a tétel ellentmond egy meglévő forrásnak (például más küszöböt ad), a szabályba írj `[[elteres]]` bejegyzést: mit mond az egyik, mit a másik, mit követ a skill és miért. Új szabályhoz:

   ```
   python scripts/uj_szabaly.py --cim "A szabály címe" --csoport mondat
   ```

4. Leképezés. Minden tételnek pontosan egy célja legyen: `szabalyok = ["K0xx"]`, `referencia = "references/fajl.md#horgony"` vagy `kihagyva = "egy mondat indoklás"`.

5. Példák. A forrás előtte–utána párjaiból a mintázatot vedd át, ne a szöveget. A szabály `[pelda]` mezőjébe saját példa kerül. Rövid, hivatkozott idézet akkor megengedett, ha a példa enélkül nem érthető; ha a forrás licence nincs kimondva, nagyobb szövegrészt ne vegyél át, mert a repó nyilvános.

6. Generálás és ellenőrzés:

   ```
   python scripts/generalas.py
   python scripts/ellenorzes.py
   ```

   Addig javíts, amíg az ellenőrzés zöld.

7. Verzió. Új forrás vagy új szabály: minor emelés (1.0.0 → 1.1.0) az `assets/adatok/katalogus.toml`-ban és a SKILL.md `metadata` mezőiben; bejegyzés a CHANGELOG.md-ben. Megfogalmazás-javítás: patch; szabály visszavonása: major.

## Kimenet formája

Rövid jelentés:

1. A létrehozott forrásfájl neve és a tételek száma, típusonként.
2. A leképezés összesítése: szabályba (ebből összevont), referenciába, kihagyva.
3. Új szabályok és új eltérésbejegyzések listája.
4. Fejezetek tétel nélkül, indoklással.
5. Az `ellenorzes.py` eredménye.
6. A javasolt verzióemelés és a CHANGELOG-bejegyzés szövege.

## Mit nem csinál

- Nem pótol emlékezetből olyan forrást, amelyet nem ért el; ezt a jelentés kimondja.
- Nem vesz át nagyobb szövegrészt a forrásból.
- Nem töröl szabályt: a meghaladott szabályt visszavonja (`allapot = "visszavont"`, `utod = "K0xx"`).

## Példa

Bemenet: egy kétoldalas, kitalált „Mintaváros levélírási lapja”, amely három szabályt ad (fő üzenet elöl, mondat legfeljebb 18 szó, „amennyiben” helyett „ha”).

Kimenet: `mintavaros-levelirasi-lap-2026.toml`, egy fejezet, három tétel, mindhárom meglévő szabályba összevonva (K002, K020, K036). A K020-ba új eltérésbejegyzés kerül: a lap 18 szavas felső határt ad, a skill továbbra is az átlagot követi. Ellenőrzés: zöld. Javaslat: 1.0.0 → 1.1.0.
