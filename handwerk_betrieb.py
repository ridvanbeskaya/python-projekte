#Gedanken: wir haben Auftrag, Geselle, Phase. 
# Phase-> wird von Geselle ausgeführt, hat Anzahl Stunden
# Geselle-> hat Stundensatz(abhängig von qualifikation und erfahrung)
#
#-------------------
# Auftrag:->hat material, menge und Preis  und hat Dauer, Kosten
# Am ende vom Auftrag sollen 
# -Gesamtkosten augegeben werden(materialkosten + arbeitszeit * stundenlohn)
# -Aufträge die mehr als 40 Stunden dauern = Großauftrag
# -Firmenkunden bekommen 8% rabatt auf arbeitskosten, aber nicht Materialkosten
# -ende des Monats: gesamtkosten aller Aufträge und wieviel Großaufträge
# -negative eingaben sollen erkannt werden
#-----------------

class Auftrag:

    def __init__(self, kunden_typ):
            self.kunden_typ = kunden_typ
            self.phasen = []

    def phase_hinzufuegen(self, phase):
        self.phasen.append(phase)

    def gesamtkosten(self):
            gesamt = 0
            for phase in self.phasen:

                if self.kunden_typ == "Firmenkunde":
                    gesamt += phase.kosten_fuer_geselle() + phase.kosten_fuer_material() -(phase.kosten_fuer_geselle()*0.08)
                else: 
                    gesamt += phase.kosten_fuer_geselle() + phase.kosten_fuer_material()
            return gesamt
    
    def gesamtdauer(self):
            gesamt = 0
            for phase in self.phasen:
                gesamt += phase.stunden
            return gesamt
    
    def ist_groß_auftrag(self):
            if self.gesamtdauer()>40:
                return True
            else:
                return False



class Phase:

    def __init__(self,name,stunden,material,menge,preis_material,geselle):
            self.name = name
            self.stunden = stunden
            self.material = material
            self.menge = menge
            self.preis_material = preis_material
            self.geselle = geselle

    def kosten_fuer_geselle(self):
            if self.geselle.stundensatz < 0 or self.stunden < 0:
                raise ValueError("negativer Stundensatz")
            else:
                return self.stunden * self.geselle.stundensatz

    def kosten_fuer_material(self):
            return self.menge * self.preis_material




class Geselle: 

    def __init__(self, name, stundensatz):
            self.name = name
            self.stundensatz = stundensatz

class Monatsabrechnung:

    def __init__(self):
            self.auftrag = []

    def auftrag_hinzufuegen(self, auftrag):
            self.auftrag.append(auftrag)

    def monat_gesamt_kosten(self):
            gesamt = 0
            for auftrag in self.auftrag:
                gesamt += auftrag.gesamtkosten()
            return gesamt
    
    def gross_auftraege(self):
        counter = 0
        for auftrag in self.auftrag:
            if auftrag.gesamtdauer() >40:
                counter += 1
        return counter

geselle1 = Geselle("Thomas", 20)
geselle2 = Geselle("Patrick", 15)
phase1 = Phase("Entwurf", 10,"papier", 100, 100, geselle1)
phase2 = Phase("Materialzuschnitt", 20, "holz", 100, 100,geselle2)
auftrag1 = Auftrag("Firmenkunde")
auftrag1.phase_hinzufuegen(phase1)
auftrag1.phase_hinzufuegen(phase2)

print("Kosten für Geselle 1: ", phase1.kosten_fuer_geselle())
print("Kosten für Geselle 2: ", phase2.kosten_fuer_geselle())
print("Auftrag Gesamtkosten: ", auftrag1.gesamtkosten())
print("Auftrag ist Großauftrag: ", auftrag1.ist_groß_auftrag())