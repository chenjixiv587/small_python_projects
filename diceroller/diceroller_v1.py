"""
Examples:
3d6 rolls three 6-sided dice
1d10+2 rolls one 10-sided die, and adds 2
2d38-1 rolls two 38-sided die, and subtracts 1
QUIT quits the program

次数 d 面数 加或者减符号 加或者减的数值


"""
import sys
import random

print("Please enter the STRING")
while True:
    try:
        diceStr = input("> ").strip().lower()
        if diceStr.upper() == "QUIT":
            sys.exit()

        dIndex = diceStr.find("d")
        if dIndex == -1:
            raise Exception("d is not find")

        numberOfDices = diceStr[:dIndex]
        if not numberOfDices.isdecimal():
            raise Exception("numberOfDices should be a number")
        numberOfDices = int(numberOfDices)

        hasModIndex = diceStr.find("+")
        if hasModIndex == -1:
            hasModIndex = diceStr.find("-")

        if hasModIndex == -1:
            numberOfSides = diceStr[:dIndex + 1:]
        else:
            numberOfSides = diceStr[:dIndex + 1: hasModIndex]

        if not numberOfSides.isdecimal():
            raise Exception("numberOfSides should be a number")
        else:
            numberOfSides = int(numberOfSides)

        if hasModIndex == -1:
            modAmount = 0
        else:
            modAmount = diceStr[hasModIndex + 1:]
        if not modAmount.isdecimal():
            raise Exception("modAmount should be a number")
        else:
            modAmount = int(modAmount)

        if diceStr[hasModIndex] == "-":
            modAmount = -modAmount

        rolls = []
        for i in range(numberOfDices):
            dice = random.randint(1, numberOfSides)
            rolls.append(dice)

        total = sum(rolls) + modAmount
        print(f"{total}", end="")
        print("(", end="")
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(", ".join(rolls), end="")
        if modAmount != 0:
            modSign = diceStr[hasModIndex]
        print(f", {modSign}{abs(modAmount)}", end="")
        print(")")

    except Exception as e:
        print(f"the error is: {str(e)}")
        continue
