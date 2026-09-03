print("Willkommen zu diesem Quiz!")
spiel_beginnen = input("Willst du mit dem Quiz beginnen? ").strip().lower()

if (spiel_beginnen not in ("yes","ja")):
    quit()

fragen = {"Was bedeutet CPU":"Computer Process Unit","Welches Tir hat 8 Beine":"Spinne",
            "Wie lauetet die Hauptstadt von Deutschland":"Berlin", 
            "Wie lautet die Hauptstadt der Türkei":"Ankara"}

score= 0;

for frage, antwort in fragen.items():
    benutzer_antwort=input(frage + " ")

    if benutzer_antwort.strip().lower() == antwort.lower():
        print("Richtig!")
        score += 1
    else:
        print("falsch!")
        print("Die richtige Antwort lautet: " + antwort)

print(f"Das Quiz ist beendet! Dein Highscore lautet: {score}")