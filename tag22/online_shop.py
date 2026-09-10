import json

with open("kategorien.json","r",encoding="utf-8")as k:
    kategorien_liste = json.load(k)


def kategorien_tiefe(liste):
    anzahl_produkte = liste.get("eigene_produkte")
    for unterkategorie in liste.get("unterkategorien"):
        anzahl_produkte += kategorien_tiefe(unterkategorie)
    return anzahl_produkte

#--------------------------------------
# def kategorien_tiefe(kategorie):
#     anzahl = kategorie.get("eigene_produkte")
#     for unterkategorie in kategorie.get("unterkategorien"):
#         anzahl += kategorien_tiefe(unterkategorie)
#     return anzahl
#---------------------------------------

print(kategorien_tiefe(kategorien_liste))