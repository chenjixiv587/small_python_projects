import datetime
import random


def getBirthdays(numberOfBirthdays):
    """Returns a list of number random date objects for birthdays"""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays hava the same year.
        startOfYear = datetime.date(year=2023, month=1, day=1)

        # Get a random day into the year
        randomNumberOfDays = datetime.timedelta(days=random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    """Return the date object of a birthday that occurs more than once
    in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None  # All birthdays are unique, so return None
    # Compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA  # Return the match birthday.


# Disply the intro
print('The informatio of birthdayparadox')


# Set up a tuple of month names in order.
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:  # Keep asking until the user enter a valid amout.
    print('How many birthdays shall i generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break  # User has entered a valid amout.

print()


# Generate and display the birthdays
print(f'Here are {numBDays} birthdays: ')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(', ', end='')
    #  index = 0 presents Month Jan
    monthName = MONTHS[birthday.month - 1]
    dateText = f'{monthName} {birthday.day}'
    print(dateText, end='')
print()
print()


# Determine if there are two birthdays that match
match = getMatch(birthdays)

# Displat the results

print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = f'{monthName}{match.day}'
    print(f'Multiple people have a birthy on {dateText}')
else:
    print('There are no matching birthdays.')


print()

# Run through 100,000 simulations
print(f'Generating {numBDays} random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations')

simMatch = 0  # How many simulations had matching birthdays in them.
for i in range(0, 100_000):
    # Report on the progress every 10,000 simulations
    if i % 10_000 == 0:
        print(f'{i} simulations run..')

    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1
print('100,000 simulations run.')
# Display simulation results
probability = round(simMatch / 100_000 * 100, 2)
print(f'Out of 100,000 simulations of {numBDays} people there was a')
print(f'matching birthday in that group, {simMatch} times. This means')
print(f'that, people have a {probability}% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')
