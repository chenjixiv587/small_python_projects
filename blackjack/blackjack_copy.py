"""
Blackjack game always we also call 21 ponits game.

"""
import sys
import random


# Set up the constants:
# suit
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
            print("The only fortunate thing is that you weren't play the true \
                  game")
            print("Thanks for playing")
            sys.exit()
        # Let the user enter his bet in this round
        print(f'Money: {money}')

        # give the bet.
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

                if getHandValue(playerHand) > 21:
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
        dealerValue = getHandValue(dealerHand)
        # Handle whether the player won, lost, or tied.
        if dealerValue > 21:
            print(f"Dealer Busts! You win {bet}")
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("You are lost!")
            money -= bet
        elif playerValue > dealerValue:
            print(f"You won {bet}")
            money += bet
        elif playerValue == dealerValue:
            print("It's a tie, the bet is returned to you.")

        input("Press enter to continue")
        print("\n\n")


def getBet(maxBet: int):
    """Reteturn the bet
    Ask the player how much they want to bet for this round.
    """
    while True:  # Keep asking until they enter a valid data
        print(f"How much do you bet, (1- {maxBet} or QUIT)")
        bet = input("> ").upper().strip()
        if bet == "QUIT":
            print("Thanks for playing")
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet  # Player entered a valid bet.


def getDeck():
    """Retrun a list of (rank, suit) tuples for all 52 cards"""
    deck = []
    # suit 表示花色 rank 表示点数
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  # Add the numbered cards
        for rank in ("J", "Q", "K", "A"):
            deck.append((rank, suit))  # Add the face and ace cards

    random.shuffle(deck)
    return deck


def displayHands(playerHand: list, dealerHand: list, showDealerHand: bool):
    """Show the play's and dealer's cards, Hide the dealer's first card if showDealerHand is Fasle"""
    print()
    if showDealerHand:
        print("DEALER: ", getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print("DEALER: ???")
        # Hide the dealer's first card.
        displayCards([BACKSIDE] + dealerHand[1:])

    # Show the player's cards
    print("PLAYER: ", getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards: list):
    """Retrun the value of the cards. Face cards are worth 10, 
    aces are worth 11 or 1, (This dfunction picks the most suitable ace value)"""
    value = 0
    numberOfAces = 0

    # Add the value for the non-ace cards
    for card in cards:
        rank = card[0]  # card is a tuple like (rank, suit)
        if rank == "A":
            numberOfAces += 1
        elif rank in ("J", "Q", "K"):  # Face cards are worth 10 points.
            value += 10
        else:
            value += int(rank)  # Numbered cards are worth their number.

    # Add the value for the aces
    value += numberOfAces  # Add one per ace
    for i in range(0, numberOfAces):
        # If another 10 can be added without busting, do so
        tempValue = value + 10
        if tempValue <= 21:
            value += 10
    return value


def displayCards(cards: list):
    """Display all cards in the cards list"""
    # rows = ['', '', '', '', '']
    rows = ['']*5  # The text to display on each row

    for i, card in enumerate(cards):
        rows[0] += ' ____ '  # Print the top line of the card
        if card == BACKSIDE:
            # Print a card's back.
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Print the card's front
            rank, suit = card  # The card is a tuple data structure
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, "_"))
            # >>> chr(9827).ljust(2)
            # '♣ '
            # >>> chr(9827).rjust(2, "_")
            # '_♣'
            # Print each row on the screen.
    for row in rows:
        print(row)


def getMove(playerHand: list, money: int):
    """Ask the player for their move, and returns 'H' for hit,
    'S' for stand, and 'D' for double down."""

    while True:  # Keep looping until the player enters a correct move.
        # Determine what moves the player can make
        moves = ["(H)it", "(S)tand"]

        # The player can double down on their first move, which we can
        # tell because they'll have exactly two cards
        if len(playerHand) == 2 and money > 0:
            moves.append("(D)ouble down")

        # Get the player's move
        movePrompt = ", ".join(moves) + "> "
        move = input(movePrompt).upper()
        if move in ("H", "S"):
            return move  # Player has entered a valid move.
        if move == "D" and ("(D)ouble down" in moves):
            return move  # Player has entered a valid move.


# If the program is run(instead of imported), run the game:
if __name__ == '__main__':
    main()
