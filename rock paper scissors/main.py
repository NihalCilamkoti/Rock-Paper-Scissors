import random

options = ["rock", "paper", "scissors"]
random_choice = random.choice(options)
computer = random_choice

def playGame(player, computer):
    print(f"You selected: {player}")
    print(f"Computer selected: {computer}")
    if player == computer:
        return "It's a tie match , play again"
    elif(player == "rock" and computer == "scissors")or(player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
        return "You win"
    else:
        return "You lose , try again"
    

def inputUser():
    player = input("select any of rock , paper , scissors: ").lower()
    return player

def invalid_input(player):
    if player not in ("rock", "paper", "scissors"):
        print("Invalid input, please select either rock, paper, or scissors.")
    else:
        print(f"You selected: {player}")
    return player

player_input = inputUser()
if player_input in options:
    result = playGame(player_input, computer)
    print(result)
else:
    invalid_input(player_input)
    