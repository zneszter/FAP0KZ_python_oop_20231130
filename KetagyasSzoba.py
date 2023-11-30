from Szoba import Szoba
class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam, ar, egyedi_attributum):
        super().__init__(szobaszam, ar)
        self.egyedi_attributum = egyedi_attributum

    def __str__(self):
        return f"Kétágyas szoba {self.szobaszam} - {self.ar} Ft/éjszaka, Egyedi attribútum: {self.egyedi_attributum}"
