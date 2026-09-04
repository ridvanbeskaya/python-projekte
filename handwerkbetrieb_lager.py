import csv

with open("lagerbestand.csv","r") as datei:
    reader = csv.DictReader(datei, delimiter=",")


    for zeile in reader:
        print(zeile)