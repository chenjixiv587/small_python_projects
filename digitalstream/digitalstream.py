import random
import shutil
import sys
import time

# set up the constants
MIN_STREAM_LENGTH = 6  # try changing this to 1 or 50
MAX_STREAM_LENGTH = 14  # try changing this to 100
PAUSE = 0.1  # try changing this to 0.0 or 2. 0
STREAM_CHARS = ["0", "1"]  # try changing this to other characters

# Density can range from 0.0 to 1.0
DENSITY = 0.2  # try changing this to 0.10 or 0.30

# get the size of the terminal window
WIDTH = shutil.get_terminal_size()[0]
# we can't print to the last column on windows without it adding a new
# line automatically so reduce the width by one
WIDTH -= 1

print("Digital Stream")
print("Press Ctrl-C to quit.")
time.sleep(2)

try:
    # for each column, when the counter is 0, no stream is shown,
    # otherwise, it acts as a counter for how many times a 1 or 0
    # should be displayed in that column.
    columns = [0] * WIDTH
    while True:
        # set up the counter for each column
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() <= DENSITY:
                    # restart a stream on this column
                    columns[i] = random.randint(
                        MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
            # display an empty space or a 1/0 character
            if columns[i] > 0:
                print(random.choice(STREAM_CHARS), end="+")
                columns[i] -= 1
            else:
                print(" ", end="")
        print()  # print a newline at the end of the row of columns
        sys.stdout.flush()  # make sure text appears on the screen
        time.sleep(PAUSE)
except KeyboardInterrupt:
    sys.exit()
