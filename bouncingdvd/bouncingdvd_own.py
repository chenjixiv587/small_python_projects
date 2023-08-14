try:
    import bext
except ImportError:
    print("This program need bext please import it")

import time
import sys
import random
# set up the constants
# set up the window
WIDTH, HEIGHT = bext.size()

WIDTH -= 1
# set up the logo

COLORS = ["black", "red", "green", "yellow", "blue",
          "purple", "cyan", "white", "reset", "random"]
UP_LEFT = 'ul'
UP_RIGHT = 'ur'
DOWN_LEFT = 'dl'
DOWN_RIGHT = 'dr'
DIRECTIONS = [UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT]
DIR = 'direction'
X = 'x'
Y = 'y'
COLOR = 'color'

NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.5


def main():
    bext.clear()
    # generate the logos
    logos = []
    for _ in range(0, NUMBER_OF_LOGOS):
        logos.append({
            COLOR: random.choice(COLORS),
            X: random.randint(0, WIDTH - 4),
            Y: random.randint(0, HEIGHT - 4),
            DIR: random.choice(DIRECTIONS), })
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1

    cornerBouncingPoints = 0

    while True:
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('    ', end='')
            # at the corner will get the points
            if logo[X] == 0 and logo[Y] == 0:
                cornerBouncingPoints += 1
                logo[DIR] = DOWN_RIGHT
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                cornerBouncingPoints += 1
                logo[DIR] = UP_RIGHT

            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                cornerBouncingPoints += 1
                logo[DIR] = DOWN_LEFT
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                cornerBouncingPoints += 1
                logo[DIR] = UP_LEFT

            # when bounce the boundary, logo will go to where.
            # left edge
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            # bottom edge
            elif logo[Y] == 0 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT
            elif logo[Y] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            # right edge
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT
            # top edge
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT

            # move the logo
            if logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
        # display the score board.
        bext.goto(5, 0)
        bext.fg("white")
        print(f"cornerBounces: {cornerBouncingPoints}")

        # display the logo
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print("DVD", end="")

        bext.goto(0, 0)
        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("by ...")
        sys.exit()
