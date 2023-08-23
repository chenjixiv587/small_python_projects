"""
Examples:
3d6 rolls three 6-sided dice
1d10+2 rolls one 10-sided die, and adds 2
2d38-1 rolls two 38-sided die, and subtracts 1
QUIT quits the program

"""
# 主要的还是考察对字符串的处理能力

import random
import sys

print("dice roller.......")


while True:
    try:
        diceStr = input(">").strip().lower()
        if diceStr.upper() == "QUIT":
            sys.exit()

        # find the 'd' in the diceStr
        dIndex = diceStr.find('d')
        if dIndex == -1:  # -1 表示找不到
            raise Exception("missing a 'd'")

        # 扔几个色子 个数在 d 前面表示
        numberOfDice = diceStr[:dIndex]
        if not numberOfDice.isdecimal():
            raise Exception("Missing the number of dice")
        else:
            numberOfDice = int(numberOfDice)

        # 找到 + 或者 - 号
        modIndex = diceStr.find("+")
        if modIndex == -1:
            modIndex = diceStr.find("-")

        # 找到色子的面数
        if modIndex == -1:  # 如果没有 +  号 或者 - 号
            numberOfSides = diceStr[dIndex + 1:]
        else:
            #  有加号或者减号
            numberOfSides = diceStr[dIndex + 1: modIndex]
        if not numberOfSides.isdecimal():
            raise Exception("missing the number of sides")
        else:
            numberOfSides = int(numberOfSides)

        # 找到加几或者减几
        if modIndex == -1:
            modAmount = 0
        else:
            modAmount = diceStr[modIndex + 1:]
            if not modAmount.isdecimal():
                raise Exception("missing the number of modeAmount")
            else:
                modAmount = int(modAmount)
                if diceStr[modIndex] == "-":
                    modAmount = -modAmount

        # 模拟掷色子
        rolls = []
        for i in range(numberOfDice):
            rollResult = random.randint(1, numberOfSides)
            rolls.append(rollResult)

        # 展示结果
        total = sum(rolls) + modAmount
        print(f"{total}", end=" ")
        print("(", end="")
        for i, roll in enumerate(rolls):
            rolls[i] = str(roll)

        print(", ".join(rolls), end="")

        # 展示加或者减
        if modAmount != 0:
            modSign = diceStr[modIndex]
            print(f", {modSign}{abs(modAmount)}", end="")
        print(")")

    except Exception as e:
        print(str(e))
        continue
