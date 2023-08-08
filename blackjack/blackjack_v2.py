"""
The blackjack game also known as 21 points
"""

import sys
import random


# Set up the constants (suits):
HEARTS = chr(9829)  # Character 9829 is '♥'
DIAMONDS = chr(9830)   # Cjaracter 9830 is '♦'
SPADES = chr(9824)  # Character 9824 is '♠'
CLUBS = chr(9827)  # Character 9827 is '♣'
BACKSIDE = 'backside'


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

    money = 5000
    while True:  # The main game loop
        # Check if the uer has run out of the money
        if money <= 0:
            print("You are broken!")
            print("The only lucky thing is you don't play in the reality.")
            print("Thanks for playing the game.")
            sys.exit()

        # Let the user enter his bet in this round.
        print(f"Money that you have: {money}")
        # Give the bet
        bet = getBet(money)
        # Give the dealer and player each 2 cards from the deck.
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        # 第一次发完牌 才是第一轮开始

        # Handle player actions
        print(f"The Bet is {bet}")
        while True:  # Keep loop until the player stands or busts
            displayHands(playerHand, dealerHand, False)
            print()
            # Check the player has bust
            if getHandValue(playerHand) > 21:
                break
            # Get the player's action(move) either H, S, or D
            move = getMove(playerHand, money - bet)
            # Handle the player actions
            if move == "D":
                # Player is doubling down, they can increase their bet
                additionalBet = getBet(min(bet, money-bet))
                bet += additionalBet
                print(f"Bet increase to {bet}")
                print(f"Current bet is {bet}")

            if move in ("H", "D"):
                # Hit / Doubling down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print(f"You drew a new card , {rank} of {suit}")
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue
            if move in ("S", "D"):
                # Standing / Doubling down stops the player's turn
                break
        # Handle the dealer's actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits
                print("Dealer hits")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
            input("Press enter to continue..")
            print("\n\n")
        # Show the final results
        displayHands(playerHand, dealerHand, True)
        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)
        # Hadle whether the player won lost or tied
        if dealerValue > 21:
            print(f"Dealer Busts You win {bet}")
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("You lost")
            money -= bet
        elif playerValue > dealerValue:
            print(f"You won {bet}")
            money += bet
        elif playerValue == dealerValue:
            print("It is a tie, the bet id returned to you")

        input("Press enter to continue....")
        print("\n\n")


def getBet(maxBet: int):
    """Ask the player how much they want to bet for thr round"""
    while True:  # Keep asking until they enter a valid data
        print(f"How much do you bet. (1 - {maxBet}) or QUIT.")
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Thanks for your playing.")
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # Player entered a valid bet


def getDeck():
    """Return a list of (rank, suit) tuples for all 52 cards"""
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Add the numbered cards
        for rank in ("K", "Q", "J", "A"):
            deck.append((rank, suit))  # Add the face and ace cards
    random.shuffle(deck)
    return deck


def displayHands(playerHand: list, dealerHand: list, showDealerHand: bool):
    """Show the play's and dealer's cards Hide the dealer's card when 
    showDealerHand is Fasle"""
    if showDealerHand:
        print("DEALER: ", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER:???")
        # Hide the dealer's first card
        displayCards([BACKSIDE] + dealerHand[1:])
    # Show the  player's cards
    print("PLAYER: ", getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards: list):
    """Return the value of the cards
    Face cards are worth 10 points
    aces are worth 1 or 11 points
    (This function picks the most suitable ace value)"""
    value = 0
    numOfAces = 0

    # Add the value for the non-ace cards
    for card in cards:
        rank = card[0]
        if rank == "A":
            numOfAces += 1
        elif rank in ("J", "Q", "K"):
            value += 10
        else:
            value += int(rank)
    # Add the value for the aces
    value += numOfAces  # Add one per ace
    for i in range(0, numOfAces):
        # If another 10 can be added without bust , do so
        tempValue = value + 10
        if tempValue <= 21:
            value += 10
    return value


def getMove(playerHand: list, money: int):
    """Ask the player for their move and returns 'H' for hit
    'S' for satnd, and 'D' for double down."""
    while True:  # Keep looping until the player enters a corret move
        # Determine what moves the player can make
        moves = ["(H)it", "(S)tand"]
        # The player can double down on their first move,
        # which we can tell because they'll have just exactly 2 cards.
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")

        # Get the player's move

        movePrompt = " ".join(moves) + "> "
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move
        if move == "D" and ("(D)ouble down" in moves):
            return move


def displayCards(cards: list):
    """Display all cards in the cards list """
    rows = [''] * 5
    for i, card in enumerate(cards):
        rows[0] += " ___ "
        if card == BACKSIDE:

            # print a card's back
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '

        else:
            # Print the card's front
            rank, suit = card  # The card is a tuple data structure
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, "_"))

    for row in rows:
        print(row)


# If excute the program exactly not to import
if __name__ == "__main__":
    main()
