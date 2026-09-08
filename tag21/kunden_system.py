import csv

with open("kunden_altsystem.csv", "r") as f:
    alt = [zeile["email"] for zeile in csv.DictReader(f)]

with open("kunden_neusystem.csv", "r") as f:
    neu = [zeile["email"] for zeile in csv.DictReader(f)]

alt_set = set(alt)
neu_set = set(neu)

gemeinsam = alt_set & neu_set
nur_alt = alt_set - neu_set
nur_neu = neu_set - alt_set

print("Gemeinsam:", gemeinsam)
print("Nur alt:", nur_alt)
print("Nur neu:", nur_neu)