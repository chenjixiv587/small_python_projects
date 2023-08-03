"""
猜测三个数字  
如果猜对一个数字 但是位置不对 就显示 Pico
如果猜对一个数字 位置也对 就显示 Fermi
都不对 显示 bagels
总共有 10 次机会
思路:
1 获得随机数字
2 获得玩家的输入 并判断是否符合要求
3 展示提示
4 是否继续游玩
"""

import random

NUM_DIGITS = 3  # The number of fdigits
MAX_GUESSES = 10  # The max number of guesses


def main():
    # The main loop of the game
    while True:
        secretNum = getSecretNum()

        numGuess = 1  # the number of guess times
        while numGuess <= MAX_GUESSES:
            guess = ''
            # Keep loop if not a valid number
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuess}')
                guess = input('> ')
            clues = showClues(guess, secretNum)
            print(clues)

            if guess == secretNum:
                break  # game over
            numGuess += 1
            if numGuess > MAX_GUESSES:
                print('You have try more than ten times')
                print(f'The secret num is {secretNum}')
        print('Do you want to continue, (yes or no)')
        if not input('> ').lower().startswith('y'):
            break


def getSecretNum():
    """Return the random secret num"""
    numbers = list('0123456789')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(0, NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def showClues(guess: str, secretNum: str):
    """Return the clues for player"""
    if guess == secretNum:
        return 'You got it!'
    clues = []
    for i in range(0, len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()
