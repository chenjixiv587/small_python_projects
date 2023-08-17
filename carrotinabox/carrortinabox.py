"""
the two boxes game. one box has a carrot, player1 can see in the box and 
say have a carrot in it or not 
player2 can choose swap the box or not.
"""

import random

input("Press Enter to begin the game...")
while True:
    playerA = input("Human pA, enter your name: ").strip()
    if playerA == "":
        continue
    else:
        break
while True:
    playerB = input("Human pB, enter your name: ").strip()
    if playerB == "":
        continue
    else:
        break

playerNames = playerA[:11].center(11) + "       " + playerB[:11].center(11)

print('''HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/''')

print()
print(playerNames)
print()
print(f"{playerA}, you have a red box in front of you")
print(f"{playerB}, you have a gold box in front of you.")
print()
print(f"{playerA}, you will get to look in the box")
print(f"{playerB.upper()}, you can't see in the box, you need keep your eyes closed.")
input(f"When {playerB} closed the eyes, press enter to continue")
print()

print(f"{playerA} here is the content in your box")

if random.randint(1, 2) == 1:
    carrotInFirstBox = True
else:
    carrotInFirstBox = False

if carrotInFirstBox:
    print('''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|    __________
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
 (carrot!)''')
    print(playerNames)
else:
    print('''
   _________
  |         |
  |         |
  |_________|    __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
(no carrot!)''')
    print(playerNames)

input("Press enter to continue....")
print("\n" * 100)  # clear the screen
print(f"{playerA} tell {playerB} to open their eyes")
input("Press enter to continue....")

print()
print(f"{playerA} says one of the sentences to {playerB}")
print('  1) There is a carrot in my box.')
print('  2) There is not a carrot in my box.')
print()
input('Then press Enter to continue...')


print()
print(f"{playerB} do you want to swap the {playerA} box yes or no?")
while True:  # keep looping until playerB give the valid response
    response = input("> ").upper().strip()
    if not (response.startswith("Y") or (response.startswith("N"))):
        print("just enter yes or no")
        continue
    else:
        break

firstBox = "RED "  # note the space after D
secondBox = "GOLD"

if response.startswith("Y"):
    firstBox, secondBox = secondBox, firstBox
    carrotInFirstBox = not carrotInFirstBox

print('''HERE ARE THE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))
print(playerNames)

input("press enter revel the winner")
print()


if carrotInFirstBox:
    print('''
   ___VV____      _________
  |   VV    |    |         |
  |   VV    |    |         |
  |___||____|    |_________|
 /    ||   /|   /         /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))

else:
    print('''
   _________      ___VV____
  |         |    |   VV    |
  |         |    |   VV    |
  |_________|    |___||____|
 /         /|   /    ||   /|
+---------+ |  +---------+ |
|   {}  | |  |   {}  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/'''.format(firstBox, secondBox))

print(playerNames)


if carrotInFirstBox:
    print(f"winner is {playerA}")
else:
    print(f"winner is {playerB}")
