#Hangman Game
#Saleem A


import os
import random

def start_screen():
    print("************************************")
    print("   ******************************   ")
    print("      ************************      ")
    print("         ******************         ")
    print("**************HANGMAN***************")
    print("         ******************         ")
    print("      ************************      ")
    print("   ******************************   ")
    print("************************************")

    print("  \|||||/")
    print(" ( ~   ~ )")
    print("@( 0   0 )@")
    print(" (   C   )")
    print("  \ \_/ /")
    print("   |___|") 
    print("    | |")

def show_credits():
    print()
    print("*********************************************")
    print("This awesome game was created by THE Saleem. ")
    print("******* Created on November 11,2017 *********")
    print("*********************************************")
    
def get_puzzle():
    path = "data"

    file_names = os.listdir(path)

    for i, f in enumerate(file_names):
        with open(path + "/" + f, "r") as f:
            beginning_lines = f.read().splitlines()
        category_name = beginning_lines[0]
        print(str(i + 1) + ") " + category_name)
              
    print()
    choice = input("Please pick the number of the category that you would like to play. ")
    print()
    print("*NOTE*: if you think that my word has a space, press the space bar as a guess.")
    choice = int(choice)
    choice = choice - 1

    file = path + "/" + file_names[choice]
  

    with open(file,"r")as f:
        lines = f.read().splitlines()

    

    category_name = lines[0]
    puzzle = random.choice( lines[1:] )

    print(category_name)
    return puzzle
    

def get_solved(puzzle, guesses):
    solved = ""

    for letter in puzzle:
        if letter in guesses:
            solved += letter
        else:
            solved += "-"

    return solved

def get_guess():
    while True:
        letter = input("Guess a letter: ")

        if len(letter) == 1:
            if(letter).isalpha():
                return letter
            else:
                print("You must enter one letter at a time cheater.")
                print()
        else:
                print("You must enter one letter at a time cheater.")
                print()

def display_board(solved):
    print(solved)

def show_result(result):
    if result == 0:
         print("You Win!!! Good Job!")
    else:
        print("You lost.")
    

def play_again(name):
    while True:
        decision = input("Would you like to play again " + name + " ? (y/n)")
        print()
        decision = decision.lower()

        if decision == "y" or decision == "yes":
            return True
        elif decision == "n" or decision == "no":
            print("OK then, have a nice day!")
            return False
        
        else:
            print("I don't understand, please enter a valid response.")
    
def play(name):
    print("Welcome to Hangman Game, " + name + "!! ")
    print()
    print("You'll have 6 guesses to try and figure out my word.")
    puzzle = get_puzzle()
    guesses = ""
    solved = get_solved(puzzle, guesses)
    display_board(solved)

    strikes = 0
    limit = 6
    result = 0
    print(solved)
    gameover = 0

    while solved != puzzle and gameover == 0:
        letter = get_guess()

        if letter not in puzzle:
            strikes +=1
            print("HAHA, that letter isn't in my word!")
            print()
            print("You have " + str(strikes) + " strikes so far. Be careful " + name + " .")
            print()
            if strikes == limit:
                print("You lose " + name + ", hehehehe, you couldn't guess it in 6 tries, how disappointing.")
                print()
                result = 1
                gameover = 1
                print(puzzle)
        
        guesses += letter
        solved = get_solved(puzzle, guesses)
        display_board(solved)

    show_result(result)

    
# Game starts running here
start_screen()
playing = True

while playing:
    name = input("What is your name earthling? ")
    play(name)
    playing = play_again(name)
show_credits()
