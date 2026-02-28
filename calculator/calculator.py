import math
def plus():
    n = 0
    while True:
        a = int(input("Enter numbers to continue addition (0 to quit): "))
        n += a
        if a == 0:
            print(f"The final value is {n}")
            break
def minus():
    n = 0
    while True:
        a = int(input("Enter numbers to continue subtraction (0 to quit): "))
        n = a - n 
        if a == 0:
            print(f"The final value is {n}")
            break
def multiply():
    n = 1
    while True:
        a = int(input("Enter numbers to continue multiplication (1 to quit): "))
        n *= a
        if a == 1:
            print(f"The final value is {n}")
            break
def division():
    a = int(input("enter a divident(0 to quit): "))
    b = int(input("enter a divisor(0 to quit): "))
    s = a /b
    print(f"the value is {s:5f}")
while True:
    inp = input("select a type to execute (+, -, *, /)(q to quit): ")
    if inp == "+":
        plus()
    elif inp == "-":
        minus()
    elif inp == "*":
        multiply()
    elif inp == "/":
        division()
    elif inp == "q":
        break
    else:
        print("make sure you entered only the given option :)")