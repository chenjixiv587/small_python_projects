import random
import time

# set up the constants
DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3  # -3 for room to enter the sum at the bottom

# the duration is in seconds
QUIZ_DURATION = 30  # this duration can change to what you want
MIN_DICE = 2  # 1 or 5 it also can be
MAX_DICE = 6  # 14 it also can be

# Reward and penalty can be change to what you want
REWARD = 4  # points award for correct answers
PENALTY = 1  # points removed for incorrect answers  can be negative number

# the program hangs if all of the dice can't fit on the screen
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

print("it is a dice game")

print(f"""Add up the sides of all the dice displayed on the screen, you have
      {QUIZ_DURATION} seconds to answer as many as possible, You get {REWARD}  
      for  each correct answer and lose {PENALTY} for each 
      incorrect answer. """)
input("Press Enter to begin ....")

# keep track of how many answers that be correct or incorrect

correctAnswers = 0
incorrectAnswers = 0
startTime = time.time()
while time.time() < startTime + QUIZ_DURATION:
    # come up with the dice to display
    sumAnswer = 0
    diceFaces = []
    for i in range(random.randint(MIN_DICE, MAX_DICE)):  # 2 - 6
        diceThrow = random.choice(ALL_DICE)  # (face, num)
        diceFaces.append(diceThrow[0])
        sumAnswer += diceThrow[1]
    # contains (x, y) tuples of the top-left corner of each diceThrow
    topLeftDiceCorners = []

    # figure out where dice should go
    for _ in range(len(diceFaces)):
        while True:
            # find a random place on the canvas to put the diceThrow
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
            # check if this diceThrow overlaps with previous dice
            overlaps = False
            for prevDiceThrowLeft, prevDiceThrowTop in topLeftDiceCorners:
                preDiceThrowRight = prevDiceThrowLeft + DICE_WIDTH
                preDiceThrowBottom = prevDiceThrowTop + DICE_HEIGHT

                # check each corner of this diceThrow to see if it is inside
                # of the area the previous diceThrow

                for cornerX, cornerY in ((topLeftX, topLeftY), (topRightX, topRightY), (bottomLeftX, bottomLeftY), (bottomRightX, bottomRightY)):

                    # 看是不是重叠 要看四个角是否在范围内
                    if (prevDiceThrowLeft <= left < preDiceThrowRight and prevDiceThrowTop <= top < preDiceThrowBottom):
                        overlaps = True

            if not overlaps:
                topLeftDiceCorners.append((left, top))
                break

    # draw the dice on the canvas
    canvas = {}
    for j, (diceThrowLeft, diceThrowTop) in enumerate(topLeftDiceCorners):
        diceThrowFace = diceFaces[j]
        for dx in range(DICE_WIDTH):
            for dy in range(DICE_HEIGHT):
                # Copy this character to the correct place on the canvas:
                canvasX = dx + diceThrowLeft
                canvasY = dy + diceThrowTop
                # Note that in diceThrowFace, a list of strings, the x and y are swapped:
                canvas[(canvasX, canvasY)] = diceThrowFace[dy][dx]
    # display the canvas on the screen
    for cy in range(CANVAS_HEIGHT):
        for cx in range(CANVAS_WIDTH):
            print(canvas.get((cx, cy), " "), end="")
        print()

    response = input("Enter the sum...").strip()
    if response.isdecimal() and int(response) == sumAnswer:
        correctAnswers += 1
    else:
        print(f"Incorrect, the answer is {sumAnswer}")
        time.sleep(2)
        incorrectAnswers += 1

# display the final score
score = correctAnswers * REWARD - incorrectAnswers * PENALTY
print(f"score is {score}")
