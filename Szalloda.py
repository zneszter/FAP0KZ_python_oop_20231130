class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []


    def foglalas(self, szobaszam, datum):
        szoba = next((s for s in self.szobak if s.szobaszam == szobaszam), None)
        if szoba and not self._foglalt(szoba, datum):
            foglalas = Foglalas(szoba, datum)
            self.foglalasok.append(foglalas)
            return foglalas
        return None

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)

    def foglalasok_listazasa(self):
        for foglalas in self.foglalasok:
            print(f"Foglalás: {foglalas}")
