import sys
import time

import sevseg

try:
    while True:
        print("\n" * 60)
        currentTime = time.localtime()
        # 使用12小时制
        hours = str(currentTime.tm_hour % 12)
        if hours == "0":
            hours = "12"
        minutes = str(currentTime.tm_min)
        seconds = str(currentTime.tm_sec)

        # 获得正确的表现形式
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDigits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDigits.splitlines()

        # 展示时钟

        print(hTopRow + "   " + mTopRow + "   " + sTopRow)
        print(hMiddleRow + " * " + mMiddleRow + " * " + sMiddleRow)
        print(hBottomRow + " * " + mBottomRow + " * " + sBottomRow)
        print()
        print("Press Ctrl-C to quit")

        # 持续循环 直到秒数改变
        while True:
            time.sleep(0.01)
            if time.localtime().tm_sec != currentTime.tm_sec:
                break

        # time.sleep(1)

except KeyboardInterrupt:
    sys.exit()
