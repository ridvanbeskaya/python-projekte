bonus_tabelle = {
    "Vertrieb": {"niedrig": 200, "mittel": 500, "hoch": 1000},
    "IT": {"niedrig": 150, "mittel": 400, "hoch": 900},
    "Verwaltung": {"niedrig": 100, "mittel": 300, "hoch": 600}
}

mitarbeiter_liste = [
    {"name": "Anna", "abteilung": "Vertrieb", "leistung": "hoch"},
    {"name": "Ben", "abteilung": "IT", "leistung": "mittel"},
    {"name": "Carla", "abteilung": "Marketing", "leistung": "niedrig"},  # Abteilung existiert nicht!
    {"name": "David", "abteilung": "Verwaltung", "leistung": "sehr hoch"}  # Leistungsstufe existiert nicht!
]


def boni_berechnen(mitarbeiter_liste, bonus_tabelle):
    boni_liste = []
    for mitarbeiter in mitarbeiter_liste:
        mitarbeiter_a = mitarbeiter.get("abteilung")
        mitarbeiter_l = mitarbeiter.get("leistung") 
        if bonus_tabelle.get(mitarbeiter_a) is None:
            boni_liste.append({"name": mitarbeiter["name"], "bonus": None} )  
        elif bonus_tabelle[mitarbeiter_a].get(mitarbeiter_l) is None:  
            boni_liste.append({"name": mitarbeiter["name"], "bonus": None} )    
        else:
            boni_liste.append({"name": mitarbeiter["name"], "bonus": bonus_tabelle[mitarbeiter_a][mitarbeiter_l]} )
    return boni_liste

print(boni_berechnen(mitarbeiter_liste, bonus_tabelle))
