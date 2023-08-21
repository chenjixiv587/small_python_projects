"""
drawing diamonds

"""


def main():
    for diamondSize in range(1, 6):
        print(f"The size is {diamondSize}")
        showOutlineDiamonds(diamondSize)
        print()
        showFilledDiamonds(diamondSize)
        print()

#  the diamond includes each line  (space  / space \)


def showOutlineDiamonds(size):
    # show the top half of the diamonds
    for i in range(size):
        print(" " * (size - i - 1), end="")  # show the left spaces
        print("/", end="")  # show the left /
        print(" " * (i * 2), end="")  # show the inner spaces
        print("\\")  # show the right \

    # show the bottom half of the diamonds
    for j in range(size):
        print(" " * j, end="")
        print("\\", end="")
        print(" " * 2 * (size - j - 1), end="")
        print("/")


def showFilledDiamonds(size):
    for i in range(size):
        print(" " * (size - 1 - i), end="")
        print("/" * (i + 1), end="")
        print("\\" * (i + 1))

    for j in range(size):
        print(" " * j, end="")
        print("\\" * (size - j), end="")
        print("/" * (size - j))


if __name__ == "__main__":
    main()
