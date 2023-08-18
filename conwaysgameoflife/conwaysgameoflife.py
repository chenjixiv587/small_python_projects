import copy
import random
import sys
import time

# set up the constants
WIDTH = 80  # the width of the cell grid
HEIGHT = 20  # the weight of the cell grid

ALIVE = chr(9786)
DEAD = chr(9787)

# the cells and nextCells are dictionaries  for the state of the game
# ther keys are (x, y) tuple. and their value are one of the ALIVE or DEAD values
# this is the cells start statement
nextCells = {}
# put random dead and alive cells into nextCells
for x in range(WIDTH):  # loop over every possible column
    for y in range(HEIGHT):  # loop over every possible row
        # 50/50 chance for starting cells being alive or dead
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD

while True:  # main program loop
    # each iteration of this loop is a step of  the simulation
    print("\n" * 50)  # separate each step with new lines
    cells = copy.deepcopy(nextCells)

    # print cells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end="")  # print the cells
        print()
    print("Press Ctrl-C to quit.")

    # calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # get the neighboring coordinates of (x, y), even if they
            # wrap around the edge

            # -1 % 20 = 19
            # 这样的话  就算是边角也没有问题
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # count the number of living neighbors
            numNeighbors = 0
            if cells[(left, above)] == ALIVE:
                numNeighbors += 1  # top-left neighbor is alive
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1  # top neighbor is alive
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1  # top-right neighbor is alive
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1  # left neighbor is alive
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1  # right neighbor is alive
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1  # left-below neighbor is Alive
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1  # below neighbor is alive
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1  # bottom-right neighbor is alive

            # set cell based on Conway's Game of Life rules
            if cells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                # living cells with 2 or 3 neighbors stay alive
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive
                nextCells[(x, y)] = ALIVE
            else:
                # everything else dies or stays dead
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()
