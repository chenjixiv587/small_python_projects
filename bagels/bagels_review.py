"""
逻辑推算游戏 猜三位数

如果提示是 Pico 那么就是 你猜的有一个数字是对的 但是位置不对
如果提示是 Fermi 那么就是 你猜的有一个数字是对的  而且位置也是对的
如果提示是 Bagels 那么你猜的都不对
你总共有十次机会
1 创建游戏主循环
2 取得随机的三位数
3 设置猜测起始值为 1 
4 while 循环 猜测的值小于设定的最大值
5 while 循环 对猜测的数字 进行判断
6 对猜测的结果进行提示
7 编写猜测结果函数
8 其实是否继续游戏
9 感谢
"""
import random

NUM_DIGITS = 3
MAX_GUESS = 10
BASE_NUM = '0123456789'


def main():

    while True:
        """THe main game loop"""

        # get the random number
        gameNum = getNum(NUM_DIGITS)

        guessTime = 1
        while guessTime <= MAX_GUESS:
            guess = ''
            while len(guess) == 0 or guess.isdecimal() is None:
                print(f'Guess #{guessTime}')
                guess = input('> ')
            guessTime += 1

            clues = getClues(guess, gameNum)
            print(clues)

            if guess == gameNum:
                break
            if guessTime > MAX_GUESS:
                print(f'{gameNum}')
                print(f'{guessTime}')
        print('Do you want to play again?')
        if not input().lower().startswith('y'):
            break
    print("Thank u")


def getNum(num):
    """Return the random number"""
    number = list(BASE_NUM)
    guessNum = ''
    for i in range(0, num):
        index = random.randint(0, len(number)-1)
        guessNum += number[index]
    return guessNum


def getClues(guess, gameNum):
    if guess == gameNum:
        return 'Good Job'
    clues = []
    for i in range(0, len(guess)):
        if guess[i] == gameNum[i]:
            clues.append('Fermi')
        elif guess[i] in gameNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:

        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()
