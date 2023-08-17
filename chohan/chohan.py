"""
even 偶数
odd 奇数

掷色子游戏  

有两个色子  扔一次 判断两个色子的和是奇数还是偶数

1 定义你拥有多少钱
2 游戏主循环开始  没有钱 就结束游戏
3 下注  注意需要循环判断
4 掷色子， 得到和
和是偶数赢 
5 计算还剩多少钱
"""


import sys
import random


def main():
    money = 5000

    while True:  # the main game loop
        print(f"Your current money is {money}")
        if money <= 0:
            sys.exit()
        else:
            # 下注
            print("How much do you want to bet, or QUIT to quit")
            bet = getBet(money)
            print(f"Your current bet is {bet}")
            # 压奇数还是偶数
            print("Please guess odd or even")
            choose = getChoose()
            print(f"Your choose is {choose}")
            # 比较结果
            print("Now throw the dices")
            sumDices = getDiceSum()
            print(f"The result is {sumDices}")
            if sumDices == choose:
                print("you win")
                money += bet
            else:
                print("you lose")
                money -= bet

            print(f"Your current money is {money}")

            print("Do you want to play again? Y/N")
            while True:
                playAgain = input().upper().strip()
                if playAgain.startswith("Y") or playAgain.startswith("N"):
                    break
                else:
                    print("Just can enter Y or N")
            if playAgain == "Y":
                continue
            else:
                print("Thank for playing")
                sys.exit()


def getChoose():
    """Return the player choose odd or even"""

    while True:  # keep looping until player give the valid bet
        choose = input().strip().upper()
        if choose == "ODD" or choose == "EVEN":
            break
        else:
            print("Just accept odd or even")
            continue

    return choose


def getBet(money: int):
    """Return the bet"""

    while True:  # keep looping until player give the valid bet
        bet = input("> ").strip().upper()
        if not bet.isdecimal():
            print("Just give the numeric bet")
            continue
        elif bet == "QUIT":
            sys.exit()
        bet = int(bet)
        if 0 < bet <= money:
            break
        else:
            print(f"should <= {money}")
            continue
    return bet


def getDiceSum(money: int):
    """Return the sum of the two dices"""
    diceOne = random.randint(1, 6)
    diceTwo = random.randint(1, 6)
    sumDices = diceOne + diceTwo
    if sumDices % 2 == 0:
        return "EVEN"
    else:
        if sumDices == 7:
            money += 10
        return "ODD"


if __name__ == "__main__":
    main()
