import random

print("Willkommen zu Lingo!")


wörter = ["Haus","Hund","Katze","Maus"]
rate_wort= random.choice(wörter)
erster_buchstabe=[rate_wort[0]]
versuch = 5
neu=""

print("Unser erstes Wort lautet: " + erster_buchstabe[0])
while versuch != 0:
 eingabe_user = input("gebe dein wort ein: ").strip()   
 if eingabe_user == rate_wort:
    print("richtig erraten!")
    break
 else:
    for x in rate_wort:
     if not neu:
        neu = x;
    else:
        neu +="_"
    print(neu)
    for a, b in zip(rate_wort, eingabe_user):
     if(a==b):
      neu+=a
    versuch = versuch-1
    print(f"Versuch es nochmals :), du hast noch: {versuch} versuche")
    print(erster_buchstabe)
    continue
 


# for x in "Haus":
#      for y in "Hmas":
#         if x == y:
#             print(f"der buchstabe {x} ist in deinem wort enthalten")
# a="Haus"
# b="Haxs"   
# wort=[] 
# for a, b in zip(a, b):
#   if(a==b):
#     wort.append(a)
# print(wort)

# wort="Katze"
# neu=""
# for x in wort:
#     if not neu:
#         neu = x;
#     else:
#         neu +="_"
# print(neu)