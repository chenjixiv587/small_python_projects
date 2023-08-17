import time


def main():

    print("Press ENTER to start, afterwards press ENTER to 'click' the stop watch")

    input()

    print("Start")

    startTime = time.time()
    lastTime = startTime
    lapNum = 1

    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(
            f"lapNum: # {lapNum}, lapTime: {lapTime},  totalTime: {totalTime}")
        lapNum += 1
        lastTime = time.time()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nDone")
