import sys

# Create the next number by adding the previous three numbers instead
# of the previous two.
# 0 1 1 2 4 7 13 24
while True:  # the main loop
    while True:  # keep looping until the user enter the valid data
        print("Please enter the valid data, QUIT to quit the program....")
        response = input("> ").strip().upper()
        if response == "QUIT":
            print("Welcome Next Time")
            sys.exit()
        elif not response.isdecimal() or int(response) <= 0:
            print("please enter the valid data...")
            continue
        else:
            fibNumber = int(response)
            break
    print(f"You want to get the fib number is {fibNumber}")

    if fibNumber == 1:
        print(f"the fib number of {fibNumber} is 0")
        continue
    elif fibNumber == 2:
        print(f"the fib number of {fibNumber} is 1")
    elif fibNumber == 3:
        print(f"the fib number of {fibNumber} is 1")
    elif fibNumber >= 1_0000:
        print("the number is so big, will need much time,")
        print("you can CTRL-C to quit..")

    # 初始位置
    secondToLast = 0
    middleNumber = 1
    lastNumber = 1
    fibNumberCalculated = 3

    while True:
        nextNumber = secondToLast + lastNumber + middleNumber
        fibNumberCalculated += 1
        if fibNumberCalculated == fibNumber:
            print(f"the fib number is {nextNumber}")
            break
        secondToLast = middleNumber
        middleNumber = lastNumber
        lastNumber = nextNumber
