"""
get soem people's birthdays and calculate the percentage of the birthday is the same
1 ensure the amount of the birthdays
2 get a list of birthdays
3 get the match birthday
4 show the birthdays width the month and day
5 run 10,000 times to calculate the percentage.
"""
import datetime
import random
BASEDAY = datetime.date(year=2023, month=1, day=1)
MONTHS = ('Jan', 'Feb', 'Mar', "Apr", "May",
          'Jun', 'Jul', "Aug", 'Sep', 'Oct', 'Nov', 'Dec')


def main():
    while True:  # Keep loop until the data is valid
        print('How many birthdays do you want to generate, max is 100')
        response = input('> ')
        if response.isdecimal() and (0 < int(response) <= 100):
            numBDdays = int(response)
            break

    birthdays = getBirthdays(numBDdays)
    # Show the birthdays of month day format
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(', ', end='')
        monthOfBirthday = MONTHS[birthday.month - 1]
        dayOfBirthday = birthday.day
        print(f'{monthOfBirthday} {dayOfBirthday}', end='')

    print()
    print()

    match = getMatch(birthdays)
    if match is not None:
        matchMonth = MONTHS[match.month - 1]
        matchDay = match.day
        print(f'The match birthday is {matchMonth} {matchDay}')

    # Begin the simulation
    print('Let\'s begin the 10,000 simulation')
    input('Enter to start...')
    simMatch = 0
    for i in range(0, 100_000):
        if i % 10000 == 0:
            print(f'{i} simulatuon start!')
        if match is not None:
            simMatch += 1
    print('100,000 is over')

    probability = round(simMatch * 100 / 100_000, 2)
    print(
        f'When {numBDdays} people in a group,the percentage of have the same birthday is {probability}')


def getBirthdays(amountOfbirthdays: int):
    """Return the birthdays list"""
    birthdays = []
    for i in range(amountOfbirthdays):
        birthday = BASEDAY + datetime.timedelta(days=random.randint(0, 364))
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays: list):
    """Return the same birthday"""
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA


if __name__ == '__main__':
    main()
