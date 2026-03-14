questions = ("What is the capital of japan?: ", 
             "Which programming lanuguage is known for its snake logo?: ", 
             "Which is planet is known as red planet?: ", 
             "What is the atomic mass of Hydrogen?: ", 
             "Which programming language is used to build Roblox")
options = ("A.New Delhi  B.Sao Paulo  C.Tokyo  D.Moscow ", 
           "A.C++  B.Java  C.Python  D.JavaScript", 
           "A.Mercury  B.Venus  C.Earth  D.Mars", 
           "A.1  B.8  C.5  D.2", 
           "A.Lua  B.Python  C.Ruby  D.Rust")
answers = ("C", "C", "D", "A", "A")
i = 0
score = 0
lives = 10
print("Welcome to py quiz game")
print("You have 10 lives to answer five questions, 4 options will be given to answer," \
    "Type the option's key only (A/B/C/D), if answer is wrong -1 lives & you don't get score points")
for i in range(len(answers)):
    print()
    print(questions[i])
    print(options[i])
    print()
    q = input("Enter the option key: ")
    print()
    if q == answers[i]:
        score += 1        
        print(f"Yes!, {q} is a correct option, +1 score")
        print(f"Current score {score}")
    else:
        print("OOPs, wrong answer")
        while not q == answers[i]:
            lives -= 1
            print()
            print(f"Lives remaining {lives}")
            print(questions[i])
            print(options[i])
            print()
            q = input("Enter the option key: ")
            if lives == 0:
                break
    if lives == 0:
        print("GAME OVER , Try again")
        break
print(f"Final score {score}")