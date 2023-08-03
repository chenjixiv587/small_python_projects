"""
逻辑推算游戏 猜三位数

如果提示是 Pico 那么就是 你猜的有一个数字是对的 但是位置不对
如果提示是 Fermi 那么就是 你猜的有一个数字是对的  而且位置也是对的
如果提示是 Bagels 那么你猜的都不对
你总共有十次机会
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print("""The game rules""")
    # Main game loop
    while True:
        # This stores the secret number the player needs to guess
        secretNum = getSecretNum()
        print('I have thought up a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')
        
        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Keep looping until they enter a valid guess.
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{numGuesses}')
                guess = input('> ')
            # the clues tell player
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # they are correct, so break out of this loop.
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print(f'The answer is {secretNum}')
        # Ask player if they want to play again
        print('Do you want to play again? (yes or no?)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing.')


def getSecretNum():
    """Return a string made up of NUM_DIGITS unique random digits"""
    numbers = list('0123456789')  # Create a list of digits 0 to 9
    random.shuffle(numbers) # Shuffle them into random order

    # Get the first NUM_DIGITS digits in the list for the secret number
    secretNum = ''
    for i in range(0, NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess:str, secretNum:str):
    """Return a strig with the pico fermi bagels clues for a guess
    and secret number pair"""
    if guess == secretNum:
        return 'You got it.'
    clues = []
    for i in range(0, len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit in the correct place.
            clues.append('Fermi')
        elif guess[i] in secretNum:
            # A correct digit is in the incorrect place
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits all
    else:
        # Sort the clues into alphabetical order so their origin order
        # dosen't give information away.
        clues.sort()
        # Make a single string from the list of string clues.
        return ''.join(clues)


# If the program is run (instead of imported), run the game.
if __name__ == "__main__":
    main()
