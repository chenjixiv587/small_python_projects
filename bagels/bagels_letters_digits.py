import random

# the digits of the number and the letters
NUM_DIGITS = 3
# the max guesses time
MAX_GUESSES = 10


def main():
    while True:   # The main game loop
        print('Welcome to my game!')
        # get the secret number
        secretNum = getSecretNum()
        guessNum = 1
        while guessNum <= MAX_GUESSES:
            # Keep loop until input is a valid number
            guess = ''
            while len(guess) != NUM_DIGITS:
                # The next guess times
                print(f'Guess #{guessNum}')
                guess = input('> ').lower()
            guessNum += 1
            # print the clues
            clues = getClues(guess, secretNum)
            print(clues)
            # guess right, quit the game.
            if guess == secretNum:
                break
            if guessNum > MAX_GUESSES:
                print(f'You have try more than {MAX_GUESSES} times')
                print(f'The secretNum is {secretNum}')
        # Ask player play again
        print('Do you want to play again?(yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing the game!')


def getSecretNum():
    """Return the secret number"""
    numbers = list('0123456789abcdefghijklmnopqrstuvwxyz')
    random.shuffle(numbers)
    secretNum = ''
    for i in range(0, NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum


def getClues(guess: str, secretNum: str):
    """Return the strig presents clues"""
    if guess == secretNum:
        return 'You got it! Goog luck'
    # keep the result in clues
    clues = []
    for i in range(0, len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()  # sort the clues by alphabet not the origin position
        return ''.join(clues)


if __name__ == '__main__':
    main()
