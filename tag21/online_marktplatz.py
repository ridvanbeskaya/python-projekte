import csv

with open(".csv", "r") as v:
    verkäufer_region_nord = [a[""] for v in csv.DictRead(v)]

with open(".csv", "r") as v:
    verkäufer_region_süd = [a[""] for v in csv.DictRead(v)]

verkäufer_nord = set(verkäufer_region_a)
verkäufer_süd = set(verkäufer_region_b)

#Verkäufer über beide Regionen zusammen
alle_verkäufer = verkäufer_nord | verkäufer_süd
print(f"Alle Verkäufer: {alle_verkäufer}")

#Verkäufer die in beiden Regionen aktiv sind
verkäufer_beide_regionen = verkäufer_nord and verkäufer_süd
print(f"Alle Verkäufer die in beiden Regionen Aktiv sind: {verkäufer_beide_regionen}")

#Verkäufer die ausschließlich in einer Region aktiv sind
verkäufer_nur_eine_region = verkäufer_nord - verkäufer_süd
print(f"Verkäufer die nur in einer Region Aktiv sind: {verkäufer_nur_eine_region}")