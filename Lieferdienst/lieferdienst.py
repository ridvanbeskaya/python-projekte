import json
import csv


with open("lieferungen.json","r",encoding="utf-8")as datei_json:
    lieferung_daten = list(json.load(datei_json))
    #print("Lieferungen: ",lieferung_daten)

with open("kuriere.csv","r")as datei_csv:
    kurier_daten = list(csv.DictReader(datei_csv,delimiter=","))
    #print("Kurier: ",kurier_daten)


#Klasse für Lieferung
class Lieferung:

    def __init__(self,lieferung_id,kunde,kurier_id,distanz_km,bestellwert,status):
        self.status = status
        self.lieferung_id = lieferung_id
        self.kunde = kunde
        self.kurier_id = kurier_id
        self.distanz_km = distanz_km
        self.bestellwert = bestellwert


    def __str__(self):
        return f"Kunde: {self.kunde}, Liefer_iD: {self.lieferung_id}, Status: {self.status}"

    @classmethod
    def lieferung_erzeugen(cls,lieferung):
        lieferung_id = a.get("lieferung_id")
        kunde = a.get("kunde")
        kurier_id = a.get("kurier_id")
        distanz_km = a.get("distanz_km")
        bestellwert = a.get("bestellwert")
        status = a.get("status")
        return Lieferung(lieferung_id,kunde,kurier_id,distanz_km,bestellwert,status)

    def status_zustand(self, neuer_status):
        if self.status in ["storniert", "geliefert"]:
            raise ValueError("Der Status dieser Bestellung kann nicht mehr geändert werden")
        return self.status = neuer_status
            


# for a in lieferung_daten:
#     lieferung1 = Lieferung.lieferung_erzeugen(a)
#     print(lieferung1)
   
    
#Klasse für Kurrier
class Kurier:

    def __init__(self,kurier_id,name,fahrzeug,km_pauschale):
        self.name = name
        self.fahrzeug = fahrzeug
        self.kurier_id = kurier_id
        self.km_pauschale = km_pauschale
        self.lieferung = []

    def __str__(self):
        return f"Name: {self.name}, Kurier_id:  {self.kurier_id}, Fahrzeug: {self.fahrzeug}"

    def lieferung_hinzufuegen(self,lieferung):
        self.lieferung.append(lieferung)
    
    @classmethod
    def kurier_erzeugen(self,kurier):
        kurier_id = kurier.get("kurier_id")
        name = kurier.get("name")
        fahrzeug = kurier.get("fahrzeug")
        km_pauschale = kurier.get("km_pauschale")
        return Kurier(kurier_id,name,fahrzeug,km_pauschale)
    
    def gesamt_umsatz_pro_kurier(self)



for a in kurier_daten:
    kurier = Kurier.kurier_erzeugen(a)
    print(kurier)
    
#Klasse für Kunde
class Kunde:

    def __init__(self,name):
        self.name = name
        self.lieferung = []

    def lieferung_hinzufuegen(self,lieferung):
        self.lieferung.append(lieferung)