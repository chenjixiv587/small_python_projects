"""
Blackjack game
21 points game
"""
import sys
import random
# Setup the suits
HEARTS = chr(9829)  # 红心
DIAMONDS = chr(9830)  # 方片
SPADES = chr(9824)  # 黑桃
CLUBS = chr(9827)  # 梅花

BACKSIDE = 'backside'
BASE_MONEY = 5000


def main():
    print("""
Copy the blackjack game from Sweigart
    Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.
""")
    money = BASE_MONEY  # 初始资金
    while True:  # 游戏主循环开始
        # 检查资金是否已经全部输光
        if money <= 0:
            print("You are broken!")
            print("The only lucky thing is that you don't play reality")
            print("Thank you for your playing")
            sys.exit()
        else:
            print("You have the enough money, you can play the game.")

        # 玩家开始下赌注
        print(f"You have {money} dollars")
        bet = getBet(money)

        # 系统开始发牌
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # 玩家开始做选择
        print(f"The current bet is {bet}")
        while True:  # 循环玩家的动作
            # 展示得到的牌 根据牌进行下一步动作
            displayHands(playerHand, dealerHand, False)
            print()

            # 判断玩家的牌是否爆破
            if getHandValue(playerHand) > 21:
                break

            # 玩家执行动作
            move = getMove(playerHand, money - bet)
            # 不同的动作 对应不同的结果
            if move == "D":
                # 赌注加倍
                additionalBet = getBet(min(bet, money - bet))
                bet += additionalBet
                print(f"The current is now {bet}")
            if move in ("H", "D"):
                # H 或者 D 都会抽一张新牌
                newCard = deck.pop()
                rank, suit = newCard
                print(f"You drew a new card , rank is {rank}, suit is {suit}")
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    continue
            if move in ("S", "D"):
                break
        # 对电脑进行操控
        if getHandValue(dealerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # 电脑抽一张
                print("Dealer Hits")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
            input("Press enter to continue")
            print("\n\n")

        # 展示最终的结果
        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        # 比较牌的结果

        if dealerValue > 21:
            print("You win {bet}")
            money += bet
        elif playerValue > 21 or playerValue < dealerValue:
            print("You lost")
            money -= bet
        elif playerValue > dealerValue:
            print("You win")
            money += bet
        elif playerValue == dealerValue:
            print("tie")

        input("Press enter to continue")
        print("\n\n")


def getBet(maxBet: int):
    """询问玩家 下多少赌注 返回赌注是整数"""
    while True:
        print(f"How much do you want to bet (1 - {maxBet}) or QUIT")
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("BYE")
            sys.exit()
        if not bet.isdecimal():
            continue
        if 1 <= int(bet) <= maxBet:
            return int(bet)


def getDeck():
    """得到 52 张牌的花色和面值(面值, 花色)"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand: list, dealerHand: list, showDealerHand: bool):
    """展示玩家和电脑的牌和分数  展示为False 就隐藏电脑的牌"""
    if showDealerHand:
        print("DEALER: ", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER:???")
        # 显示DEALER 的牌的第一张为背面
        displayCards([BACKSIDE] + dealerHand[1:])
    # 展示玩家的牌
    print("PLAYER: ", getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards: list):
    """根据牌得到分数"""
    values = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1
        elif rank in ("J", "Q", "K"):
            values += 10
        else:
            values += int(rank)

    # 如果得到的牌 是 A 的话 默认是1 但是如果加上10 的话 没有爆破 就加10
    values += numberOfAces
    for i in range(0, numberOfAces):
        tempValue = values + 10
        if tempValue <= 21:
            values += 10
    return values


def getMove(playerHand: list, money: int):
    """询问玩家接下来的动作 H 表示再抽一张 D 表示加倍 S 表示观望"""
    while True:
        moves = ["(H)it", "(S)tand"]
        # 当第一次发牌后  玩家可以选择加倍赌注
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")

        # 玩家选择
        movePrompt = " ".join(moves) + "> "
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move
        if move == "D" and ("(D)ouble down" in moves):
            return move


def displayCards(cards: list):
    """展示牌"""
    rows = [""] * 5
    for i, card in enumerate(cards):
        rows[0] += " ___ "
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card  # The card is a tuple data structure
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, "_"))

    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
