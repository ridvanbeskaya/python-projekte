class Termin:

    def __init__(self,name):
        self.name=name
        self.liste = []


    def dienstlesitung(self,dienstleistung_name):

        self.liste.append(dienstleistung_name)
        return self.liste

    def kosten_und_dauer(self, katalog):
        kosten = 0
        dauer = 0
        for name in self.liste:
            dienst = katalog.get(name)
            if dienst is None:
                print("Unbekannte Dienstlesitung")
            else:
                kosten += dienst[0]
                dauer += dienst[1]
        if kosten > 100:
            print("Rabat von 10%: ")
            kosten = kosten - (kosten*0.1)
        return kosten, dauer

class Tagesabrechnung:

    def __init__(self):
        self.liste = []

    def termin_hinzufuegen(self,termin_objekt):
        self.liste.append(termin_objekt)
        return self.liste
    
    def gesamtumsatz(self,katalog):
        gesamt = 0
        for termin in self.liste:
            kosten, dauer = termin.kosten_und_dauer(katalog)
            print("Kosten: ", kosten)
            gesamt += kosten
        return gesamt



katalog = {"waschen&schneiden": [35,45],"föhnen": [15,20],
"färben": [60,90], "dauerwelle": [80,120], "bartschnitt": [12,5]}

TerminA = Termin("Hannah")
TerminA.dienstlesitung("föhnen")
TerminA.dienstlesitung("dauerwelle")
TerminA.dienstlesitung("färben")
TerminB = Termin("Julia")
TerminB.dienstlesitung("föhnen")
TerminB.dienstlesitung("färben")
print(TerminA.kosten_und_dauer(katalog))
print(TerminB.kosten_und_dauer(katalog))
abrechnung = Tagesabrechnung()
abrechnung.termin_hinzufuegen(TerminA)
abrechnung.termin_hinzufuegen(TerminB)
print("Tagesabrechnung: ", abrechnung.gesamtumsatz(katalog))