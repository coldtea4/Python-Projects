#loop
    #ask user roll dice or not
    #if user says yes, roll two dice and print the values
    #if user says no, end the game
    #if user gives invalid response, ask again until valid response is given
import random

dice_value_1 = -1
dice_value_2 = -1
while True:
    player_response = input("Roll the dice? (y/n): ").strip().lower()
    if player_response == "y":
        print("Rolling dice.")
        dice_value_1 = random.randint(1, 6)
        dice_value_2 = random.randint(1, 6)
        if dice_value_1 == 1 and dice_value_2 == 1:
            print("Ouch... snake eyes!")
        print(F"({dice_value_1}, {dice_value_2})")
    elif player_response == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid response. Try again, Please.")

        
    