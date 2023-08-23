import time
import random
import sys


PAUSE = 0.5

ROWS = [
    # 123456789 use this to measure the number of spaces
    "         ##",  # index 0 has no {}
    "        #{}-{}#",
    "       #{}---{}#",
    "      #{}-----{}#",
    "     #{}------{}#",
    "    #{}------{}#",
    "    #{}-----{}#",
    "     #{}---{}#",
    "     #{}-{}#",
    "        ##",  # index 9 has no {}
    "        #{}-{}#",
    "       #{}---{}#",
    "      #{}-----{}#",
    "     #{}------{}#",
    "    #{}------{}#",
    "    #{}-----{}#",
    "     #{}---{}#",
    "     #{}-{}#"]


try:
    print("DNA")
    print("Press Ctrl-C to quit")
    time.sleep(2)
    rowIndex = 0

    while True:
        # increment rowIndex to draw the next row
        rowIndex += 1
        # 当下标达到 ROW 的长度时 说明一圈走完 需要恢复初始状态
        if rowIndex == len(ROWS):
            rowIndex = 0
        # 下标 0 和 9 都没有 {}
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue

        # select random pairs
        randomSelection = random.randint(1, 4)
        if randomSelection == 1:
            leftContent, rightContent = "A", "T"
        elif randomSelection == 2:
            leftContent, rightContent = "T", "A"
        elif randomSelection == 3:
            leftContent, rightContent = "G", "C"
        elif randomSelection == 4:
            leftContent, rightContent = "C", "G"

        # print the row
        print(ROWS[rowIndex].format(leftContent, rightContent))

        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
