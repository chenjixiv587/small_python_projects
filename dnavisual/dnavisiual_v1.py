import random
import sys
import time
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

print("DNA begin")
time.sleep(2)
rowIndex = 0
PAUSE = 0.15
try:

    while True:
        rowIndex += 1
        if rowIndex == len(ROWS):
            rowIndex = 0
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue
        choice = random.randint(1, 4)
        if choice == 1:
            left, right = "A", "T"
        elif choice == 2:
            left, right = "T", "A"
        elif choice == 3:
            left, right = "G", "C"
        elif choice == 4:
            left, right = "C", "G"

        print(ROWS[rowIndex].format(left, right))
        time.sleep(PAUSE)

except KeyboardInterrupt:
    print("Quit")
    sys.exit()
