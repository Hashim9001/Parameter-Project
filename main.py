import random

def findNumber(computerNumber):
    number = int(input("Try to guess a number between 1 and 1000\n"))
    if number == computerNumber:
        print("CONGRATULATIONS. You Got It!")

    else:
        print("The number to guess was " + str(computerNumber))
        if number > computerNumber:
            newNumber = number - computerNumber
            if newNumber < 100:
                print(f"That was pretty close. You just overshot by a bit. You missed by {newNumber}.\n")
            else:
                print(f"You overshot that by quite a bit. You missed by {newNumber}.\n")
        else:
            newNumber = computerNumber - number
            if newNumber < 100:
                print(f"That was really close. You just undershot by a bit. You missed by {newNumber}.\n")
            else:
                print(f"Your number was too small. You missed by {newNumber}.\n")

while True:
    ranNumber = random.randint(1,1000)
    findNumber(ranNumber)