# GDE Objektumorintentált szoftverfejlesztés VIZSGA 2023.11.30 16:00-19:00

Ez a 2023.11.30-i vizsga feladat
A megoldásra 3 órátok van. A vizsga 16:00-19:00-ig tart.
A github-on lévő utolsó commit nem lehet 19:00 után. Csak az azelőtti utolsó commmit-ot veszem figyelembe az értékelésnél.


## Általános elvárások
- Pythonban készítsétek a vizsgafeladatot
- a "tesztkerdesek.txt"-t töltsétek le, és tegyétek bele a Python projektetekbe
- a "tesztkerdesek.txt"-ben töltsétek ki a neveteket, szakotokat és neptun kódotokat, ílletve írjátok be a helyes válaszokat
- kész projektet osszátok meg a saját github repositorytokba PUBLIC-ra
- 3 órátok van a feladat megoldására, és github-ra való push-olására
- hogy biztos legyen, a végén egy browser incognito ablakában nézzétek meg az elküldendő github repositoryt (látható, fent van az utolsó commit is)
- a feladat elvégzése végén küldjétek el nekem email-ben a boga.aron@gde.hu címre a github repositorytok url-jét



## 1. A tesztkérdések (35%)

A válasz helyre írjátok be a helyes választ. Jó válasz 1 pont, rossz válasz -1 pont, nincs válasz 0 pont.

## 2. Programozási feladat (65%)

A feladat során egy egyszerű szálloda szobafoglalási rendszert kell megvalósítani Pythonban. 
A rendszernek képesnek kell lennie szobák kezelésére, foglalások kezelésére, létrehozására és lemondására, valamint a foglalások listázására.


### Feladatok

#### Osztályok Létrehozása 

- Hozz létre egy Szoba absztrakt osztályt, amely alapvető attribútumokat definiál (ár, szobaszám). (5 pont)
- Hozz létre az Szoba osztályból EgyagyasSzoba és KetagyasSzoba származtatott osztályokat, amelyek különböző attributumai vannak, és az áruk is különböző.(5 pont)
- Hozz létre egy Szalloda osztályt, ami ezekből a Szobákból áll, és van saját attributuma is (név pl.) (10 pont)
- Hozz létre egy Foglalás osztályt, amelybe a Szálloda szobáinak foglalását tároljuk (elég itt, ha egy foglalás csak egy napra szól) (10 pont)

#### Foglalások Kezelése

- Implementálj egy metódust, ami lehetővé teszi szobák foglalását dátum alapján, visszaadja annak árát. (15 pont)
- Implementálj egy metódust, ami lehetővé teszi a foglalás lemondását. (5 pont)
- Implementálj egy metódust, ami listázza az összes foglalást. (5 pont)

#### Felhasználói Interfész és adatvalidáció
- Készíts egy egyszerű felhasználói interfészt, ahol a felhasználó kiválaszthatja a kívánt műveletet (pl. foglalás, lemondás, listázás). (20 pont)

- A foglalás létrehozásakor ellenőrizd, hogy a dátum érvényes (jövőbeni) és a szoba elérhető-e akkor. (10 pont)
- Biztosítsd, hogy a lemondások csak létező foglalásokra lehetségesek. (5 pont)
- Töltsd fel az futtatás után a rendszert 1 szállodával, 3 szobával és 5 foglalással, mielőtt a felhasználói adatbekérés megjelenik. (10 pont)

Jó munkát! Légyszi önálló munkában, internettel...