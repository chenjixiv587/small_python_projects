import random
import sys
import time


try:
    import bext
except ImportError:
    print("this program needs bext")
    sys.exit()


WIDTH = 79
HEIGHT = 22

TREE = "A"
FIRE = "W"
EMPTY = " "

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANGE = 0.01

PAUSE_LENGTH = 0.5


def main():
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)
        # run a single simulation step:
        nextForest = {
            'width': forest['width'],
            'height': forest['height'],
        }

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # if we are already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here
                    continue

                if forest[(x, y)] == EMPTY and random.random() <= GROW_CHANCE:
                    # grow a tree in this empty space
                    nextForest[(x, y)] = TREE

                elif forest[(x, y)] == TREE and random.random() <= FIRE_CHANGE:
                    nextForest[(x, y)] = FIRE

                elif forest[(x, y)] == FIRE:
                    # this tree is currently buring
                    # loop through all the neighbouring spaces
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # fire spreads to neighbouring trees.
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # the tree has burned down now so erase it
                else:
                    # just copy the existing object
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)


def createNewForest():
    """returns a dic for a new forest data structure"""
    forest = {
        'width': WIDTH,
        'height': HEIGHT,
    }

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
    return forest


def displayForest(forest):
    bext.goto(0, 0)
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg("red")
                print(FIRE, end='')
            elif forest[(x, y)] == EMPTY:
                print(EMPTY, end='')
        print()

    bext.fg('reset')  # use the default font color
    print(f"Grow chance {GROW_CHANCE * 100}%", end='')
    print(f"Lighting chance {FIRE_CHANGE * 100}%", end='')
    print("Press CTRL-C to quit")


if __name__ == "__main__":
    main()
