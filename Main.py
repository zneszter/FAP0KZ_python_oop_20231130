from datetime import datetime, timedelta
import Szalloda
import EgyagyasSzoba
import KetagyasSzoba




# Adatfeltöltés
szalloda = Szalloda.Szalloda("Zsolt Szállodája")

szalloda.szoba_hozzaadas(EgyagyasSzoba.EgyagyasSzoba(101, 8000, "Ingyenes reggeli"))
szalloda.szoba_hozzaadas(KetagyasSzoba.KetagyasSzoba(201, 12000, "Tengerre néző kilátás"))
szalloda.szoba_hozzaadas(EgyagyasSzoba.EgyagyasSzoba(301, 10000, "Ingyenes parkolás"))

szalloda.foglalas(101, datetime(2023, 12, 1))
szalloda.foglalas(201, datetime(2023, 12, 5))
szalloda.foglalas(301, datetime(2023, 12, 10))
szalloda.foglalas(101, datetime(2023, 12, 15))
szalloda.foglalas(201, datetime(2023, 12, 20))

# Felhasználói interfész
while True:
    print("\n1. Szabad szobák listázása")
    print("2. Foglalás")
    print("3. Lefoglalt szobák listázása")
    print("4. Lemondás")
    print("0. Kilépés")

    valasztas = input("Válasszon egy menüpontot: ")

    if valasztas == "1":
        for szoba in szalloda.szobak:
            print(szoba)
    elif valasztas == "2":
        szobaszam = int(input("Adja meg a szobaszámot: "))
        datum_str = input("Adja meg a dátumot (YYYY-MM-DD): ")
        datum = datetime.strptime(datum_str, "%Y-%m-%d")
        foglalas = szalloda.foglalas(szobaszam, datum)
        if foglalas:
            print(f"Sikeres foglalás: {foglalas}")
        else:
            print("A szoba már foglalt vagy a dátum nem érvényes.")
    elif valasztas == "3":
        szalloda.foglalasok_listazasa()
    elif valasztas == "4":
        lemondas_idx = int(input("Adja meg a lemondandó foglalás sorszámát: ")) - 1
        if 0 <= lemondas_idx < len(szalloda.foglalasok):
            szalloda.lemondas(szalloda.foglalasok[lemondas_idx])
            print("Lemondás sikeres.")
        else:
            print("Érvénytelen sorszám.")
    elif valasztas == "0":
        print("Köszönjük, hogy használta a szállodai rendszert. Viszontlátásra!")
        break
    else:
        print("Érvénytelen választás. Kérjük, válasszon újra.")
