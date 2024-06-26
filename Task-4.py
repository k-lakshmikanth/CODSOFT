##############################################
# Task 4
# Rock, Paper, Scissors Game
# The traditional rock, paper, scissors game where two players each choose one of the three items. The winner is determined by the rules:
# Rock crushes scissors
# Scissors cuts paper
# Paper covers rock
# The game is a tie if both players choose the same item.
##############################################


from random import choice
from os import system

options = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

def retry(func, *args, **kwargs):
    def inner():
        try:
            func(*args, **kwargs)
        except:
            inner()
    return inner

@retry
def play():
    global user_score, computer_score
    system("cls")
    user_input = int(input("Options:\n 1.rock\n 2.paper\n 3.scissors\nEnter your choice: "))-1
    user_input = options[user_input]
    computer_selection = choice(options)

    print(f"\n\nYour Choice: {user_input}\nBot's Choice: {computer_selection}\n")

    GameLogic = (user_input == "rock" and computer_selection == "scissors") or\
                (user_input == "scissors" and computer_selection == "paper") or\
                (user_input == "paper" and computer_selection == "rock")

    if user_input == computer_selection:
        print("😐It's a tie😐")
    elif GameLogic:
        print("🎉You win🎉")
        user_score += 1
    else:
        print("🥺You lose🥺")
        computer_score += 1
    print(f"Score Board:\nYour score: {user_score}\nComputer Score: {computer_score}")

while True:
    play()
    play_again = input("Do you want to play again? (Y/N): ").upper()
    if play_again != "Y":
        print("Exiting...")
        break
    