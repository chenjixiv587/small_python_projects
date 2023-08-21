"""
自动滚动效果模拟
"""
# set the constants
import time
import sys
import random

WIDTH = 70
PAUSE_AMOUNT = 0.2


def main():
    print("Press CTRL-C to QUIT")
    time.sleep(2)
    leftWidth = 20
    gapWidth = 10

    while True:

        rightWidth = WIDTH - leftWidth - gapWidth
        print((chr(9786) * leftWidth) +
              (" " * gapWidth) + (chr(9787) * rightWidth))

        try:
            time.sleep(PAUSE_AMOUNT)
        except KeyboardInterrupt:
            sys.exit()

        # change the leftWidth and gapWidth
        diceRoll = random.randint(1, 6)
        if diceRoll == 1 and leftWidth > 1:
            leftWidth -= 1
        elif diceRoll == 2 and leftWidth - gapWidth < WIDTH - 1:
            leftWidth += 1
        else:
            pass

        diceRoll = random.randint(1, 6)
        if diceRoll == 2 and gapWidth > 1:
            gapWidth -= 1
        elif diceRoll == 3 and leftWidth - gapWidth < WIDTH - 1:
            gapWidth += 1
        else:
            pass


if __name__ == "__main__":
    main()
