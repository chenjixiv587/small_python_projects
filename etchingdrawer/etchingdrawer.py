import sys
import shutil

'''
9472 ─
9474 │
9484 ┌
9488 ┐
9492 └
9496 ┘
9500 ├
9508 ┤
9516 ┬
9524 ┴
9532 ┼
'''
UP_DOWN_CHAR = chr(9474)
LEFT_RIGHT_CHAR = chr(9472)
DOWN_RIGHT_CHAR = chr(9484)
DOWN_LEFT_CHAR = chr(9488)
UP_RIGHT_CHAR = chr(9492)
UP_LEFT_CHAR = chr(9496)
UP_DOWN_RIGHT_CHAR = chr(9500)
UP_DOWN_LEFT_CHAR = chr(9508)
DOWN_LEFT_RIGHT_CHAR = chr(9516)
UP_LEFT_RIGHT_CHAR = chr(9524)
CROSS_CHAR = chr(9532)

DIRECTION_UP_OR_DOWN = (set(["W", "S"]), set(["W"]), set(["S"]))
DIRECTION_LEFT_OR_RIGHT = (set(["A", "D"]), set(["A"]), set(["D"]))

# get the size of the terminal size

CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_HEIGHT -= 5
CANVAS_WIDTH -= 1

"""the keys for canvas will be (x, y) integer tuples for the coordinate 
and the value is a  set of  letters WASD that tell what kind of line 
should be drawn
"""

canvas = {}
cursorX = 0
cursorY = 0


def getCanvasString(canvasData, cx, cy):
    """return a multiline string of the line drawn in canvasData """
    canvasStr = ""

    """canvasData is a dictionary with (x, y) tuple keys and values that
      are sets of WASD strings to show which directions the lines are drawn at each xy point"""
    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_WIDTH):
            if columnNum == cx and rowNum == cy:
                canvasStr += "#"
                continue
            # add the line character for this point to canvasStr
            cell = canvasData.get((columnNum, rowNum))
            if cell in DIRECTION_UP_OR_DOWN:
                canvasStr += UP_DOWN_CHAR
            elif cell in DIRECTION_LEFT_OR_RIGHT:
                canvasStr += LEFT_RIGHT_CHAR
                # 同时按下
            elif cell == set(["S", "D"]):
                canvasStr += DOWN_RIGHT_CHAR
            elif cell == set(["A", "S"]):
                canvasStr += DOWN_LEFT_CHAR
            elif cell == set(["W", "D"]):
                canvasStr += UP_RIGHT_CHAR
            elif cell == set(["W", "A"]):
                canvasStr += UP_LEFT_CHAR
            elif cell == set(["W", "S", "D"]):
                canvasStr += UP_DOWN_RIGHT_CHAR
            elif cell == set(["W", "S", "A"]):
                canvasStr += UP_DOWN_LEFT_CHAR
            elif cell == set(["A", "S", "D"]):
                canvasStr += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(["W", "A", "D"]):
                canvasStr += UP_LEFT_RIGHT_CHAR
            elif cell == str(["W", "A", "S", "D"]):
                canvasStr += CROSS_CHAR
            elif cell == None:
                canvasStr += " "

        canvasStr += "\n"
    return canvasStr


moves = []
while True:
    # draw the lines based on the data in canvas
    print(getCanvasString(canvas, cursorX, cursorY))

    print("Press WASD to move, H for help, C to clear, F to save or QUIT to quit.")

    response = input("> ").upper()

    if response == "QUIT":
        print("Thanks for playing...")
        sys.exit()
    elif response == "H":
        print('Enter W, A, S, and D characters to move the cursor and')
        print('draw a line behind it as it moves. For example, ddd')
        print('draws a line going right and sssdddwwwaaa draws a box.')
        print()
        print('You can save your drawing to a text file by entering F.')
        input("Press Enter to return to the program..")
        continue
    elif response == "C":
        canvas = {}  # erase the canvas data
        moves.append("C")  # record the move
    elif response == "F":
        # save the canvas to a text file
        try:
            print("Enter filename to save to:")
            filename = input("> ")
            # make sure the filename ends with .txt
            if not filename.endswith(".txt"):
                filename += ".txt"
            with open(filename, "w", encoding="utf-8") as file:
                file.write("".join(moves) + "\n")
                file.write(getCanvasString(canvas, None, None))
        except:
            print('Error: Could not save the file')
    for command in response:
        if command not in ("W", "A", "S", "D"):
            continue  # ignore this letter and continue to next one
        moves.append(command)  # record this move

        # the first line we add needs to form a full line
        if canvas == {}:
            if command in ("W", "S"):
                # make the first line a horizontal one
                canvas[(cursorX, cursorY)] = set(["W", "S"])
            elif command in ("A", "D"):
                # make the first line a vertical one
                canvas[(cursorX, cursorY)] = set(["A", "D"])

        # update x  and  y
        if command == "W" and cursorY > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorY -= 1
        elif command == "S" and cursorY < CANVAS_HEIGHT - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorY += 1
        elif command == "A" and cursorX > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorX -= 1
        elif command == "D" and cursorX < CANVAS_WIDTH - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorX += 1
        else:
            # if the cursor dosen't move because it would have moved off
            # the edge of the canvas then don't change the set at canvas[(cursorX, cursorY)]
            continue

        # if there's no set for (cursorX, cursorY), add an empty set
        if (cursorX, cursorY) not in canvas:
            canvas[(cursorX, cursorY)] = set()

        # add the direction string to this xy point's set
        if command == "W":
            canvas[((cursorX, cursorY))].add("S")
        elif command == "S":
            canvas[(cursorX, cursorY)].add("W")
        elif command == "A":
            canvas[(cursorX, cursorY)].add("D")
        elif command == "D":
            canvas[(cursorX, cursorY)].add("A")
