import random

print("welcome to the game")


# get the player names
while True:
    print("please enter your name, player1")
    response1 = input("> ").strip()
    if response1 == "":
        continue
    else:
        player1 = response1
        break

while True:
    print("please enter your name, player2")
    response2 = input("> ").strip()
    if response2 == "":
        continue
    else:
        player2 = response2
        break

while True:
    print("please enter your name, player3")
    response3 = input("> ").strip()
    if response3 == "":
        continue
    else:
        player3 = response3
        break


redBox = "red"
goldBox = "gold"
blackBox = "black"

player1Score = 0
player2Score = 0
player3Score = 0


while True:
    print(
        f"there are three boxes, {player1} has {redBox} box, {player2} has {goldBox} box, {player3} has {blackBox} box")

    print(f"{player1} can now see the box,{player2} can not see..")

    if random.randint(1, 2) == 1:
        diamondInFirst = True
        print("redBox has diamond")
    else:
        diamondInFirst = False
        print("goldBox has diamond")

    print(f"{player1} can say have in box or not")

    print(f"{player2} do you want to swap? yes or no?")
    while True:
        response4 = input("> ").upper().strip()

        if response4.startswith("Y") or response4.startswith("N"):
            break
        else:
            print("Just YES or NO")
            continue

    if response4 == "Y":
        diamondInSecond = diamondInFirst
        diamondInFirst = not diamondInFirst
        redBox, goldBox = goldBox, redBox
        print(f"{player1} has {goldBox}, {player2} has {redBox}")
    else:
        diamondInSecond = not diamondInFirst
    print("player2 battles with player3")
    while True:
        print(f"{player3} do you want to swap? yes or no?")
        response5 = input("> ").upper().strip()
        if response5.startswith("Y") or response5.startswith("N"):
            break
        else:
            print("Just YES or NO")
            continue
    if response5 == "Y":
        goldBox, blackBox = blackBox, goldBox
        diamondInSecond = not diamondInSecond

    if diamondInFirst:
        print(f"winner is {player1}")
        player1Score += 1
    else:
        if diamondInSecond:
            print(f"winner is {player2}")
            player2Score += 1
        else:
            print(f"winner is {player3}")
            player3Score += 1

    print(
        f"player1 scores: {player1Score}, player2 scores: {player2Score}, player3 scores:{player3Score}")
    print("do you want to play again?")
    while True:
        choose = input().strip().upper()
        if choose == "Y" or choose == "N":
            break
        else:
            print("Just can enter N or Y")
            continue
    if choose == "Y":
        continue
    else:
        break
print("Thank for playing.")
