import os
import random
print("START")
choices= ["Rock","Paper","Scissor"]
yourturn = input("Enter your choice(Rock,Paper,Scissor):")
botturn = random.choice(choices)
print(f"\n Your turn {yourturn}, bot's turn{botturn}.\n")

if(yourturn == botturn):
    printf("It's a tie")
elif(yourturn =="rock"):
    if(botturn == "scisssor"):
        printf("YOU WON")
        else:
        print("YOU LOST ")
    elif yourturn == "paper":
        if botturn == "rock":
            print("YOU WON!")
        else:
            print("YOU LOST.")
    elif yourturn == "scissors":
        if botturn== "paper":
            print("YOU WON")
        else:
            print("YOU LOST")
