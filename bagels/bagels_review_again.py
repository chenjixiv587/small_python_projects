"""
Play the game that guess the NUM_DIGITS string numbers
We should know the NUM_DIGITS MAX_GUESS 
And user will get the relative information

the process
1 start the main loop of the game
2 get the secretNum by using getSecretNum function
3 start the loop of judge the guessNnum and MAX_NUM
4 judge the user input data
5 show the clues
6 print the game info
7 ask user countinue or not
8 thank the user to play the game


"""
import random
NUM_DIGITS = 3
MAX_GUESS = 10
BASE_NUM = '0123456789'


def main():
    while True:  # The main loop of the game
        print('Welcome to the guess game.')
        secretNum = getSecretNum(NUM_DIGITS)
        guessNum = 1  # set the start guess num as 1
        while guessNum <= MAX_GUESS:
            guess = ''
            # keep loop until the guess is valid
            while len(guess) != NUM_DIGITS or guess.isdecimal() is None:
                print(f'Guess #{guessNum}')
                guess = input('> ')
            guessNum += 1

            # show the hint
            clues = getClues(guess, secretNum)
            print(clues)
            if guess == secretNum:
                break
            if guessNum > MAX_GUESS:
                print(f'You have tried {MAX_GUESS} times')
                print(f'The secret num is {secretNum}')
        print('Do you want to play again? (yes or no)')
        if not input().lower().startswith('y'):
            break
    print('Thank you for your playing.')


def getSecretNum(digitsOfNum: int):
    """Return the number string"""
    number = list(BASE_NUM)
    secretNum = ''
    # get the digitsOfNum random numbers
    for i in range(digitsOfNum):
        secretNum += number[random.randint(0, len(number) - 1)]
    return secretNum


def getClues(guess: str, secretNum: str):
    """Rerturn the string of the hint"""
    if guess == secretNum:
        return 'You win'
    clues = []
    for i in range(0, len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')
        elif guess[i] in secretNum:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        # ensure the sort of the clues not the origin position.
        clues.sort()
        return ''.join(clues)


if __name__ == '__main__':
    main()
