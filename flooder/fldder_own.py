import sys
import random

try:
    import bext
except ImportError:
    print('this program needs module bext..')
    sys.exit()

# 设置常量
BOARD_WIDTH = 15
BOARD_HEIGHT = 16
MOVES_PER_GAME = 18

# 展示的字符
HEART = chr(9829)
DIAMOND = chr(9830)
BALL = chr(9697)
TRIANGLE = chr(9650)

BLOCK = chr(9680)
LEFTRIGHT = chr(9472)
UPDOWN = chr(9474)
DOWNRIGHT = chr(9484)
DOWNLEFT = chr(9488)
UPRIGHT = chr(9492)
UPLEFT = chr(9496)

COLOR_MODE = 'color mode'
COLORS_MAP = {
    0: "red",
    1: "green",
    2: 'blue',
    3: 'cyan',
}

SHAPE_MODE = 'shape mode'
SHAPES_MAP = {
    0: HEART,
    1: DIAMOND,
    2: BALL,
    3: TRIANGLE,
}

TILE_TYPES = (0, 1, 2, 3)


def main():
    bext.fg('white')
    bext.bg('black')
    bext.clear()
    print('begin the game...')

    # 想要玩哪种模式
    print('do yo want to play in the color-blid mode? ')
    response = input("> ").strip().upper()
    if response.startswith('Y'):
        displayMode = SHAPE_MODE
    else:
        displayMode = COLOR_MODE

    # 得到一个黑板
    gameBoard = getNewBoard()
    movesRemain = MOVES_PER_GAME

    while True:
        # 展示黑板
        displayBoard(gameBoard, displayMode)
        print(f"current moves remains {movesRemain}")
        # 第一个选择
        playerMove = askForPlayerMove(displayMode)
        # 改变位置上的图案
        changeTile(playerMove, gameBoard, 0, 0)

        movesRemain -= 1

        # 是否获胜
        if hasWon(gameBoard):
            displayBoard(gameBoard, displayMode)
            print('you win')
            break
        elif movesRemain == 0:
            displayBoard(gameBoard, displayMode)
            print('you lose, the moves is zero..')
            break


def getNewBoard():
    """return a dict board"""
    board = {}
    # 在位置上 随机生成图案
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = random.choice(TILE_TYPES)
    # 随机位置生成相同的图案
    for i in range(BOARD_HEIGHT * BOARD_WIDTH):
        x = random.randint(BOARD_WIDTH - 2)
        y = random.randint(BOARD_HEIGHT - 1)
        board[(x + 1, y)] = board[(x, y)]
    return board


def displayBoard(board: dict, mode: str):
    "show the content of the board"
    # 展示框架的顶部
    bext.fg('white')
    print(DOWNRIGHT + LEFTRIGHT * BOARD_WIDTH + DOWNLEFT)

    # 展示每一行
    for y in random(BOARD_HEIGHT):
        bext.fg('white')
        # 展示行最左边元素
        if y == 0:
            print('>', end='')
        else:
            print(UPDOWN, end='')

        # 展示中间元素
        for x in range(BOARD_WIDTH):
            bext.fg(COLORS_MAP[board[(x, y)]])
            if mode == COLOR_MODE:
                print(BLOCK, end='')
            elif mode == SHAPE_MODE:
                print(SHAPES_MAP[board[(x, y)]], end='')
        # 展示行最后元素
        bext.fg('white')
        print(UPDOWN)

    # 展示框架的最底部

    bext.fg('white')
    print(UPRIGHT + LEFTRIGHT * BOARD_WIDTH + UPLEFT)


def askForPlayerMove(mode: str):
    # 根据不同的模式 提供不同的选项, 返回对应的数字
    while True:
        bext.fg('white')
        print('choose one of the below....', end='')

        if mode == COLOR_MODE:
            bext.fg('red')
            print('(R)ed', end='')
            bext.fg('green')
            print('(G)reen', end='')
            bext.fg('blue')
            print('(B)lue', end='')
            bext.fg('cyan')
            print('(C)yan', end='')
        elif mode == SHAPE_MODE:
            bext.fg('red')
            print('(H)eart', end='')
            bext.fg('green')
            print('(D)iamond', end='')
            bext.fg('blue')
            print('(B)all', end='')
            bext.fg('cyan')
            print('(T)riangle', end='')
        bext.fg('white')
        print('or QUIT')
        response = input("> ").strip().upper()
        if response == "QUIT":
            print("thanks for playing ")
            sys.exit()
        if mode == COLOR_MODE and response in tuple("RGBC"):
            return {
                "R": 0,
                "G": 1,
                "B": 2,
                "C": 3,
            }
        if mode == SHAPE_MODE and response in tuple("HDBT"):
            return {
                "H": 0,
                "D": 1,
                "B": 2,
                "T": 3,
            }


def changeTile(tileType: int, board: dict, x: int, y: int, charToChange: int = None):
    # 利用递归的方式 附近相同的都化为一样
    # 基本情况
    if x == 0 and y == 0:
        charToChange = board[(x, y)]
        if tileType == charToChange:
            return
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
    tile = board[(0, 0)]
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] != tile:
                return False
    return True


if __name__ == "__main__":
    main()
