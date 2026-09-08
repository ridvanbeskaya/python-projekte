import json,csv
from collections import Counter



with open("lieferungen.json","r",encoding="utf-8")as datei_json:
    lieferung_daten = list(json.load(datei_json))
    #print("Lieferungen: ",lieferung_daten)

with open("kuriere.csv","r")as datei_csv:
    kurier_daten = list(csv.DictReader(datei_csv,delimiter=","))
    #print("Kurier: ",kurier_daten)

#Übergänge
erlaubte_uebergaenge = {
    "offen": ["unterwegs", "storniert"],
    "unterwegs": ["geliefert", "storniert"],
    "geliefert": [],       # keine Änderung mehr möglich
    "storniert": []        # keine Änderung mehr möglich
}


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
        lieferung_id = lieferung.get("lieferung_id")
        kunde = lieferung.get("kunde")
        kurier_id = lieferung.get("kurier_id")
        distanz_km = lieferung.get("distanz_km")
        bestellwert = lieferung.get("bestellwert")
        status = lieferung.get("status")
        return Lieferung(lieferung_id,kunde,kurier_id,distanz_km,bestellwert,status)

    def status_zustand(self, neuer_status):
        if self.status in ["storniert", "geliefert"]:
            raise ValueError("Der Status dieser Bestellung kann nicht mehr geändert werden")
        self.status = neuer_status
        return self.status
    
    def meiste_bestellungen(self,lieferung_liste):
        alle_kunden = [lieferung["kunde"] for lieferung in lieferung_liste if "kunde" in lieferung]
        zaehler = Counter(alle_kunden)
        haeufigstes_element, anzahl = zaehler.most_common(1)[0]
        return  haeufigstes_element, anzahl
            
   
    
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
    
    def gesamt_umsatz_pro_kurier(self,kurier_id):
        gesamt = 0
        for k in self.lieferung:
            if k.kurier_id == kurier_id and k.status == "geliefert":
                gesamt += k.bestellwert
                
        return gesamt
    def gesamtgewinn(self):
        kilometer_kosten = 0
        umsatz = 0
        for l in self.lieferung:
            if l.status =="geliefert":
                kilometer_kosten += float(self.km_pauschale)*l.distanz_km
                umsatz += l.bestellwert
        return umsatz - kilometer_kosten

    def alle_lieferungen(self):
        for a in self.lieferung:
            print(a)

        
                
alle_kurier = [Kurier.kurier_erzeugen(k) for k in kurier_daten]

for l in lieferung_daten:
    lieferug = Lieferung.lieferung_erzeugen(l)
    gefunden = False   # Markierung: noch kein Treffer
    for k in alle_kurier:
        if lieferug.kurier_id == k.kurier_id:
            k.lieferung_hinzufuegen(lieferug)
            gefunden = True   # Treffer gefunden!
    if not gefunden:   # NACH der inneren Schleife prüfen: wurde überhaupt ein Treffer gefunden?
        print(f"Warnung: Kurier {lieferug.kurier_id} für Lieferung {lieferug.lieferung_id} nicht gefunden!")


# --- Ausgaben ---
print()
print("=== Lieferungen pro Kurier ===")
for k in alle_kurier:
    print(f"{k.kurier_id} ({k.name}): {len(k.lieferung)} Lieferungen")
 
print()
print("=== Gesamtumsatz pro Kurier (nur 'geliefert') ===")
for k in alle_kurier:
    print(f"{k.kurier_id}: {k.gesamt_umsatz_pro_kurier(k.kurier_id):.2f} Euro")
 
print()
print("=== Gesamtgewinn pro Kurier ===")
for k in alle_kurier:
    print(f"{k.kurier_id}: {k.gesamtgewinn():.2f} Euro")
 
print()
print("=== Häufigster Kunde ===")
beispiel_lieferung = Lieferung.lieferung_erzeugen(lieferung_daten[0])
kunde, anzahl = beispiel_lieferung.meiste_bestellungen(lieferung_daten)
print(f"{kunde} mit {anzahl} Lieferungen")