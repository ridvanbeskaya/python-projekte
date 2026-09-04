import json

with open("mitarbeiter.json", "r", encoding="utf-8") as datei:
    mitarbeiter_daten = json.load(datei)

# def durchschnittsgehalt(mitarbeiter_daten):
#     gesamt = 0
#     length = 0
#     for m in mitarbeiter_daten:
#         if m.get("gehalt") == None:
#             continue
#         else:
#             gesamt += m.get("gehalt")
#             print(gesamt)
#             length += 1
#     if length == 0:
#         return None
#     return gesamt / length
def durchschnittsgehalt(mitarbeiter_daten):
    gehaelter = [m["gehalt"] for m in mitarbeiter_daten if "gehalt" in m]
    if not gehaelter:
        return None
    return sum(gehaelter)/len(gehaelter)
print(durchschnittsgehalt(mitarbeiter_daten))