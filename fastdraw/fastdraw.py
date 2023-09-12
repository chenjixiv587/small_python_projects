# 测试你的灵敏度

import random
import sys
import time


print("Fast Draw")
print()

input("press enter to begin....")
while True:
    print()
    print("It is high noon....")
    time.sleep(random.randint(20, 50) / 10.0)
    print("DRAW NOW!!!!!")
    drawTime = time.time()
    input()  # when you press enter it will return 按下enter键 就会执行它
    timeElapsed = time.time() - drawTime

    if timeElapsed < 0.01:
        # 如果时间小于 0.01  说明在DRAW出现之前　你就按下了　enter
        print("You drew before 'DRAW' appeared, you lose..")
    elif timeElapsed > 0.3:
        timeElapsed = round(timeElapsed, 4)
        print(f"You took {timeElapsed} seconds to draw, too slow")
    else:
        timeElapsed = round(timeElapsed, 4)
        print(f"You played the {timeElapsed} seconds to draw, you win...")

    response = input("Enter q to quit > ").strip().upper()
    if response == "Q":
        sys.exit()
