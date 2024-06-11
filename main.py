import random

print("Welcome to Stone Paper Scissor Game!!!")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

playing = input("\nDo you want to play ? ")

if playing != "yy" :
    quit()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


User_wins = 0
Computer_wins = 0
Draw = 0

options=["stone","paper","scissor"]

while True:
    User_input = input("\nType stone / paper / scissor or \nq to Quit \nEnter your choice :")
    
    if User_input == "q":
        break
    
    if User_input not in options:
        continue

    random_number = random.randint(0,2)
    # stone:0,paper:1,scissor:2
    Computer_pick = options[random_number]
    print("Computer picked",Computer_pick + ".")

    if User_input == "stone" and Computer_pick == "scissor" :
        print("Congratulations!You won!!")
        User_wins += 1

    elif User_input == "paper" and Computer_pick == "stone" :
        print("Congratulations!You won!!")
        User_wins += 1

    elif User_input == "scissor" and Computer_pick == "paper" :
        print("Congratulations!You won!!")
        User_wins += 1

    elif User_input == Computer_pick :
        print("It was a draw!")
        Draw += 1

    else:
        print("Sorry!You Lost!!")
        Computer_wins += 1

print("\nYou won",User_wins,"times.")
print("The Computer won",Computer_wins,"times.")
print("It was a draw for",Draw,"times.")
print("Goodbye!!!")
        
     



       
     
