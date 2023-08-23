import random
import time

# 需要在循环之后得到结果的变量 不要在循环里面定义

DICE_WIDTH = 9
DICE_HEIGHT = 5

CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3

QUIZ_DURATION = 10  # seconds

MIN_DICE = 2
MAX_DICE = 6

REWARD = 4
LOSE = 1

# Dice
D1 = (["+-------+",
       "|       |",
       "|   @   |",
       "|       |",
       "+-------+"], 1)
D2a = (["+-------+",
        "| @     |",
        "|       |",
        "|     @ |",
        "+-------+"], 2)
D2b = (["+-------+",
        "|    @  |",
        "|       |",
        "| @     |",
        "+-------+"], 2)
D3a = (["+-------+",
        "|     @ |",
        "|   @   |",
        "|@      |",
        "+-------+"], 3)
D3b = (["+-------+",
        "| @     |",
        "|   @   |",
        "|     @ |",
        "+-------+"], 3)
D4 = (["+-------+",
       "|  @@   |",
       "|       |",
       "|   @@  |",
       "+-------+"], 4)
D5 = (["+-------+",
       "| @   @ |",
       "|   @   |",
       "|  @ @  |",
       "+-------+"], 5)
D6a = (["+-------+",
        "|  @  @ |",
        "|  @  @ |",
        "|  @  @ |",
        "+-------+"], 6)
D6b = (["+-------+",
        "| @ @ @ |",
        "| @ @ @ |",
        "|       |",
        "+-------+"], 6)


ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]
print("game begin......")
input("Press enter to begin.....")
startTime = time.time()
correct = 0
incorrect = 0
while time.time() < startTime + QUIZ_DURATION:

    # 投色子  个数在 2 到 6 之间
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):
        dice = random.choice(ALL_DICE)
        diceFaces.append(dice[0])
        sumAnswer += dice[1]

    # 确认色子位置
    appearDice = []
    for i in range(len(diceFaces)):
        while True:

            # 设置色子的初始位置 默认为左上角
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            # 色子位置的四个角
            leftTopX = left
            leftTopY = top

            rightTopX = left + DICE_WIDTH
            rightTopY = top

            leftBottomX = left
            leftBottomY = top + DICE_HEIGHT

            rightBottomX = left + DICE_WIDTH
            rightBottomY = top + DICE_HEIGHT

            # 判断后一个色子是否和前一个重叠
            # 第一个必定不重叠
            overlap = False

            for prevDieLeft, prevDieTop in appearDice:
                prevDieRight = prevDieLeft + DICE_WIDTH
                prevDieBottom = prevDieTop + DICE_HEIGHT

                for cornerX, cornerY in ((leftTopX, leftTopY), (rightTopX, rightTopY), (leftBottomX, leftBottomY), (rightBottomX, rightBottomY)):
                    if prevDieLeft <= cornerX < prevDieRight and prevDieTop <= cornerY < prevDieBottom:
                        overlap = True

            if not overlap:
                appearDice.append((left, top))
                break

    # 把色子画到画布中
    canvas = {}
    for i, (dieLeft, dieTop) in enumerate(appearDice):

        dieFace = diceFaces[i]
        for dy in range(DICE_HEIGHT):
            for dx in range(DICE_WIDTH):
                cx = dieLeft + dx
                cy = dieTop + dy
                canvas[(cx, cy)] = dieFace[dy][dx]
    # 展示画布
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), " "), end="")
        print()

    # 回答问题

    print("the sum of the dices is ?")
    while True:
        response = input("> ").strip()
        if response.isdecimal() and int(response) > 0:
            break
        else:
            print("Must be number")
            continue
    if int(response) == sumAnswer:
        correct += 1
    else:
        print(f"incorrect, the correct is {sumAnswer}")
        incorrect += 1
        time.sleep(2)

score = REWARD * correct - LOSE * incorrect
print(f"the correct time is: {correct}")
print(f"the incorrect time is {incorrect}")
print(f"score is {score}")
