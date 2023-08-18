"""
1. If n is even, the next number n is n / 2.
2. If n is odd, the next number n is n * 3 + 1.
3. If n is 1, stop. Otherwise, repeat
"""
import sys
print("Please give a number, we will show you the process to change it to 1")

# get the valid number
while True:
    number = input("> ").strip()
    if not number.isdecimal():
        print("Please give a number")
        continue
    number = int(number)
    if number > 0:
        break
    else:
        print("number must more than 0")
        continue
print(number)
count = 0

while True:
    count += 1
    if number == 1:
        break
    elif number % 2 == 0:
        number /= 2
        print(int(number))
    else:
        number = number * 3 + 1
        print(int(number))


print(f"the total amount of number is {count}")
