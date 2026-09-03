import re
class Miete:

    def __init__(self,name,kaltmiete,nebenkosten):
        self.name = name
        self.kaltmiete = kaltmiete
        self.nebenkosten = nebenkosten

    
    def __str__(self):
        return f"Name: {self.name}, Kaltmiete: {self.kaltmiete}, Nebenkosten: {self.nebenkosten}"
    
    @staticmethod
    def textzeile_prüfen(text):
       muster = muster = r"^[a-zA-ZäöüÄÖÜß\s]+;\s*\d+(\.\d+);\s*\d+(\.\d+)$"
       return bool(re.fullmatch(muster,text))


    @classmethod
    def aus_textzeile(cls, text):
        teile = text.split(";")
        name = teile[0]
        kaltmiete = float(teile[1])
        nebenkosten = float(teile[2])
        return Miete(name, kaltmiete, nebenkosten)



mieten = ["Julia Muster;850.0;190.50", "Hans Müller;750.00;120.50", "Alex Strauss;1050.00;220.50"]

for a in mieten:
    miete = Miete.aus_textzeile(a)
    print(miete.__str__())
    print(miete.textzeile_prüfen(a))