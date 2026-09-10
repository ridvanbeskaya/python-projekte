import json

with open("stueckliste.json","r",encoding="utf-8") as datei:
    stück_liste = json.load(datei)


def gesamtpreis(liste,bauteil):
    preis = 0
    if liste.get("einzelpreis") != 0 and liste.get("bauteil") == bauteil:
        preis = liste.get("einzelpreis")
    
    for b in liste.get("bestandteile"):
        preis +=gesamtpreis(b,bauteil)
    return preis

print(gesamtpreis(stück_liste,"Hinterrad"))