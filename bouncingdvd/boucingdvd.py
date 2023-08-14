"""Bouncing DVD
The DVD logo swims in the screen...
"""

import sys
import random
import time


try:
    import bext
except ImportError as e:
    print("This program need bext module")
    sys.exit()


# Set up the costants
WIDTH, HEIGHT = bext.size()

# We can't print to the last column on Windows without it
# adding a newline automatically, so reduce the width by one:
WIDTH -= 1

NUMBERS_OF_LOGOS = 5  # This can change anytime
PAUSE_AMOUNT = 0.2  # This can change anytime
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta',
          'cyan', 'white']  # This can change anytime
UP_RIGHT = "ur"
UP_LEFT = "ul"
DOWN_RIGHT = "dr"
DOWN_LEFT = "dl"
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)
# Key names for logo dictionaries
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'


def main():
    bext.clear()

    # Generate some logos
    logos = []
    for i in range(0, NUMBERS_OF_LOGOS):
        logos.append({
            COLOR: random.choice(COLORS),
            X: random.randint(1, WIDTH - 4),
            Y: random.randint(1, HEIGHT - 4),
            DIR: random.choice(DIRECTIONS),
        })

        if logos[-1][X] % 2 == 1:
            # Make sure X is even so it can hit the corner
            logos[-1][X] -= 1

    cornerBounces = 0  # Count how many times a logo hits a corner
    while True:  # The main loop
        for logo in logos:
            # Erase the logo's current location.
            bext.goto(logo[X], logo[Y])
            print("   ", end="")  # (!) Try commenting this line out

            originalDirection = logo[DIR]

            # See if the logo bounces off the corners
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] == DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1
            # see if the logo bounces off the left edge
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # see if the logo bounces off the right edge
            # (WIDTH -3 because 'DVD'  has 3 letters)
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # see if the logo bounces off the top  edge
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT
            # see if the logo bouces off the bottom edge
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] == UP_RIGHT

            if logo[DIR] != originalDirection:
                # change color when the logo bounces
                logo[COLOR] = random.choice(COLORS)

            # move the logo.(X moves by 2 because the terminal )
            # characters are twice as tall as they are wide.
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # display the number of the corner bounces
        bext.goto(5, 0)
        bext.fg('white')
        print("Corner bounces: ", cornerBounces, end='')

        for logo in logos:
            # draw the logos at their new location:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print("DVD", end='')
        bext.goto(0, 0)

        sys.stdout.flush()  # (required for bext-using programs)
        time.sleep(PAUSE_AMOUNT)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        print("Bouncing DVD logo, by ,,,")
        sys.exit()