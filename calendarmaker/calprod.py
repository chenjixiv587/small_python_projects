import time


def calProd():
    # calculate the product of the first 100,000 numbers
    product = 1
    for i in range(1, 100_000):
        product *= i
    return product


startTime = time.time()
prod = calProd()
endTime = time.time()
print(f"the result is {len(str(prod))} digits long.")
print(f"took {endTime - startTime} seconds to calculate")
