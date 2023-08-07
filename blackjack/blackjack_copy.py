"""
Blackjack game always we also call 21 ponits game.

"""
import sys
import random


# Set up the constants:
HEARTS = chr(9829)  # Character 9829 is '♥'
DIAMONDS = chr(9830)  # Cjaracter 9830 is '♦'
SPADES = chr(9824)  # Character 9824 is '♠'
CLUBS = chr(9827)  # Character 9827 is '♣'

BACKSIDE = 'backside'


def main():
    print('''Copy the blackjack game from Sweigart
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
    The dealer stops hitting at 17.''')

    money = 5000
    while True:  # Main game loop
        # Check if the user has run out of money.
        if money <= 0:
            print('You are broke!')
            print("The only fortunate thing is you weren't play the true game")
            print("Thanks for playing")
            sys.exit()
        # Let the user enter his bet in this round
        print(f'Money: {money}')
        bet = getBet(money)

        # Give the dealer and player each 2 cards from the deck
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player actions
        print(f'Bet: {bet}')
        while True:  # Keep loop until the player stands or busts
            displayHands(playerHand, dealerHand, False)
            print()
            # Check the player has bust
            if getHandValue(playerHand) > 21:
                break
            # Get the player's action(move), either H, S, or D
            move = getMove(playerHand, money - bet)
            # Handle the player actions
            if move == "D":
                # Player id doubling down, they can increase their bet
                additionalBet = getBet(min(bet, (money - bet)))
                bet += additionalBet
                print(f"Bet increased to {bet}")
                print(f"Bet :{bet}")
            if move in ('H', "D"):
                # Hit / doubling down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print(f"You drew a {rank} of {suit}")
                playerHand.append(newCard)

                if getHandValue > 21:
                    # The player has busted
                    continue

            if move in ("S", "D"):
                # Stand/doubling down stops the player's turn
                break
        # Handle the dealer's actions
        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                # The dealer hits
                print("Dealer hits..")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break  # The dealer has busted
                input("Press enter to continue...")
                print("\n\n")
        # Show the final hands
        displayHands(playerHand, dealerHand, True)

        playerValue = getHandValue(playerHand)
        dealerHand = getHandValue(dealerHand)
        # Handle whether the player won, lost, or tied.


def getBet(money: int):
    """Reteturn the bet"""
    pass


def getDeck():
    """Retrun a list that includes cards"""
    pass


def displayHands(playerHand: list, dealerHand: list, status: bool):
    pass


def getHandValue(hand: list):
    pass


def getMove(hand: list, money: int):
    """Return the action string lile H D S """
    pass


if __name__ == '__main__':
    main()
