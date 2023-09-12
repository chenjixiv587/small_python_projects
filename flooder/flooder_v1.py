import sys
import random

try:
    import bext
except ImportError:
    print("This program need bext module...")
    sys.exit()


# set up the constants
BOARD_WIDTH = 16
BOARD_HEIGHT = 14
MOVES_PER_GAME = 20


# constants for the different shapes in colorblind mode
HEART = chr(9829)
DIAMOND = chr(9830)
SPADE = chr(9824)
CLUB = chr(9827)
BALL = chr(9697)
TRIANGLE = chr(9650)

BLOCK = chr(9680)
LEFTRIGHT = chr(9472)
UPDOWN = chr(9474)
DOWNRIGHT = chr(9484)
DOWNLEFT = chr(9488)
UPRIGHT = chr(9492)
UPLEFT = chr(9496)


# all the color/shape tiles used on the board
TILE_TYPE = (0, 1, 2, 3, 4, 5)

COLOR_MODE = 'color mode'
COLORS_MAP = {
    0: 'red',
    1: 'green',
    2: 'blue',
    3: 'yellow',
    4: 'cyan',
    5: 'purple',
}

SHAPE_MODE = 'shape mode'
SHAPES_MAP = {
    0: HEART,
    1: TRIANGLE,
    2: DIAMOND,
    3: BALL,
    4: CLUB,
    5: SPADE,
}


def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print("here we go...")

    print("Do you want to play in the color-blind mode?")
    response = input("> ").strip().upper()
    if response.startswith('Y'):
        displayMode = SHAPE_MODE
    else:
        displayMode = COLOR_MODE
    # 定义一个游戏黑板
    gameBoard = getNewBoard()
    movesRemains = MOVES_PER_GAME

    while True:
        # 展示黑板
        displayBoard(gameBoard, displayMode)
        print(f'moves remains:  {movesRemains}')

        playerMove = askForPlayerMove(displayMode)
        changeTile(playerMove, gameBoard, 0, 0)

        movesRemains -= 1

        if hasWon(gameBoard):
            displayBoard(gameBoard, displayMode)
            print("you won")
            break
        elif movesRemains == 0:
            displayBoard(gameBoard, displayMode)
            print('you have run out of moves')
            break


def getNewBoard():
    """return a dictionary of a new flood it board"""
    # keys are (x, y) tuples, values are the tile at that position
    board = {}

    # create the random colors for the board
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = random.choice(TILE_TYPE)

    # make serveral tiles the same as their neighbors
    for i in range(BOARD_HEIGHT * BOARD_WIDTH):
        x = random.randint(0, BOARD_WIDTH - 2)
        y = random.randint(0, BOARD_HEIGHT - 1)
        board[(x + 1, y)] = board[(x, y)]

    return board


def displayBoard(board: dict, mode: str):
    """display the board on the screen"""

    # 展示顶部
    bext.fg('white')
    print(DOWNRIGHT + LEFTRIGHT * BOARD_WIDTH + DOWNLEFT)

    # 展示每一行
    for y in range(BOARD_HEIGHT):
        # 展示行最左边
        bext.fg('white')
        if y == 0:
            print(">", end="")
        else:
            print(UPDOWN, end='')
        # 展示中间部分
        for x in range(BOARD_WIDTH):
            bext.fg(COLORS_MAP[board[(x, y)]])
            if mode == COLOR_MODE:
                print(BLOCK, end="")
            elif mode == SHAPE_MODE:
                print(SHAPES_MAP[board[(x, y)]], end="")
        # 展示行尾部
        bext.fg('white')
        print(UPDOWN)

    bext.fg('white')
    print(UPRIGHT + LEFTRIGHT * BOARD_WIDTH + UPLEFT)


def askForPlayerMove(mode: str):
    """let the player select a color to paint the upper left title"""
    # 问玩家 第一个选择什么 返回的是一个数字 数字对应的是类型里面具体的值
    while True:
        bext.fg('white')
        print('choose one of below', end='')

        if mode == COLOR_MODE:
            bext.fg('red')
            print('(R)ed', end="")
            bext.fg('green')
            print('(G)reen', end="")
            bext.fg('blue')
            print('(B)lue', end="")
            bext.fg('yellow')
            print('(Y)ellow', end="")
            bext.fg('cyan')
            print('(C)yan', end="")
            bext.fg('purple')
            print('(P)urple', end="")
        elif mode == SHAPE_MODE:
            bext.fg('red')
            print('(H)eart', end="")
            bext.fg('green')
            print('(T)riangle', end="")
            bext.fg('blue')
            print('(D)iamond', end="")
            bext.fg('yellow')
            print('(B)all', end="")
            bext.fg('cyan')
            print('(C)lub', end="")
            bext.fg('purple')
            print('(S)pade', end="")

        bext.fg("white")
        print('or QUIT: ')
        response = input("> ").strip().upper()
        if response == "QUIT":
            print("bye")
            sys.exit()
        if mode == COLOR_MODE and response in tuple("RGBYCP"):
            return {
                "R": 0,
                "G": 1,
                "B": 2,
                "Y": 3,
                "C": 4,
                "P": 5,
            }[response]
        if mode == SHAPE_MODE and response in tuple("HTDBCS"):
            return {
                "H": 0,
                "T": 1,
                "D": 2,
                "B": 3,
                "C": 4,
                "S": 5,
            }[response]


def changeTile(tileType: int, board: dict, x: int, y: int, charToChange: int = None):
    """Change the color/shape of a tile using the recursive flood fill algorihm"""
    if x == 0 and y == 0:
        charToChange = board[(x, y)]
        if tileType == charToChange:
            return  # base case already is the same tile
    board[(x, y)] = tileType

    if x > 0 and board[(x - 1, y)] == charToChange:
        changeTile(tileType, board, x - 1, y, charToChange)
    if y > 0 and board[(x, y - 1)] == charToChange:
        changeTile(tileType, board, x, y - 1, charToChange)
    if x < BOARD_WIDTH - 1 and board[(x + 1, y)] == charToChange:
        changeTile(tileType, board, x + 1, y, charToChange)
    if y < BOARD_HEIGHT - 1 and board[(x, y + 1)] == charToChange:
        changeTile(tileType, board, x, y + 1, charToChange)


def hasWon(board: dict):
    "return true if the entire board is one color or shape"
    tile = board[(0, 0)]

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] != tile:
                return False
    return True


if __name__ == "__main__":
    main()
