import json

with open("dateisystem.json","r",encoding="utf-8") as d:
    datei_liste = json.load(d)


def maximale_kb(datein):
    anzahl = 0
    for datei in datein.get("inhalt"):
        if datei.get("typ")=="datei":
            anzahl += datei.get("groesse_kb")
        elif datei.get("typ")=="ordner":
            anzahl += maximale_kb(datei)
    return anzahl

print(maximale_kb(datei_liste))