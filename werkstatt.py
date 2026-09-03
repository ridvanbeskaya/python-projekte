class Kunde:

    def __init__(self,name,fahrzeug):
        self.name = name
        self.fahrzeug = fahrzeug
        self.auftrag = []
    

    def __str__(self):
        a = []
        for auftrag in self.auftrag:
            a.append(auftrag.__str__())
        return f"Kunde : {self.name}, {self.fahrzeug}, {', '.join(a)}"

    def auftrag_hinzufuegen(self, auftrag):
        self.auftrag.append(auftrag)

    def gesamt_kosten(self):
        gesamt = 0
        auftrag_menge = 0
        for auftrag in self.auftrag:
            auftrag_menge +=1
            gesamt += auftrag.kosten
        if auftrag_menge > 2:
            gesamt = gesamt - (gesamt * 0.05)    
        return gesamt

    def gesamt_dauer(self):
        gesamt = 0
        for auftrag in self.auftrag:
            gesamt += auftrag.dauer
        return gesamt

class Auftrag:

    def __init__(self, name,kosten, dauer):
        self.name = name
        self.kosten = kosten
        self.dauer = dauer

    def __str__(self):
        return f"Auftrag: {self.name}"
    



kunde1 = Kunde("thomas","BMW")
kunde1.auftrag_hinzufuegen(Auftrag("ölwechsel",60,30))
kunde1.auftrag_hinzufuegen(Auftrag("reifen wechseln",  100,30))

print(kunde1)

