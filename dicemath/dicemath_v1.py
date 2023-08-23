import random
import time

# set up the constants
DICE_WIDTH = 9
DICE_HEIGHT = 5

CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3  # -3 for room to enter the sum at the bottom


# the duration
QUIZ_DURATION = 30  # seconds
MIN_DICE = 2
MAX_DICE = 6


REWARD = 4
PENALTY = 1


assert MAX_DICE <= 14

D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)


ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]

print(f"""
Add up the sides of all the dice played on the screen,
      you have {QUIZ_DURATION} seconds to answer as many as possible,
      you get {REWARD} points when you give the correct answers, you get 
      {PENALTY} if you get incorrect answers.""")
input("Press Enter to go on ..")

# keep tacck of how many answers were correct and incorrect
correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
while time.time() < QUIZ_DURATION + startTime:
    # come up with the dice to display
    sumAnswer = 0
    diceFaces = []
    # get the die of every time throw
    for i in range(random.randint(MIN_DICE, MAX_DICE)):  # (2, 6)
        die = random.choice(ALL_DICE)
        face = die[0]
        diceFaces.append(face)
        num = die[1]
        sumAnswer += num

    # contains (x, y) tuples of the top-left corner of each die
    # 记录左上角就可以确定四个角
    topLeftDiceCorners = []

    # figure out where dice should go:
    for i in range(len(diceFaces)):
        while True:
            # the origin (left, top ) of the dice
            left = random.randint(0, CANVAS_WIDTH - 1 - DICE_WIDTH)
            top = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

            # the four corners
            topLeftX = left
            topLeftY = top

            topRightX = left + DICE_WIDTH
            topRightY = top

            bottomLeftX = left
            bottomLeftY = top + DICE_HEIGHT

            bottomRightX = left + DICE_WIDTH
            bottomRightY = top + DICE_HEIGHT

            # check if this die overlaps with previous dice
            overlaps = False

            for prevDieLeft, prevDieTop in topLeftDiceCorners:
                # x 范围 prevDieLeft 到 prevDieRight
                # y 范围 prevDieTop 到 prevDieBottom
                prevDieRight = prevDieLeft + DICE_WIDTH
                prevDieBottom = prevDieTop + DICE_HEIGHT
                for cornerX, cornerY in ((topLeftX, topLeftY), (topRightX, topRightY), (bottomLeftX, bottomLeftY), (bottomRightX, bottomRightY)):

                    # 看是不是重叠 要看四个角是否在范围内
                    if (prevDieLeft <= left < prevDieRight and prevDieTop <= top < prevDieBottom):
                        overlaps = True

            # 第一个肯定会加入
            if not overlaps:
                topLeftDiceCorners.append((left, top))
                break

    canvas = {}
    for i, (dieLeft, dieTop) in enumerate(topLeftDiceCorners):
        dieFace = diceFaces[i]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                canvasX = dieLeft + dx
                canvasY = dieTop + dy

                canvas[(canvasX, canvasY)] = dieFace[dy][dx]
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), " "), end="")
        print()
    # Let the player enter their answer:
    response = input('Enter the sum: ').strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswers += 1
    else:
        print('Incorrect, the answer is', sumAnswer)
        time.sleep(2)
        incorrectAnswers += 1

# Display the final score:
score = (correctAnswers * REWARD) - (incorrectAnswers * PENALTY)
print('Correct:  ', correctAnswers)
print('Incorrect:', incorrectAnswers)
print('Score:    ', score)
