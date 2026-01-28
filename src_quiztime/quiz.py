'''
quiz game with mostly mulitple choice questions,
with a few harder puzzles and a riddle thrown in to spice
the game up.

'''



import os


def clearconsole():
    #clears the console
    os.system('cls')

    return


RedColorCode = '\033[31m'
GreenColorCode = '\033[32m'
NilColorCode = '\033[0m'
GrayishColorCode = '\033[26m'
score = 0
clearconsole()
print(GrayishColorCode + "Welcome to the best quiz ever." + NilColorCode)
print(GrayishColorCode + "For these first easy questions type A, B, C, or D to answer." + NilColorCode)
print("")
questions = [
    ("What is the capital of Sweden?",
     ["A) Berlin", "B) Tuesday", "C) Paris", "D) Stockholm"],
     "D"),

    ("Which state are you in right now?",
     ["A) Sold", "B) Liquid", "C) Oregon", "D) Gas"],
     "C"),

    ("What is 6 + 7?",
     ["A) heh... 67...", "B) 21", "C) 13.314", "D) 11 * 2 / 2 - 3 + 4 - 2 + 3"],
     "D"),

    ("For these next questions, type the answer in full. \n What is best subject?",
     [""],
     "NONE OF THEM"),

    ("What is the current year?",
     [""],
     "2026"),
     
    ("What is the color of the sun?",
     [""],
     "WHITE"),

     
]

for question, options, correct_answer in questions:
    print(question)
    for option in options:
        print(option)
    answer = input("Your answer: ").upper()

    if answer == correct_answer:
        score += 1
        clearconsole()
        print(GreenColorCode + "Correct!!!" + NilColorCode)
    else:
        clearconsole()
        print(RedColorCode + "WRONG! The correct answer is", correct_answer + NilColorCode)

print("Quiz finished!")


if score <= 5:
    print(RedColorCode + "Your grade:", score, "out of", len(questions),
          "You get an F for FAILURE!")

if score == 6 or score == 7 or score == 8:
    print(RedColorCode + "Your grade:", score, "out of", len(questions),
          "I give it a solid C, TRY HARDER!")

if score == 9:
    print(GreenColorCode + "Your grade:", score, "out of", len(questions),
          "Pretty good, high B, not an A but you've done well enough.")

if score == 10:
    print(GreenColorCode + "Your grade:", score, "out of", len(questions),
          "Great job, you've truly impressed me.")
