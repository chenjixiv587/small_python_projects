"""
一行一行 输出神秘代码

"""
import time
import sys
import random
import shutil

STREAM_CHARS = ["B", "R", "U", "C", "E"]
MIN_STREAM_LENGTH = 6
MAX_STREAM_LENGTH = 14

DENSITY = 0.02  # 密集程度 也就是可以展现神秘代码的概率
PAUSE = 0.1

WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1  # 为了更好的显示效果 去除最右边的长度

# 每个列的初始值 为 0 就是表示的是 “ ”
columns = [0] * WIDTH
print("begin...")
time.sleep(2)
try:
    while True:  # 一行一行的输出
        for i in range(WIDTH):
            # 每列输出一个
            # 初始必定经历这步
            # 设置每列的值
            if columns[i] == 0:
                if random.random() < DENSITY:
                    columns[i] = random.randint(
                        MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)

            # 展示每列
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end="")
                columns[i] -= 1
            else:
                print(" ", end="")
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)

except KeyboardInterrupt:
    print("bye")
    sys.exit()
