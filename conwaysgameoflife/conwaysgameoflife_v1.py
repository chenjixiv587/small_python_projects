
"""
思路

1 设定 展示区域的长和高 
2 设定 块状 的生死表现状态
3 设定 所有块的初始状态 都是随机的
4 循环开始，变化块的状态
1 深度复制块
2 展示块
3 得到周边块
4 判断周边块的状态
5 根据规则判断当前块的死活
5 每 一秒变换一次

"""
import sys
import random
import time
import copy

# set the constants
WIDTH = 80
HEIGHT = 20
DEAD = chr(9786)
ALIVE = chr(9787)

# set the origin cells
nextCells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD

while True:
    print("\n" * 50)
    cells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end="")
        print()
    print("Ctrl-C to quit")

    # get all the cells neighbors

    for x in range(WIDTH):
        for y in range(HEIGHT):

            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT
            numberOfNeighborAlive = 0
            if cells[(left, above)] == ALIVE:
                numberOfNeighborAlive += 1
            if cells[(x, above)] == ALIVE:
                numberOfNeighborAlive += 1
            if cells[(right, above)] == ALIVE:
                numberOfNeighborAlive += 1
            if cells[(left, y)] == ALIVE:
                numberOfNeighborAlive += 1
            if cells[(right, y)] == ALIVE:
                numberOfNeighborAlive += 1
            if cells[(left, below)] == ALIVE:
                numberOfNeighborAlive += 1
            if cells[(x, below)] == ALIVE:
                numberOfNeighborAlive += 1
            if cells[(right, below)] == ALIVE:
                numberOfNeighborAlive += 1

            if cells[(x, y)] == ALIVE and (numberOfNeighborAlive == 2 or numberOfNeighborAlive == 3):
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numberOfNeighborAlive == 3:
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()
