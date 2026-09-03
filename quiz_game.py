print("Willkommen zu diesem Quiz!")

playing = input("Do you want to Play? ")

if(playing.lower() != "yes"):{ #.lower() wandelt alles in kleingeschriebenes
#.upper()macht das gegenteil
    quit() #beendet das Programm
    }

print("Okay! Lets play:)")
punkte = 0

#First Question
answer = input("What does CPU stand for? ")
if answer == "Central Processing Unit":
    print("correct!")
    punkte +=10
else: 
    print("false!")
    punkte -=10

#Second Question
answer = input("What does GPU stand for? ")
if answer == "Graphics Processing Unit":
    print("correct!")
    punkte +=10
else: 
    print("false!")
    punkte -=10

#Third Question
answer = input("What does RAM stand for? ")
if answer == "Random Access Memory":
    print("correct!")
    punkte +=10
else: 
    print("false!")
    punkte -=10

#fourth Question
answer = input("What does PSU stand for? ")
if answer == "Power supply unit":
    print("correct!")
    punkte +=10
else: 
    print("false!")
    punkte -=10

print("Game Over, xour Highscore: " + str(punkte)) #str() wandelt die zahl in ein string