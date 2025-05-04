
# Kursinio darbo ataskaita  iš objektinio programavimo


# Įvadas

## Apie ką šis projektas?

Tai yra transporto nuomos sistema, parašyta Python kalba, leidžianti ieškoti, nuomoti skirtingų tipų transporto priemones: (automobilius, motociklus, žemės ūkio technika, dviračius).

Sistema palaiko šias funkcijas:
- Transporto priemonių sąrašo įkėlimas
- Nuomos ir grąžinimo logika
- Įrašų saugojimas CSV faile
- Vienetų testavimas

###  Kaip paleisti bei naudotis programą?

1. Įsitikinkite, kad turite **Python 3.x** versiją.
2. Paleiskite `main.py` failą terminale: bash python main.py
3. ![](images/program.start.png)
4. Atidarius langą, ekrane pasirodys Transporto nuomos sistema su penkiais galimais pasirinkimais. Norėdami atlikti konkretų veiksmą (pvz., peržiūrėti transporto priemones ar išsinuomoti), įveskite atitinkamą skaičių nuo 1 iki 5 ir paspauskite Enter.

5. **Norėdami pamatyti, kokios transporto priemonės yra galimos nuomai, pirmiausia turite pasirinkti 1 – „Show all vehicles“.** Tik tada galėsite matyti siūlomų automobilių sąrašą ir priimti sprendimą dėl nuomos.
6. ![naudojimas](images/program.use.png)

6. **Kiekvienai transporto priemonei pateikiama ši informacija:  
– **Transporto tipas** (pvz., automobilis, motociklas),  
– **Identifikavimo numeris (ID)** – šio numerio programa prašys, kai norėsite atlikti nuomos ar atšaukimo veiksmą,  
– **Pagaminimo metai**,  
– **Spalva**,  
– **Variklio talpa (litrais)**,  
– **Papildoma informacija** – pavyzdžiui, ar transporto priemonė yra hibridinė, elektrinė ir pan.

Kai kuriais atvejais sistema gali __paprašyti papildomos informacijos__, pavyzdžiui, įvesti savo vardą – tai reikalinga nuomos ar atšaukimo veiksmams atlikti. Tokiu atveju tiesiog įrašykite savo vardą ir tęskite pagal pateiktas instrukcijas.


1. **Trumpas sistemos aprašymas:**
Ši sistema leidžia peržiūrėti visus galimus transporto pasirinkimus, ieškoti konkretaus automobilio pagal ID, išsinuomoti ar atšaukti nuomą bei išeiti iš programos.

2. **Kaip pasirinkti meniu punktą:**
    
	Skaičių reikia įrašyti tiksliai – pvz., norėdami išsinuomoti transporto priemonę, įveskite skaičių 3 ir paspauskite Enter.
    
3. **Ką daryti, jei įvedate neteisingą reikšmę:**
    
	Jei įvesite neteisingą pasirinkimą (pvz., raidę arba skaičių, kurio nėra meniu), sistema parodys klaidos pranešimą ir paprašys įvesti iš naujo.
    
4. **Išsamesnė informacija apie vardo įvedimą:**
    
	Kai kurios funkcijos (pvz., nuoma ar atšaukimas) gali paprašyti įvesti jūsų vardą, kad būtų galima identifikuoti naudotoją. Įrašykite jį tiksliai taip, kaip naudojote anksčiau, kad sistema jus atpažintų.
    
5. **Išėjimo instrukcija:**
    
	Norėdami išeiti iš sistemos, pasirinkite 5. Programa bus uždaryta automatiškai.
    
6. **Patarimas dėl patogumo:**
    
	Naudodami sistemą patogiausia dirbti pilnu ekranu, kad visos instrukcijos būtų aiškiai matomos.
    

# Analizė 
## Darbo įkėlimas naudojant Git ir GitHub

Projektas buvo valdomas naudojant versijų kontrolės sistemą **Git**. Sukūrus vietinę saugyklą, programos failai bei dokumentacija (Markdown formato failas) buvo įkelti į **GitHub** platformą, kuri pasirinkta kaip nuotolinė saugykla darbui pateikti.

Į GitHub buvo įkelti šie failai:

- Programos pirminis kodas,
    
- Aprašomasis failas `README.md`, kuriame pateikta informacija apie programos veikimą, struktūrą bei naudojimo instrukcijos.


Abu failai buvo patalpinti **vienoje bendroje saugykloje**, užtikrinant aiškią struktūrą ir prieinamumą.

## Objektinio programavimo pamatai jų panaudojimas ir paaiškinimas

### Polimorfizmas

**Polimorfizmas** reiškia, kad ta pati metodo antraštė (pvz., `show_info()`) gali būti **įgyvendinta skirtingai** skirtingose klasėse. Tai leidžia įvairiai naudoti tą patį metodą, o elgesys priklauso nuo to, kokios konkrečios klasės objektas tą metodą kviečia.

![img](images/picture1.png) ![img](images/picture3.png) ![img](images/picture2.png)	


Programoje naudojamas **polimorfizmas**, kuris leidžia skirtingoms klasėms (`Car` ir `Motorcycle`) įgyvendinti bendrą metodą `show_info()` savaip. Abstraktuota bazinė klasė __Transport__ deklaruoja šį metodą kaip abstraktų, o paveldinčios klasės pateikia savo konkrečią informacijos atvaizdavimo logiką.

Tai leidžia visus transporto priemonių objektus (nesvarbu, ar tai automobilis, ar motociklas) laikyti viename sąraše ir kviesti `show_info()` metodą nežinant konkretaus objekto tipo. Kiekviena klasė pati pasirūpina, kad būtų pateikta jai būdinga informacija.

Pateiktuose ekrano nuotraukose matyti, kaip kiekviena klasė (`Car` ir `Motorcycle`) turi savo `show_info()` metodo versiją, kuri gražiai suformatuoja ir pateikia visą su objektu susijusią informaciją: markę, modelį, metus, spalvą, variklio tūrį bei papildomą informaciją.

### Abstrakcija

Abstrakti klasė – tai tarsi šablonas būsimiems objektams, kuris apibrėžia, kokie metodai ar savybės privalo būti klasėse, paveldinčiose iš jos. Ji neskirta kurti tiesioginius objektus, o naudojamas kaip pagrindas, pamatas (šablonas), pagal kurį kuriamos konkrečios klasės.

Galima sakyti, kad tai „klasės šablonas“, kuriame suplanuojama, ką turės paveldinčios klasės, tačiau pats abstraktus metodas (pvz., show_info()) dar neturi konkretaus įgyvendinimo.

![](images/abs.png)

Paveldėjimo pagalba konkrečios klasės (pvz., Car, Motorcycle) perima bendrus bruožus iš abstrakčios klasės (pvz., Transport) ir pačios įgyvendina trūkstamą logiką – šiuo atveju metodą show_info().

Naudojant @abstractmethod dekoratorių, užtikrinama, kad bazinėje klasėje Transport metodas show_info() neturi konkretaus įgyvendinimo – tai paliekama paveldinčioms klasėms, tokioms kaip Car ar Motorcycle. Kiekviena iš jų pateikia savo informacijos atvaizdavimo logiką, tačiau bendru atveju išlieka vienoda.

Norint naudoti abstrakčias klases ir metodus, programos pradžioje atliekamas reikiamų modulių importas:

from abc import ABC, abstractmethod
Šis importas leidžia paveldėti iš ABC (Abstract Base Class) ir naudoti @abstractmethod žymėjimą.

Šis abstrakcijos principas leidžia:

Sutalpinti bendrą logiką vienoje vietoje, išvengiant pasikartojimo;
Užtikrinti struktūros vientisumą – visos transporto priemonės turės show_info() metodą;Lengvai išplėsti sistemą pridedant naujus transporto tipų klasės (pvz., Truck, Car, neprarandant suderinamumo su jau egzistuojančia logika.
Ekrano nuotraukoje parodyta, kaip sukuriama ši bazinė abstrakti klasė Transport bei abstraktus metodas show_info() – tai esminis žingsnis struktūrizuojant programą pagal OOP principus.

### Paveldėjimas
Paveldėjimas – tai objektinio programavimo principas, leidžiantis vienai klasei (pvz., Car) perimti savybes ir metodus iš kitos – bazinės klasės (pvz., Transport). Taip užtikrinamas kodo pakartotinis naudojimas ir leidžiama išplėsti esamą funkcionalumą, nekuriant visko iš naujo.

![](images/pav.png)

Klasė Car paveldi iš abstrakčios bazinės klasės Transport, kuri apibrėžia bendrus visoms transporto priemonėms požymius – tokius kaip id, brand ir model.
Naudojant super().__init__() metodą, paveldimi bendri atributai, o papildomi atributai, tokie kaip year, color, engine_capacity ir extra, pridedami Car klasėje.
Taip užtikrinamas kodo pakartotinio naudojimo principas – bendra logika laikoma bazinėje klasėje, o specifinė informacija aprašoma paveldinčiose klasėse.

### Inkapsuliacija
Inkapsuliacija – tai vidinių objekto duomenų apsaugojimas nuo tiesioginės prieigos iš išorės. Vietoj to siūloma naudoti metodus arba specialius „saugiklius“, kaip @property, kad būtų galima kontroliuoti:


- kaip tie duomenys pasiekiami,
- ar jie gali būti keičiami,
- ar reikalinga papildoma logika (pvz., validacija, logų rašymas ir t. t.).

![](images/ink.png)

![](images/ink2.png)


Metodai kaip:

**_is_vehicle_rented**

**_save_rental_record**

yra inkapsuliacijos pavyzdžiai, ir jų pavadinimai su pabraukimu (_) rodo, kad tai yra "protected" (saugomi, vidaus naudojimui skirti) metodai.

Klasėje naudojami metodai su pavadinimais, prasidedančiais pabraukimu (_), yra skirti vidiniam naudojimui – tai yra inkapsuliacijos požymis.
Tokie metodai, kaip _is_vehicle_rented ir _save_rental_record, slepia sudėtingą ar jautrią logiką nuo išorinio pasaulio, taip apsaugodami objekto būseną bei struktūrą.


Python'e prieigos lygiai nėra griežtai kontroliuojami, tačiau naudojami vardų žymėjimai (naming conventions), kurie padeda atskirti, kaip nariai turėtų būti naudojami:

####  Paprastesnis pavyzdys 

```python
class Transport:
    def __init__(self):
        self.public_var = "Visiems prieinama"
        self._protected_var = "Naudoti tik klasėje ar paveldėtojuose"
        self.__private_var = "Paslėpta (name mangling)"
```

| Žymėjimas       | Prieigos lygis | Aprašymas                                                                 |
|------------------|----------------|---------------------------------------------------------------------------|
| `public_var`     | **Public**     | Viešas – gali būti pasiekiamas ir keičiamas iš bet kur.                  |
| `_protected_var` | **Protected**  | Apsaugotas – nenaudoti iš išorės, bet pasiekiamas paveldinose klasėse.  |
| `__private_var`  | **Private**    | Privatus – paslėptas nuo išorinio naudojimo (atliekamas vardų maskavimas). |

# **Pasirinktas dizaino šablonas: Factory Method (Gamyklos metodas)**

![](images/design.png)

Sukurtas `VehicleFactory` klasės metodas `create_vehicle(...)`, kuris, pagal pateiktą transporto priemonės tipą (`"car"`, `"motorcycle"`, `"agricultural"`, `"non_motor"`), **grąžina atitinkamą objekto egzempliorių** (pvz., `Car`, `Motorcycle` ir t. t.).
Klientinis kodas nurodo tik transporto priemonės tipą, bet neturi žinoti konkrečios klasės ar jos kūrimo detalių.

Šis metodas atitinka Factory Method principą – **visa objektų kūrimo logika yra sutelkta vienoje vietoje**. Tai leidžia lengvai pridėti naujas transporto priemonių rūšis ar modifikuoti kūrimo procesą neliečiant kitų sistemos dalių.Šiame projekte pritaikytas **Factory Method** dizaino šablonas. Jo esmė – **sukurti objektus per atskirą metodą (vadinamą „fabriku“), o ne aprašant klases tiesiogiai programos logikoje**. Toks sprendimas leidžia atskirti objektų kūrimo logiką nuo jų naudojimo, taip padidinant sistemos lankstumą, testuojamumą ir plėtrą.

### **Kodėl šis šablonas tinkamiausias:**

- **Plėtra (Extensibility)**: Galima lengvai pridėti naujus transporto priemonių tipus papildant `create_vehicle` metodą, nekeičiat likusio kodo.
    
- **Atskyrimas (Decoupling)**: Klientinis kodas nepriklauso nuo konkrečių transporto klasių – jis tiesiog naudoja gamyklos metodą.
    
- **Atsakomybės paskirstymas**: `VehicleFactory` atsakinga tik už transporto priemonių kūrimą, o ne už jų veikimą.
    

### **Kodėl kiti šablonai netinka:**

- **Singleton** – naudojamas, kai reikia vieno bendro objekto, o čia kuriami skirtingi transporto priemonių objektai.
    
- **Abstract Factory** – reikalingas, kai kuriamos visos objektų grupės (šeimos), o čia pakanka vienetinių objektų kūrimo.
    
- **Builder** – skirtas labai sudėtingiems objektams su daug parametrų, o čia objektų kūrimas paprastesnis.
    
- **Prototype** – naudojamas klonuoti esamus objektus, o mūsų atveju objektai kuriami naujai.
    
- **Adapter / Decorator / Composite** – tai struktūriniai šablonai, labiau tinkami modifikuoti ar kombinuoti objektų elgseną, o ne juos kurti.

## Agregacija

Agregacija – tai toks ryšys tarp klasių, kai viena klasė „turi“ kitos klasės objektus, bet jie gali egzistuoti ir be jos. Kitaip tariant, tai kaip laikinas bendradarbiavimas: viena klasė naudoja kitą, bet nėra nuo jos priklausoma visiškai.
jeigu sunaikinsi vieną iš objektų, kitas liks neliestas.

![](images/ags.png)

Klasė `RentalManager` saugo transporto priemonių sąrašą per `vehicles` kintamąjį. Šios transporto priemonės nėra sukuriamos `RentalManager` viduje – jos perduodamos iš išorės (pavyzdžiui, sukurtos per `VehicleFactory`). Tai reiškia, kad `RentalManager` tiesiog **„priima“ jau sukurtus objektus ir su jais dirba**, bet **jų gyvenimo trukmės nekontroliuoja** – jei `RentalManager` ištrinsim, transporto priemonės vis tiek gali likti

Būtent dėl to šis ryšys ir vadinamas **agregacija** – klasė turi kitų objektų, bet nėra už juos atsakinga nuo pradžios iki galo.

## Darbas su duomenų failais(Skaitymas rašymas )


Šiame projekte duomenų saugojimui ir apdorojimui naudojami CSV (Comma-Separated Values) formato tekstiniai failai. Failai naudojami:

- Transporto priemonių informacijos saugojimui
- Nuomos įrašų registravimui ir tikrinimui

![](images/fail.png)

```python
with open(self.file_path, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
```

Nauji įrašai pridedami naudojant režimą `"a"` (append), kuris neištrina esamo turinio:
```python
with open(self.rental_file_path, "a") as file:
    file.write(record.to_csv_row() + "\n")
```
Failo perrašymui (kai norima pakeisti ar pašalinti įrašus) naudojamas režimas `"w"`:
```python
with open(self.rental_file_path, "w") as file:
    for line in lines:
        if not line.startswith(vehicle_id + ","):
            file.write(line)
``` 

| Režimas | Pavadinimas         | Aprašymas                                                                           |
| ------: | ------------------- | ----------------------------------------------------------------------------------- |
|   `"r"` | Read (skaitymas)    | Atidaro esamą failą skaitymui. Jei failas neegzistuoja – sukeliama klaida.          |
|   `"w"` | Write (rašymas)     | Sukuria naują failą arba perrašo esamą. Ištrina visą ankstesnį turinį.              |
|   `"a"` | Append (pridėjimas) | Atidaro failą priedui. Įrašai pridedami failo pabaigoje, neištrinant esamo turinio. |

# Išvada

- Sukūriau veikiančią programą, kuri leidžia registruoti ir valdyti transporto priemonių nuomą. Programa skaito ir rašo duomenis į CSV failus, todėl viskas išsaugoma net ir išjungus ją.
- Naudojau keturis objektinio programavimo principus – paveldėjimą, abstrakciją, inkapsuliaciją ir polimorfizmą. Tai padėjo kodą padaryti aiškesnį ir lengviau tvarkomą.
- Pritaikiau „Factory Method“ dizaino šabloną – jis labai praverčia, kai reikia kurti skirtingų tipų transporto priemones (pvz., automobilį ar motociklą) automatiškai pagal duomenis.
- Failų valdymas leido ne tik išsaugoti duomenis, bet ir juos filtruoti, ištrinti ar pridėti naujus – tai padarė programą praktišką naudoti.
- Projekte taip pat parodžiau, kaip veikia agregacija – pavyzdžiui, nuoma „priklauso“ transporto priemonei, bet jie abu egzistuoja atskirai.
- Šiuo metu, jeigu galvočiau apie programos tobulinimą, kyla kelios idėjos. Pirmiausia būtų naudinga išplėsti transporto priemonių duomenų bazę – pridėti daugiau laukų arba naujų transporto tipų. Taip pat galima būtų pagerinti duomenų atvaizdavimą, kad viskas ekrane atrodytų aiškiau ir tvarkingiau. Galiausiai, būtų labai naudinga įdiegti galimybę pasirinkti, kokia kalba veikia programa – tai padarytų ją patogesnę platesniam vartotojų ratui.