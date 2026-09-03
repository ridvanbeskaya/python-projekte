import random



#number = input("Guess the number: ")
score = 0

# while True:
#     random_number = random.randrange(1,7)
#     number = int(input("Guess the number: ").strip())
#     if number == random_number:
#         print("richtig erraten!")
#         score +=1
#     else:
#         print(f"falsch! die zahl lautet{random_number}")
#     if score == 3:
#         print(f"Glückwunsch du hast {score} mal erraten")
#         quit()

for versuch in range(5):
     random_number = random.randrange(1,7)
     number = int(input("Guess the number: ").strip())
     if number == random_number:
        print("richtig erraten!")
        score +=1
     else:
        print(f"falsch! die zahl lautet{random_number}")
     
 
print(f"Du hast {score} mal richtig erraten! ")