"""
惊人的标题生成器
"""

import random

# Set up the constants:
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania',
          'Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent',
         'Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado',
         'Plastic Straw', 'Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement',
          'Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']


def main():
    print("make awesome")
    # get the valid number of headlines
    while True:
        print("please enter the number you want to generate the click headlines")
        response = input("> ").strip()
        if not response.isdecimal():
            print("Please enter a number")
            continue
        else:
            numberOfHeadlines = int(response)
            break
    for i in range(numberOfHeadlines):
        clickbaitType = random.randint(1, 4)
        if clickbaitType == 1:
            headline = generate1()
        elif clickbaitType == 2:
            headline = generate2()
        elif clickbaitType == 3:
            headline = generate3()
        elif clickbaitType == 4:
            headline = generate4()
        print(headline)
        print()

    print("\n")

    website = random.choice(
        ['wobsite', 'blag', 'Facebuuk', 'Googles', 'Facesbook', 'Tweedie', 'Pastagram'])

    when = random.choice(WHEN).lower()
    print(f"Post these to our {website}, {when} or your friend")


def generate1():
    noun = random.choice(NOUNS)
    return f"Are Millennials Killing the {noun} Industry?"


def generate2():
    noun = random.choice(NOUNS)
    pluralNoun = random.choice(NOUNS) + "s"
    when = random.choice(WHEN)
    return f'Without This {noun}, {pluralNoun} Could Kill You {when}'


def generate3():
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f"Big Companies Hate {pronoun}! See How This {state} {noun1} Invented a Cheaper {noun2}"


def generate4():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    pronoun = random.choice(POSSESIVE_PRONOUNS)
    place = random.choice(PLACES)
    return f"You Won\'t Believe What This {state} {noun} Found in {pronoun} {place}"


if __name__ == "__main__":
    main()
