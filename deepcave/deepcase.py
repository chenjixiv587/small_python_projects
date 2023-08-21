import random
import sys
import time

# set up the constants
WIDTH = 70  # can be 10 or 30
PAUSE_AMOUNT = 0.2  # can be 0 or 1.0

print("Press Ctrl-C to quit.")
time.sleep(2)

leftWidth = 20
gapWidth = 10
while True:
    # display the tunnel segment
    rightWidth = WIDTH - leftWidth - gapWidth
    print(("#" * leftWidth) + (" " * gapWidth) + ("#" * rightWidth))

    # check for pressing ctrl-c to quit
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        print("QUIT")
        sys.exit()

    # adjust the leftWidth
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth -= 1  # decrease leftWidth
    elif diceRoll == 2 and ((leftWidth + gapWidth) < WIDTH - 1):
        leftWidth += 1  # increase leftWidth
    else:
        pass

    # adjust the gap width
    if diceRoll == 1 and gapWidth > 1:
        gapWidth -= 1
    elif diceRoll == 2 and ((leftWidth + gapWidth) < WIDTH - 1):
        gapWidth += 1
    else:
        pass


# def adjustWidth(width):
#     diceRoll = random.randint(1, 6)
#     if diceRoll == 1 and width > 1:
#         width -= 1  # decrease leftWidth
#     elif diceRoll == 2 and ((leftWidth + gapWidth) < WIDTH - 1):
#         width += 1  # increase leftWidth
#     else:
#         pass
