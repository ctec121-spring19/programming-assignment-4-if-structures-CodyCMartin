# Module 3
#   Programming Assignment 4
#     Prob-3.py

# <Cody Martin>

def letterGrade(score):
    if score == 0:
        letterGrade = "F"
    elif score == 1:
        letterGrade = "F"
    elif score == 2:
        letterGrade = "D"
    elif score == 3:
        letterGrade = "C"
    elif score == 4:
        letterGrade = "B"
    elif score == 5:
        letterGrade = "A"
    

    return letterGrade

def unitTest():
    print("If score = 1:\t", letterGrade(0))
    print("If score = 1:\t", letterGrade(1))
    print("If score = 1:\t", letterGrade(2))
    print("If score = 1:\t", letterGrade(3))
    print("If score = 1:\t", letterGrade(4))
    print("If score = 1:\t", letterGrade(5))

if __name__ == "__main__":
    unitTest()