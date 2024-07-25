# Rock, Paper & Scissors
# By Victor Sório

import random

options = [
    "rock", 
    "paper",
    "scissors",
]

cmd = "continue"

while cmd == "continue":
    choice = random.choice(options)
    
    print("Choose 'rock', 'paper' or 'scissors':")
    inp = str(input()).lower().strip()
    
    if choice == "rock" and inp == "scissors":
        print("Rock crushes scissors. You lose, try again.")
    elif choice == "rock" and inp == "paper":
        print("Paper covers rock. You won!")
    elif choice == "paper" and inp == "rock":
        print("Paper covers rock. You lose, try again.")
    elif choice == "paper" and inp == "scissors":
        print("Scissors cut paper. You won!")
    elif choice == "scissors" and inp == "paper":
        print("Scissors cut paper. You lose, try again.")
    elif choice == "scissors" and inp == "rock":
        print("Rock crushes scissors. You won!")
    elif choice == inp:
        print("It's a tie. Try again.")
    
    print("Would you like to try again? y/n")    
    if str(input()).lower().strip() == "n":
        cmd = "break"
        print("Bye!")
        
    print("------------------------------------")