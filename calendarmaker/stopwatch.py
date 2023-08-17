import time
# display the program instruction
print("Press ENTER to begin, Afterward, Press ENTER to 'click' the stopwatch, Press Ctrl-C to quit")

input()  # Press Enter to begin

print("Started")

startTime = time.time()  # get the first lap's start time.
lastTime = startTime
lapNum = 1

# start tracking the lap times
try:
    while True:
        input()  # press enter to begin
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(
            f"Lap #{lapNum}, totalTime: {totalTime} , lapTime: {lapTime}", end='')
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # handle the Ctrl-C exception to keep its error message from displaying
    print("\nDone")
