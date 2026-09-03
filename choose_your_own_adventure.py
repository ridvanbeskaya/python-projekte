user_name = input("Type your name: ")
print(f"Welcome, {user_name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way you like to go ? ").lower()
if answer == "left":
    answer = input("You come to ariver, you can walk around it or swim accross? Type walk to walk around or swim to swim accross:  ").lower()

    if answer == "swim":
        print("You swam accross an were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water an you lost the game.")
    else:
       print("Not a valid option. You lose.")

elif answer == "right":
    print("loser")

else:
    print("Not a valid option. You lose.")