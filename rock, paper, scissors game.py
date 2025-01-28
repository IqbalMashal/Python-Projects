import random 

options  = ("rock", "paper", "scissors")

player = None
computer = random.choice(options)
flag = True

while flag:
    player = input("Enter a choise (rock, paper, and scissors): ")

    if player not in options:
        print("Invalid option, Try again")
    elif player == computer:
        print("Tie Game")
    elif player == "rock" and computer == "scissors":
        print(f"You win! {player} beats {computer}")
    elif player == "paper" and computer == "rock":
        print(f"You win! {player} beats {computer}")
    elif player == "paper" and computer == "paper":
        print(f"You win! {player} beats {computer}")
    else:
        print(f"You lost!  {player} does not beats {computer}")

    
    