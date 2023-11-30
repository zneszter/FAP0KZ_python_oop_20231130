from datetime import datetime, timedelta
class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def __str__(self):
        return f"{self.szoba} - Foglalva {self.datum}"
