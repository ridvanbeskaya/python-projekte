class Fahrzeug:
    def __init__(self, kennzeichen, kilometerstand):
        self.kennzeichen = kennzeichen
        self.kilometerstand = kilometerstand

    def wartung_faellig(self):
        if self.kilometerstand > 100000:
            return True
        else:
            return False


class LKW(Fahrzeug):

    def __init__(self,kennzeichen,kilometerstand,max_ladung_kg):
        super().__init__(kennzeichen, kilometerstand)
        self.max_ladung_kg = max_ladung_kg


class Transporter(Fahrzeug):

    def __init__(self,kennzeichen,kilometerstand,max_ladung_kg):
        super().__init__(kennzeichen, kilometerstand)
        self.max_ladung_kg = max_ladung_kg


lkw_1 = LKW("B-XY 123", 120000, 12000)
transporter_1 = Transporter("K-AB 456", 45000, 1500)

print(lkw_1.wartung_faellig())
print(transporter_1.wartung_faellig())