import random
import sys

BASE_MONEY = 5000


def main():
    playerOneMoney = BASE_MONEY
    playerTwoMoney = BASE_MONEY - 1000
    while True:
        if playerOneMoney <= 0 or playerTwoMoney <= 0:
            sys.exit()
        else:
            # get the debt
            print("Player1 get the bet")
            playerOneBet = getBet(playerOneMoney)
            print("player2 get the bet")
            playerTwoBet = getBet(playerTwoMoney)
            print(f"The player1 bet is {playerOneBet}")
            print(f"The player2 bet is {playerTwoBet}")
            print("--------------\n")
            # get the choice
            print("Player1 get the choice")
            playerOneChoice = getChoice()
            print("Player2 get the choice")
            playerTwoChoice = getChoice()
            print(f"The player1 choose is :{playerOneChoice}")
            print(playerTwoChoice)
            print(f"The player2 choose is :{playerTwoChoice}")
            print("--------------\n")
            # throw the dices
            dicesFirst = random.randint(1, 6)
            dicesSecond = random.randint(1, 6)
            print(f"The firstDice is {dicesFirst}")
            print(f"The secondDice is {dicesSecond}")
            if dicesFirst == 2 or dicesSecond == 2:
                playerOneMoney += 10
                playerTwoMoney -= 10
            if dicesFirst == 5 or dicesSecond == 5:
                playerTwoMoney += 15
                playerOneMoney -= 15

            dicesTogether = getDicesTogether(dicesFirst, dicesSecond)
            print(f"the dices sum is {dicesTogether}")
            guess = getGuess(dicesTogether)
            print(f"The result is {guess}")
            if guess == playerOneChoice and dicesTogether == playerTwoChoice and dicesTogether == 7:
                playerOneMoney += (playerOneBet + 70)
                playerTwoMoney += (playerTwoBet + 70)
            elif guess == playerOneChoice and dicesTogether != playerTwoChoice:
                playerOneMoney += playerOneBet + playerTwoBet
                playerTwoMoney -= playerTwoBet
            elif guess != playerOneChoice and dicesTogether == playerTwoChoice:
                playerOneMoney -= playerOneBet
                playerTwoMoney += playerTwoBet + playerOneBet
            elif guess != playerOneChoice and dicesTogether != playerTwoChoice:
                pass

            print(f"the player1 money remains {playerOneMoney}")
            print(f"the player2 money remains {playerTwoMoney}")
            print("------------------\n")
            input("Press Enter to continue....")


def getBet(maxBet: int):
    """return the bet"""
    while True:
        print(f"Please enter the bet you want (1- {maxBet}) or Q to quit")
        bet = input("> ").upper().strip()
        if bet == "Q":
            print("Thanks for playing....")
            sys.exit()
        elif not bet.isdecimal():
            print("Must be decimal bet")
            continue
        elif int(bet) > maxBet:
            print("bet can't more than money")
            continue
        else:
            bet = int(bet)
            break
    return bet


def getChoice():
    """return the choice player choose 'ODD or EVEN' """
    while True:
        print("Please give the guess, ODD or EVEN")
        choice = input().upper().strip()
        if choice == "EVEN" or choice == "ODD":
            break
        else:
            print("Please just enter ODD/EVEN")
    return choice


def getDicesTogether(dicesFirst, dicesSecond):
    sumOfDices = dicesFirst + dicesSecond
    return sumOfDices


def getGuess(sumOfDices: int):
    if sumOfDices % 2 == 0:
        return "EVEN"
    else:
        return "ODD"


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print("\nDone")
        print("Ctrl-C to terminate the program.")
