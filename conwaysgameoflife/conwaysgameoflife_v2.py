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
import random
import copy
import time
import sys
# set up the constants
WIDTH = 79
HEIGHT = 20

ALIVE = chr(9632)
DEAD = chr(9633)

# set the start nextCells
nextCells = {}
with open("config.txt", "r") as f:
    content = f.readlines()
    leftNum = int(content[0].strip()[-1])
    rightNum = int(content[1].strip()[-1])
    print(leftNum, rightNum)
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.randint(leftNum, rightNum) == 1:
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD


# show the cells and change the cells
while True:
    # print the cells
    print("\n" * 50)
    cells = copy.deepcopy(nextCells)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end="")
        print()
    print("Press Ctrl-C to quit.")

    # get the position of the edge
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # judge the neighbors status
            numAliveNeighbor = 0
            if cells[(left, above)] == ALIVE:
                numAliveNeighbor += 1
            if cells[(x, above)] == ALIVE:
                numAliveNeighbor += 1
            if cells[(right, above)] == ALIVE:
                numAliveNeighbor += 1
            if cells[(left, y)] == ALIVE:
                numAliveNeighbor += 1
            if cells[(right, y)] == ALIVE:
                numAliveNeighbor += 1
            if cells[(left, below)] == ALIVE:
                numAliveNeighbor += 1
            if cells[(x, below)] == ALIVE:
                numAliveNeighbor += 1
            if cells[(right, below)] == ALIVE:
                numAliveNeighbor += 1

            # judge the nextCells
            if cells[(x, y)] == ALIVE and (numAliveNeighbor == 2 or numAliveNeighbor == 3):
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numAliveNeighbor == 3:
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()
