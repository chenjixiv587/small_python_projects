import math
import sys

while True:
    print("please enter the positive number to get th factors of it")
    response = input("> ").strip().upper()
    if response == "Q":
        print("Bye")
        sys.exit()
    elif not response.isdecimal():
        continue
    elif int(response) < 0:
        continue
    else:
        number = int(response)

    factors = []

    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)

    # 去重
    factors = list(set(factors))
    factors.sort()

    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(" ".join(factors))
