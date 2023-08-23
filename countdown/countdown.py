import time
import sys
import digitalclock.sevseg as sevseg


print("please enter the valid seconds")
while True:  # keep looping until the user give the valid time
    seconds = input("> ").strip()
    if not seconds.isdecimal():
        print("please enter the number")
        continue
    seconds = int(seconds)
    if seconds < 0:
        print("please let the number > 0")
        continue
    else:
        break

secondLeft = seconds  # this can change to other numbers

try:
    while True:  # the main program loop
        # clear the screen by printing several newlines
        print("\n" * 60)
        # get the hours/minutes/seconds from the secondLeft
        hours = str(secondLeft // 3600)
        minutes = str((secondLeft % 3600) // 60)
        seconds = str(secondLeft % 60)

        # get the digit string from the sevseg module
        hDigits = sevseg.getSevSegStr(hours, 2)
        hTopRow, hMiddleRow, hBottomRow = hDigits.splitlines()

        mDigits = sevseg.getSevSegStr(minutes, 2)
        mTopRow, mMiddleRow, mBottomRow = mDigits.splitlines()

        sDIgits = sevseg.getSevSegStr(seconds, 2)
        sTopRow, sMiddleRow, sBottomRow = sDIgits.splitlines()

        # display the digits
        print(hTopRow + "   " + mTopRow + "   " + sTopRow)
        print(hMiddleRow + " * " + mMiddleRow + " * " + sMiddleRow)
        print(hBottomRow + " * " + mBottomRow + " * " + sBottomRow)

        if secondLeft == 0:
            print()
            print("    *****BOOM*****")
            print("enter what you want to say")
            say = input("> ").strip()
            print(say)
            break

        time.sleep(1)
        secondLeft -= 1
except KeyboardInterrupt:
    sys.exit()
