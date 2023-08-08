"""
21 Points Game copy from Al Sweigart by Bruce Chen
"""

import sys
import random

# Set up the constants:
HEARTS = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES = chr(9824)  # Character 9824 is '♠'.
CLUBS = chr(9827)  # Character 9827 is '♣'.

BACKSIDE = 'backside'

START_MONEY = 5000

FACE_CARDS = ("J", "Q", "K", "A")


def main():
    money = START_MONEY
    while True:
        """The main game loop"""
        # when the money is less than 0 or equal to 0
        # the main loop will terminted
        print(f"Your current money is {money}")
        if money <= 0:
            print("You have no money")
            print("Bye Bye")
            sys.exit()

        # give the bet
        bet = getBet(money)
        print(f"Your current bet is {bet}")

        # create the deck and throw the cards
        deck = getDeck()
        # The cards are list of 2 tuples in it (rank, suit)
        playerHand = [deck.pop(), deck.pop()]
        dealerHand = [deck.pop(), deck.pop()]

        # player begin move
        while True:
            """Player begin move until player stand or bust"""
            displayHand(playerHand, dealerHand, False)
            # because we can't know the dealer's point so
            # we just know when player bigger than 21
            # we terminted the current loop
            if getHandValue(playerHand) > 21:
                break
            # begin move
            move = getMove(playerHand, money - bet)
            if move == "D":
                additionalBet = min(bet, money - bet)
                bet += additionalBet
                print(f"Your current bet is {bet}")
            if move in ("H", "D"):
                newCard = deck.pop()
                playerHand.append(newCard)
                displayHand(playerHand, dealerHand, False)
                if getHandValue(playerHand) > 21:
                    break
            # S means do nothing so we choose break
            if move in ("S", "D"):
                break

        # dealer begin move
        if getHandValue(dealerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Dealer Hits....")
                dealerHand.append(deck.pop())
                displayHand(playerHand, dealerHand, False)
                if getHandValue(dealerHand) > 21:
                    break
                input("Press enter to continue...")
                print("\n\n")

        # show the results
        displayHand(playerHand=playerHand,
                    dealerHand=dealerHand, showDealerHand=True)
        # get the points of the player and dealer
        playerHandValue = getHandValue(playerHand)
        dealerHandValue = getHandValue(dealerHand)

        if dealerHandValue > 21:
            print("You win!")
            money += bet
        elif playerHandValue > 21 or playerHandValue < dealerHandValue:
            print("You lost")
            money -= bet
        elif playerHandValue > dealerHandValue:
            print("You win ")
            money += bet
        elif playerHandValue == dealerHandValue:
            print("It is tie")

        input("Press enter to continue...")
        print("\n\n")


def getBet(maxBet: int):
    """return the valid bet """
    while True:  # Keep looping until the player enter the valid data
        print(
            f"how much do you want to bet in the game? bet between (1- {maxBet}) or QUIT")
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Bye Welcome next time to play.")
            sys.exit()
        if not bet.isdecimal():
            print("You don't enter the valid data, please enter again")
            break
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def getDeck():
    """Return a list of cards that fill with tuples (rank, suit)"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        # numbered cards
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        # face cards and ace
        for rank in FACE_CARDS:
            deck.append((rank, suit))
    # make deck random
    random.shuffle(deck)
    return deck


def displayHand(playerHand: int, dealerHand: int, showDealerHand: bool):
    """Display the points and cards."""
    # display the dealer info
    if showDealerHand:
        print(f"The dealer ponits is: {getHandValue(dealerHand)}")
        displayCards(dealerHand)
    else:
        print("DEALER:???")
        displayCards([BACKSIDE] + dealerHand[1:])
    # display the player info
    print(f"The player ponits is: {getHandValue(playerHand)}")
    displayCards(playerHand)


def displayCards(cards: list):
    """Display all the cards in the cards list."""
    rows = ['', '', '', '', '']  # The text to display on each row.

    for i, card in enumerate(cards):
        rows[0] += ' ___  '  # Print the top line of the card.
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

    # Print each row on the screen:
    for row in rows:
        print(row)


def getHandValue(cards: list):
    """return the points of the cards"""
    value = 0  # the origin value
    numberOfAces = 0
    for i, card in cards:
        rank, suit = card
        if rank == "A":
            numberOfAces += 1
        elif rank in ("J", "k", "Q"):
            value += 10
        else:
            value += int(rank)

    # value += numberOfAces # add 1 per ace
    # for i in range(0, numberOfAces):
    #     tempValue = value + 10:
    #     if tempValue <= 21:
    #         value += 10

    if numberOfAces > 0:
        value += numberOfAces
        for i in range(0, numberOfAces):
            tempValue = value + 10
            if tempValue <= 21:
                value += 10
    return value


def getMove(playerHand: list, money: int):
    """return S H D 
        pay attention that only the first round can player do D 
    """
    while True:  # keep looping until the player give a correct move.
        moves = ["H", "S"]
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")

        movePrompt = " ".join(moves) + "> "
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move
        if move == "D" and "(D)ouble down" in moves:
            return move


if __name__ == "__main__":
    main()
