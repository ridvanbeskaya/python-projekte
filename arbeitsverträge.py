from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

class Vertrag:

    def __init__(self,name,startdatum,laufzeit_in_monaten):
        self.name = name
        self.startdatum = startdatum
        self.laufzeit_in_monaten = laufzeit_in_monaten


    def vertrags_dauer(self):
        return self.startdatum + relativedelta(months = self.laufzeit_in_monaten)

    def ablauf_vertrag(self, heute):
        if self.vertrags_dauer() - heute < timedelta(days = 30) and self.vertrags_dauer() > heute:
            return True
        else:
            return False

class AblaufendeVerträge:

    def __init__(self):
        self.veträge = []

    def vertrag_hinzufügen(self,vertrag):
        self.veträge.append(vertrag)
    
    def anzahl_ablaufender_verträge(self,heute):
        counter = 0
        for vertrag in self.veträge:
            if vertrag.ablauf_vertrag(heute) == True:
                counter +=1
        return counter


heute = datetime(2027,1,30)
vertrag1 = Vertrag("Julia", datetime(2026,1,1),12)
print(vertrag1.ablauf_vertrag(datetime(2026,10,1)))
vertrag2 = Vertrag("Anton",datetime(2026,2,15),12)
print(vertrag2.ablauf_vertrag(datetime(2027,1,30)))


probe=AblaufendeVerträge()
probe.vertrag_hinzufügen(vertrag1)
probe.vertrag_hinzufügen(vertrag2)
print(probe.anzahl_ablaufender_verträge(heute))