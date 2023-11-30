from Foglalas import Foglalas
from datetime import datetime

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadas(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        szoba = next((s for s in self.szobak if s.szobaszam == szobaszam), None)


        if szoba and not self._foglalt(szoba, datum) and datum > datetime.now():
            foglalas = Foglalas(szoba, datum)
            self.foglalasok.append(foglalas)
            return foglalas
        return None

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)

    def foglalasok_listazasa(self):
        for i, foglalas in enumerate(self.foglalasok,1):
            print(f"Sorszáma: {i} Foglalás: {foglalas}")

    def _foglalt(self, szoba, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                return True
        return False
