"""
0 1 1 2 3 5 8 13 21 34 55

"""

import sys


while True:  # the main loop
    while True:  # keep looping until the user enter the valid value
        print("Please enter the fac number..such 5, 50, 5000, QUIT to quit")
        response = input("> ").strip().upper()
        if response == "QUIT":
            print("welcome next time....")
            sys.exit()
        elif response.isdecimal() and int(response) != 0:
            facNumber = int(response)
            break
        else:
            print("Please enter again...")
            continue

    if facNumber == 1:
        print(f"the first fac number is {facNumber}")
        continue
    elif facNumber == 2:
        print(f"the second fac number is {facNumber}")
        continue

    if facNumber >= 1_000:
        print("WARNING: this will take so long time to execute....")
        print("Press CTRL_C to stop...")

    secondToLastNumber = 0
    lastNumber = 1
    fibNumbersCalculated = 2
    while True:
        nextNumber = secondToLastNumber + lastNumber
        fibNumbersCalculated += 1

        print(nextNumber)
        if fibNumbersCalculated == facNumber:
            print(f"the facNumber is {nextNumber}")
            break
        secondToLastNumber = lastNumber
        lastNumber = nextNumber
