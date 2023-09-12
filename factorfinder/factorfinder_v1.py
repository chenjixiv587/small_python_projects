import sys
import math


while True:
    # 询问用户 获得正确的数字
    print("Please give a positive number")
    response = input("> ").strip().upper()
    if response == "Q":
        print("BYE")
        sys.exit()
    elif not (response.isdecimal() and int(response) > 0):
        continue
    else:
        number = int(response)

    factors = []
    for i in range(1, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)

    factors = list(set(factors))
    factors.sort()

    for i, factor in enumerate(factors):
        factors[i] = str(factor)
    print(", ".join(factors))
