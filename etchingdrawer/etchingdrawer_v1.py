import sys
import shutil

"""
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
"""

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


# get the size of the terminal size
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH -= 1
CANVAS_HEIGHT -= 5


canvas = {}
cursorX = 0
cursorY = 0


def getCanvasString(canvasData, cx, cy):
    """return a multiline string of the line drawn in
    canvasData
    canvasData 是一个字典 他的键是(x,y)坐标 值是WASD组合成的集合
    """
    canvasString = ""
    for rowNum in range(CANVAS_HEIGHT):
        for columnNum in range(CANVAS_WIDTH):
            # 光标所在位置用 # 表示
            if columnNum == cx and rowNum == cy:
                canvasString += "#"
                continue

            cell = canvasData.get((columnNum, rowNum))
            if cell in (set(["W", "S"]), set(["W"]), set(["S"])):
                canvasString += UP_DOWN_CHAR
            elif cell in (set(["A", "D"]), set(["A"]), set(["D"])):
                canvasString += LEFT_RIGHT_CHAR
            elif cell == set(["S", "D"]):
                canvasString += DOWN_RIGHT_CHAR
            elif cell == set(["A", "S"]):
                canvasString += DOWN_LEFT_CHAR
            elif cell == set(["W", "D"]):
                canvasString += UP_RIGHT_CHAR
            elif cell == set(["W", "A"]):
                canvasString += UP_LEFT_CHAR
            elif cell == set(["W", "S", "D"]):
                canvasString += UP_DOWN_RIGHT_CHAR
            elif cell == set(["W", "S", "A"]):
                canvasString += UP_DOWN_LEFT_CHAR
            elif cell == set(["A", "S", "D"]):
                canvasString += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(["W", "A", "D"]):
                canvasString += UP_LEFT_RIGHT_CHAR
            elif cell == set(["W", "A", "S", "D"]):
                canvasString += CROSS_CHAR
            elif cell is None:
                canvasString += ""
        canvasString += "\n"
    return canvasString


moves = []
while True:
    # draw the line based on the data in canvas
    print(getCanvasString(canvas, cursorX, cursorY))
    print("press W A S D to move, H for help, C to clear, f to save to a file, Q or quit")

    response = input("> ").strip().upper()
    if response == "Q":
        print("GAME OVER")
        sys.exit()
    elif response == "H":
        print("Help.....")
    elif response == "C":
        canvas = {}
        moves.append("C")
    elif response == "F":
        # save the canvas to a text file
        try:
            print("Enter the filename to save to :...")
            filename = input("> ")
            if not filename.endswith(".txt"):
                filename += ".txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(" ".join(moves) + "\n")
                f.write(getCanvasString(canvas, None, None))

        except:
            print("Error: Could not save the file")
    for command in response:
        if command not in ("W", "A", "S", "D"):
            continue
        moves.append(command)

        if canvas == {}:
            if command in ("W", "S"):
                canvas[(cursorX, cursorY)] = set(["W", "S"])
            elif command in ("A", "D"):
                canvas[(cursorX, cursorY)] = set(["A", "D"])

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
            continue

        if (cursorX, cursorY) not in canvas:
            canvas[(cursorX, cursorY)] = set()

        if command == "W":
            canvas[(cursorX, cursorY)].add("S")
        elif command == "S":
            canvas[(cursorX, cursorY)].add("W")
        elif command == "A":
            canvas[(cursorX, cursorY)].add("D")
        elif command == "D":
            canvas[(cursorX, cursorY)].add("A")
