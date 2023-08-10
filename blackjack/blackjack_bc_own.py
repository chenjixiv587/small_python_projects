"""
Let's start the 21 points game.
"""
import sys
import random
# Spades 黑桃 Hearts 红桃 Clubs 梅花 Diamonds 方块
# 9824 ♠ SPADES
# 9827 ♣ CLUBS
# 9829 ♥ HEARTS
# 9830 ♦ DIAMONDS

# prepare the cards constants

SPADES = chr(9824)
CLUBS = chr(9827)
HEARTS = chr(9829)
DIAMONDS = chr(9830)

BACKSIDE = "backside"

# The start money of player is BASE_MONEY
BASE_MONEY = 5000


def main():
    print("Welcome to the 21 points game")
    print("Rules")
    money = BASE_MONEY
    while True:  # the main game loop
        print(f"You current money is {money}")
        # if money <= 0 exit the game
        if money <= 0:
            print("U lost")
            print("Thank you for playing the game")
            sys.exit()
        # get the bet
        bet = getBet(money)
        print(f"Your bet is {bet}")

        # get the cards and show the cards
        deck = getDeck()
        playerHand = [deck.pop(), deck.pop()]
        dealerHand = [deck.pop(), deck.pop()]

        # the player begin move
        while True:  # keep looping until the player tanke the "S" or money bust
            # show the cards and points
            displayHands(playerHand, dealerHand, False)
            # if values > 21 break the loop
            if getHandValue(playerHand) > 21:
                break
            # move maybe "H" or "S" or "D"
            move = getMove(playerHand, money - bet)
            # judge the move
            if move == "D":
                additionalBet = getBet(min(bet, money - bet))
                bet += additionalBet
                print(f"Your current bet is {bet}")

            if move in ("D", "H"):
                newCard = deck.pop()

                rank, suit = newCard
                print(f"You get a new card, {rank} of {suit}")
                playerHand.append(newCard)
                if getHandValue(playerHand) > 21:
                    continue
            if move in ("S", "D"):
                break

        # It is the time for dealer to take action
        if getHandValue(dealerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                newCard = deck.pop()
                dealerHand.append(newCard)
                displayHands(playerHand, dealerHand, False)
                if getHandValue(dealerHand) > 21:
                    break
                input("Press enter to continue.")
                print("\n\n")

        # the fianal result
        displayHands(playerHand, dealerHand, True)
        playerHandValue = getHandValue(playerHand)
        dealerHandValue = getHandValue(dealerHand)

        if dealerHandValue > 21:
            print("The player won")
            money += bet
        elif playerHandValue > 21 or playerHandValue < dealerHandValue:
            print("The player lost")
            money -= bet
        elif playerHandValue > dealerHandValue:
            print("The player won")
            money += bet
        elif playerHandValue == dealerHandValue:
            print("it is a tie")

        input("Press enter to continue")
        print("\n\n")


def getBet(maxBet):
    """return the bet"""
    while True:  # keep looping until the user enters the valid bet
        bet = input(
            f"How much do you wnat to bet? (1- {maxBet}), 'QUIT' to exit the game  ").upper().strip()
        if bet == "QUIT":
            sys.exit()
        elif not bet.isdecimal():
            continue
        elif 1 <= int(bet) <= maxBet:
            bet = int(bet)
            return bet


def getDeck():
    """return cards list contains tuples(rank, suit)"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def displayHands(playerHand: list, dealerHand: list, showDealerHand: bool):
    """display the points and cards"""
    if showDealerHand:
        print(f"The value of dealer is {getHandValue(dealerHand)}")
        displayCards(dealerHand)

    else:
        print("DEALER:????")
        displayCards([BACKSIDE] + dealerHand[1:])
    print(f"The player value is {getHandValue(playerHand)}")
    displayCards(playerHand)


def displayCards(cards):
    """show the cards"""
    rows = ['']*5
    for card in cards:
        rows[0] += " ___ "
        if card == BACKSIDE:
            # Print a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front:
            rank, suit = card  # The card is a tuple data structure.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)


def getMove(playerHand: list, money: int):
    """Return the action the player take."""
    moves = ["H(its)", "S(tand)"]
    if len(playerHand) == 2 and money > 0:
        moves.append("(D)ouble down")
    movePrompt = " ,".join(moves) + "> "
    move = input(movePrompt).upper().strip()
    if move in ["H", "S"]:
        return move
    elif move == "D" and "(D)ouble down" in moves:
        return move


def getHandValue(cards: list):
    """Return the value of the cards"""
    value = 0
    numberOfAces = 0

    for card in cards:
        rank, suit = card
        if rank == "A":
            numberOfAces += 1
        elif rank in ("J", "Q", "K"):
            value += 10
        else:
            value += int(rank)
    value += numberOfAces
    while numberOfAces > 0:
        if value + 10 <= 21:
            value += 10
        numberOfAces -= 1
    return value


if __name__ == "__main__":
    main()
