import sys
import random
import time
try:
    import bext
except ImportError:
    print("This program needs module bext")
    sys.exit()

# set the width, height of the show window
WIDTH, HEIGHT = bext.size()

WIDTH -= 1


NUMBERS_OF_LOGOS = 5
PAUSE_AMOUNT = 0.2
COLORS = ["red", "green", "random"]
# Directions
UP_RIGHT = "ur"
UP_LEFT = "ul"
DOWN_LEFT = "dl"
DOWN_RIGHT = "dr"

DIRECTIONS = (UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT)

# key name of a logo (a logo is a dictionary)
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    # clear the window
    bext.clear()

    # generate some logos
    logos = []
    for _ in range(0, NUMBERS_OF_LOGOS):
        logos.append(
            {COLOR: random.choice(COLORS),
             X: random.randint(1, WIDTH-4),
             Y: random.randint(1, HEIGHT - 4),
             DIR: random.choice(DIRECTIONS), }
        )
        # make sure each logo X is even, then it can hit the corner

        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1
    cornerBounces = 0
    while True:
        # erase the logo's current location
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print("   ", end='')

            originalDirection = logo[DIR]

            # see if the logo bounces off the corner
            if logo[X] == 0 and logo[Y] == 0:
                cornerBounces += 1
                logo[DIR] = DOWN_RIGHT
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                cornerBounces += 1
                logo[DIR] = UP_RIGHT
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                cornerBounces += 1
                logo[DIR] = DOWN_LEFT
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                cornerBounces += 1
                logo[DIR] = UP_LEFT
            # see if the logo bounces the bountries.

            # see if the logo bounces off the left edge
            if logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # see if the logo bounces off the bottom edge
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            # see if the logo bounces off the right dege

            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT

            # see if the logo bounces off the top edge
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            if logo[DIR] != originalDirection:
                # change color when the logo bounces
                logo[COLOR] = random.choice(COLORS)

            # move the logo by the different direction
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

        # display the number of the corner bounces
        bext.goto(5, 0)
        bext.fg("white")
        print("Corner bounces: ", cornerBounces, end="")

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
        print("Bouncing DVD logo, by...")
        sys.exit()
