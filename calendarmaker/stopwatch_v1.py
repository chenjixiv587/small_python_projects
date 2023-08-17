import time

print("Press ENTER to start, afterwards press ENTER to 'click' the stop watch")
input()
print("Start")
startTime = time.time()
lastTime = startTime  # last time is the start of the next lap
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f"lapNum: #{lapNum}, lapTime: {lapTime}, totalTime: {totalTime}")
        lastTime = time.time()
        lapNum += 1

except KeyboardInterrupt:
    print("\n Ctrl-C to quit..")
    print("\nDone")
