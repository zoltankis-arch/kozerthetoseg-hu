# Forrásfelvétel jelentése: Mintaváros Önkormányzata, Levélírási lap (2026)

Feltételezések (nem tudtam kérdezni):
- A forrás teljes egészében feldolgozandó (egy oldal, egy fejezet).
- A lapnak nincs nyilvános URL-je, ezért a forrásrekordban nincs `url`; a bibliográfiai adat a kiadó, a cím és az év.
- A licenc a lap utolsó mondata: "A lap szabadon terjeszthető a forrás megjelölésével."
- A skill mappájába nem írtam. A munkát a skill másolatán végeztem (`eval-10/with_skill/work`), így a verzióemelést és a CHANGELOG-bejegyzést csak javaslom, nem vezettem át.

1. Létrehozott forrásfájl: `assets/adatok/forrasok/mintavaros-levelirasi-lap-2026.toml` (másolata az outputs mappában). Egy fejezet, 3 tétel, mind szabály típusú, prioritás A.

2. Leképezés: mind a 3 tétel meglévő szabályba lett összevonva, referenciába és kihagyásba egy sem.
   - #001, az első mondat mondja meg, miről szól a levél: K002 (a fő üzenet elöl).
   - #002, egy mondat legfeljebb 18 szó: K020 (mondathossz).
   - #003, "amennyiben" helyett "ha": K036 (egyszerűbb szó a körülményes helyett).

3. Új szabály nem készült. Új eltérésbejegyzés egy van, a K020-ban: a lap 18 szavas felső határt ad, a többi forrás 15–20 szavas átlagot vagy 20 szavas határt. A skill továbbra is az átlagot követi, mert a 18 szavas határ helyi belső szabály, és a felszíni szám önmagában nem dönti el az érthetőséget.

4. Fejezet tétel nélkül nincs.

5. Ellenőrzés: `generalas.py` lefutott. Az `ellenorzes.py` a helyesen elnevezett mappában zöld: "Rendben: 18 forrás, 470 leltártétel, 83 aktív és 0 visszavont szabály." A `work` nevű másolatban egyetlen hiba jelent meg, a mappanév és a `name` mező eltérése; ez csak a másolás mellékhatása.

6. Javasolt verzióemelés: minor, 1.3.0 → 1.4.0 az `assets/adatok/katalogus.toml`-ban és a SKILL.md `metadata` mezőiben (`version`, `forraskatalogus`). CHANGELOG-bejegyzés (a skill mappájában jelenleg nincs CHANGELOG.md):
   "1.4.0: új forrás, Mintaváros Önkormányzata: Levélírási lap (2026), A prioritás; 3 tétel a K002, K020 és K036 szabályba összevonva; új eltérésbejegyzés a K020-ban (18 szavas helyi felső határ)."

Megjegyzés: a bemenet kitalált mintaforrás. Ha valódi felvételre kerülne, a nyilvános kiadás URL-jét és az eredeti oldalszámozást érdemes pótolni.
