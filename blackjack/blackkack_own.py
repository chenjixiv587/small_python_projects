"""
blackkack 21 points game
"""

import sys
import random
BASE_MONEY = 5000

# Set the constants

# 9829 ♥
# 9830 ♦
# 9824 ♠
# 9827 ♣
HEART = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

BACKSIDE = "backdide"


def main():
    money = BASE_MONEY
    print("Welcome to the 21 points game!")
    print("""Rules:
          when the player money is <= 0 , terminted the game.
          the first time, system will give each two cards.
          the first round, you can hit, stand, and double down.
          J Q K means value of 10.
          2 - 10 means themsefl.
          A means 1 or 11.
          when player stand means do nothing.
          when hit or double down ,all get new card.
          when one point > 21, break the loop
""")
    while True:  # The main game loop
        # if the player's money <= 0, game over, sys.exit()
        print(f"Your current money is {money}")
        if money <= 0:
            print("Sorry you have no money left")
            print("You are so lucky that you didn't play it in the reality")
            sys.exit()

        # player give the game bet
        bet = getBet(money)
        print(f"Your current bet is {bet}")

        # give each the two cards from the deck
        deck = getDeck()
        playerHand = [deck.pop(), deck.pop()]
        dealerHand = [deck.pop(), deck.pop()]

        # when get the cards, the player need to take action. (Hit Stand Double...)
        while True:  # keep looping until player take stand or bust
            # show the cards and points of each other
            displayHands(playerHand, dealerHand, False)
            print()

            if getHandValue(playerHand) > 21:
                break

            move = getMove(playerHand, money - bet)
            if move == "D":
                additionalBet = getBet(min(bet, money - bet))
                bet += additionalBet
                print(f"The current bet is {bet}")
            # whether D or H , all get a new card
            if move in ("H", "D"):
                newCard = deck.pop()
                rank, suit = newCard
                print(f"You get a new card, {rank} of {suit}")
                playerHand.append(newCard)
                displayHands(playerHand, dealerHand, False)
                if getHandValue(playerHand) > 21:
                    continue
            if move in ("S", "D"):
                break

        # the dealer should take actions now
        if getHandValue(dealerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                newCard = deck.pop()
                dealerHand.append(newCard)
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input("Press enter to continue...")
                print("\n\n")

        # last compare the points
        displayHands(playerHand, dealerHand, True)
        playerPoints = getHandValue(playerHand)
        dealerPoints = getHandValue(dealerHand)

        if dealerPoints > 21:
            print("The player won")
            money += bet
        elif playerPoints > 21 or (playerPoints < dealerPoints):
            print("You lost")
            money -= bet
        elif playerPoints == dealerPoints:
            print("It is a tie, money will return to you.")

        input("Press enter to continue...")
        print("\n\n")


def getBet(maxBet: int):
    """return  the player bet according the maxBet"""
    while True:  # keep looping until the bet is valid
        print(f"You should give a bet, (1- {maxBet}) or QUIT ")
        bet = input("> ")
        if bet == "QUIT":
            sys.exit()
        elif not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    """Return the list of cards that contains tuples(rank, suit)"""
    deck = []
    for suit in (HEART, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):  # the numbered card
            deck.append((str(rank), suit))
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))  # the face card and ace
    random.shuffle(deck)
    return deck


def getMove(playerHand, money):
    """return the move """
    while True:  # keep looping until player enter a valid data
        moves = ["H(its)", "(S)tand"]
        # if the first round and money > 0, can D
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")
        movePromopt = " ".join(moves) + "> "
        move = input(movePromopt).upper().strip()
        if move in ("H", "S"):
            return move
        elif move == "D" and "(D)ouble down" in moves:
            return move


def displayHands(playerHand, dealerHand, showDealerHand):
    """show the cards and points """
    print()

    if showDealerHand:
        print("DEALER: ", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER: ???")
        displayCards([BACKSIDE] + dealerHand[1:])
    print("PLAYER: ", getHandValue(playerHand))
    displayCards(playerHand)


def displayCards(cards):
    """Display all the card in the list"""
    rows = [""] * 5
    for card in cards:
        rows[0] += " ___ "
        if card == BACKSIDE:
            # Print a card's back:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card

            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)


def getHandValue(cards):
    """Retrun the points of the cards"""
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == "A":
            numberOfAces += 1
        elif rank in ("J", "Q", "K"):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(0, numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value


if __name__ == "__main__":
    main()
