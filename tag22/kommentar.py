import json

with open("kommentare.json","r",encoding="utf-8") as datei:
    kommenter_liste = json.load(datei)

def anzahl_kommentare(liste):
    counter = 0
    if "text" in liste:
        counter +=1
    for k in liste.get("antworten"):
        counter += anzahl_kommentare(k)
    return counter 

def antwort_tiefe(liste):
    tiefe = 0
    if "antworten" in liste:
        tiefe +=1
    for t in liste.get("antworten"):
        tiefe += antwort_tiefe(t)
    return tiefe

print(anzahl_kommentare(kommenter_liste))
print(antwort_tiefe(kommenter_liste))