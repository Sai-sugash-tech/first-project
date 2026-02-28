import math
import random
print("WELCOME TO NUMBER GUESSING GAME")
print("Rules of this game:" \
" you have 10 attempts to find a single number randomly chosen by python between 1 to 100" \
" you will get hints like number is too low or number is too high")
guesses = 0
ran = random.randint(1, 100)
while True:
    ins = int(input("Guess a number between 1 to 100: "))
    print()
    if ins > ran:
        guesses = guesses + 1
        if guesses > 9:
            print("OOPs You ran out of attempts")
            break
        print("Number  is too high try again")
        print(f"number of guesses remaining {10-guesses}")
        print()
    elif ins < ran:
        guesses = guesses + 1
        if guesses > 9:
            print("OOPs You ran out of attempts")
            break
        print("Number is too low try again")
        print(f"number of guesses remaining {10-guesses}")
        print()
    elif ins == ran:
        print(f"Huarry {ins} is a correct guess")
        print(f"Number of guesses taken {guesses}")
        break
    elif ins < 0:
        print("Make sure you typed a positive number")
    elif ins > 100:
        print("Make sure you typed a number below 100")
    else:
        print("Make sure you typed as instructed")
    