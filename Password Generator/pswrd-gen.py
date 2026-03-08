import random 
import string 
def num_only():
    c = int(input("enter how many digits do you want in your password: "))
    for x in range(c):
        num = random.randint(1, 9)
        print(num, end="")
def l_only():
    c = int(input("enter how many letters do you want in your password: "))
    for x in range(c):
        l = random.choice(string.ascii_letters)
        print(l, end="")
def both():
    c = int(input("enter how many characters do you want in your password: "))
    for x in range(c-3):
        l = random.choice(string.ascii_letters)
        print(l, end="")
    for y in range(3):
        num = random.randint(1, 9)
        print(num, end="")
while True:
    ins = input("\nwhat type of password do you want (only num/only letters/both)(Q to quit): ")
    if ins == "only num":
        num_only()
    elif ins == "only letters":
        l_only()
    elif ins == "both":
        both()
    elif ins == "Q" or ins == "q" or ins == "quit" or ins == "Quit":
        break
    else:
        print("Make sure you type the exact same given options :)")

