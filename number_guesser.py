import random

top_of_range = input("Type a number! ")

if top_of_range.isdigit(): #checkt ob die eingabe ein Digit ist !!
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger than 0 next time")
        quit()

else:
    print("Please type in a digit")
    quit()

random_number = random.randint(1,top_of_range)

while True:
    user_guess = input("Guess a number: ")
    if user_guess.isdigit(): #checkt ob die eingabe ein Digit ist !!
     user_guess = int(user_guess)

    else:
     print("Please type in a digit")
     continue #startet die schleife wieder

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        print("false, please try it agein!")
