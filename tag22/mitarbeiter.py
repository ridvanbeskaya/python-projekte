class Mitarbeiter:
    def __init__(self, name):
        self.name = name
        self.untergebene = []

    def untergebenen_hinzufuegen(self, mitarbeiter):
        self.untergebene.append(mitarbeiter)

    def team_groesse(self, besucht=None):
        if besucht is None:
            besucht = set()
        if self in besucht:
            raise ValueError(f"Zirkelbezug entdeckt bei {self.name}!")
        besucht.add(self)
        anzahl = len(self.untergebene)
        for u in self.untergebene:
            anzahl += u.team_groesse(besucht)
        return anzahl


geschaeftsfuehrer = Mitarbeiter("Frau Neumann")
abteilungsleiter_1 = Mitarbeiter("Herr Kraus")
abteilungsleiter_2 = Mitarbeiter("Frau Ott")
#abteilungsleiter_3 = Mitarbeiter("Herr X")
teamleiter_1 = Mitarbeiter("Herr Bauer")

geschaeftsfuehrer.untergebenen_hinzufuegen(abteilungsleiter_1)
geschaeftsfuehrer.untergebenen_hinzufuegen(abteilungsleiter_2)
#geschaeftsfuehrer.untergebenen_hinzufuegen(abteilungsleiter_3)
abteilungsleiter_1.untergebenen_hinzufuegen(teamleiter_1)
abteilungsleiter_1.untergebenen_hinzufuegen(geschaeftsfuehrer)

print(geschaeftsfuehrer.team_groesse())