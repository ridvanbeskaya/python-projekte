import csv

with open("lagerbestand.csv","r") as datei:
    reader = list(csv.DictReader(datei, delimiter=","))

    def gesamtwert(lager_liste):
        gesamt = 0
        for produkt in lager_liste:
         if float(produkt.get("menge")) > 0:
            gesamt += float(produkt.get("menge"))*float(produkt.get("einzelpreis"))
        return gesamt

    print(gesamtwert(reader))

    def mindestbestand(lager_liste):
        mindestbestand_liste =[a["produkt"] for a in lager_liste if float(a["menge"])<float(a["mindestbestand"])]
        return mindestbestand_liste
    print(mindestbestand(reader))

    def negative_werte(lager_liste):
        negative_wert_liste = []
        for a in lager_liste:
            if float(a.get("menge")) < 0 or float(a.get("menge")) is None:
                negative_wert_liste.append(a["produkt"])
            elif float(a.get("einzelpreis")) < 0 or float(a.get("einzelpreis")) is None:
                negative_wert_liste.append(a["produkt"])
            elif float(a.get("menge")) < 0 or float(a.get("menge")) is None:
                negative_wert_liste.append(a["produkt"])
        return negative_wert_liste
    print(negative_werte(reader))



