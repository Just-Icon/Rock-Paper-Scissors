#import random module
import random

#introduction to the game
print("Welcome to 'rock', 'paper', 'scissors' game.\nPls choose any of 'rock', 'paper', or 'scissors' by typing 'R', 'P' or 'S'.")
options = ['R', 'P', 'S']
"R" == "Rock"
"P" == "Paper"
"S" == "Scissors"

#input from user and computer
user_choice = input("Enter your letter: ").upper()

#loop in case user picks the wrong letter
while user_choice not in options:
    print("Oops!!\nThat's not accepted\nPls choose a letter from the list\n")
    user_choice = input("Enter your letter: ").upper()

cpu_choice = (random.choice(options))

print(f"Player({user_choice}) : CPU({cpu_choice})")

rule1 = ('R' > 'S')
rule2 = ('S' > 'P')
rule3 = ('P' > 'R')

#loop to restart if the CPU and the user pick the same letter.
while user_choice == cpu_choice:
    print("It's a tie, pls play again")
    user_choice = input("Enter your letter: ").upper()
    while user_choice not in options:
        print("Oops!!\nThat's not accepted\nPls choose a letter from the list\n")
        user_choice = input("Enter your letter: ").upper()

    cpu_choice = (random.choice(options))

    print(f"Player({user_choice}) : CPU({cpu_choice})")

#conditionals to decide winner
if user_choice == "R":
    if cpu_choice == "S":
        print("You win")
    elif cpu_choice == "P":
        print("CPU wins")
elif user_choice == "P":
    if cpu_choice == "R":
        print("You win")
    elif cpu_choice == "S":
        print("CPU wins")
elif user_choice == "S":
    if cpu_choice == "P":
        print("You win")
    elif cpu_choice == "R":
        print("CPU wins")
