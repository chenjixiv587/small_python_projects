"""
Examples:
3d6 rolls three 6-sided dice
1d10+2 rolls one 10-sided die, and adds 2
2d38-1 rolls two 38-sided die, and subtracts 1
QUIT quits the program

次数  d  面数  加号/减号  加减值
"""
import sys
import random

print("game begin..")
input("Press enter to begin....")

while True:
    try:
        print("please enter the command you want.")
        diceStr = input("> ").strip().lower()
        if diceStr.upper() == "QUIT":
            print("you don't want to play bye")
            sys.exit()

        # 字符串中必须要有d
        dIndex = diceStr.find("d")
        if dIndex == -1:
            raise Exception("must have d")

        # 获得次数
        numberOfTimes = diceStr[:dIndex]
        if not numberOfTimes.isdecimal():
            raise Exception("numberOfTimes must be a number")
        numberOfTimes = int(numberOfTimes)

        # 获得 加 减 号 乘号位置
        hasModIndex = diceStr.find("+")
        if hasModIndex == -1:
            hasModIndex = diceStr.find("-")
            if hasModIndex == -1:
                hasModIndex = diceStr.find("*")

        # 获得面数
        if hasModIndex == -1:
            numberOfSides = diceStr[dIndex + 1:]
        else:
            numberOfSides = diceStr[dIndex + 1: hasModIndex]

        if not numberOfSides.isdecimal():
            raise Exception("numberOfSides must be a number")
        numberOfSides = int(numberOfSides)

        # 加减值
        if hasModIndex == -1:
            modAmount = 0
        else:
            modAmount = diceStr[hasModIndex + 1:]
            if not modAmount.isdecimal():
                raise Exception("modAmount must be a number")
            modAmount = int(modAmount)
            if diceStr[hasModIndex] == "-":
                modAmount = -modAmount

        # 扔色子
        rolls = []
        for i in range(numberOfTimes):
            roll = random.randint(1, numberOfSides)
            rolls.append(roll)
        # 将最小的剔除掉
        rolls.sort(reverse=True)
        rolls.pop()

        if diceStr[hasModIndex] == "*":
            total = sum(rolls) * modAmount
        else:
            total = sum(rolls) + modAmount

        # 展示
        print(total, " ", end="")
        print("(", end="")

        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)
        print(", ".join(rolls), end="")

        if modAmount != 0:
            modSign = diceStr[hasModIndex]
            print(f", {modSign}{abs(modAmount)}", end="")
        print(")")

    except Exception as e:
        print(f"the error is {str(e)}")
        continue
