'''
循环的 一行一行 的 输出神秘代码
'''
import sys
import random
import shutil
import time


STREAM_CHARS = ["1", "0"]
MIN_STREAM_LENGTH = 50
MAX_STREAM_LENGTH = 100
PAUSE = 0.2
DENSITY = 0.02  # 字符出现的概率

WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1

columns = [0] * WIDTH
print("begin .....")
time.sleep(2)
print("Press Ctrl-C to Quit..")
try:
    while True:  # 一行一行的输出
        for i in range(WIDTH):
            # 给 column 赋值
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    columns[i] = random.randint(
                        MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)

            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end="")
                columns[i] -= 1
            else:
                print(" ", end="")
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)

except KeyboardInterrupt:
    print("quit")
    sys.exit()
