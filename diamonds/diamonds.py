def main():
    print("Diamonds,.......")

    # display diamonds of sizes 1 through 6
    for diamondSize in range(1, 20):
        print(f"The size is: {diamondSize}")
        displayOutlineDiamond(diamondSize)
        print()  # print a newline
        displayFilledDiamond(diamondSize)
        print()

# pay attention drawing line and line


def displayOutlineDiamond(size):
    # display the top half of the diamond
    # space / space \
    for i in range(size):
        # print the left leading space
        print(" " * (size - i - 1), end="")
        # print the left /
        print("/", end="")
        # print inner space
        print(" " * (i * 2), end="")
        # print the \
        print("\\")

    # display the bottom half of the diamond
    for j in range(size):
        # print the leading spaces
        print(" " * j, end="")
        # print the \
        print("\\", end="")
        # print the inner space
        print(" " * (size - j - 1) * 2, end="")
        # print the /
        print("/")

# display filled Diamonds


def displayFilledDiamond(size):
    # display the top half of the diamond
    for i in range(size):
        print(" " * (size - i - 1), end="")  # left side space
        print("/" * (i + 1), end="")  # left half of diamond
        print("\\" * (i + 1))  # right side of diamond

    # display the bottom half of the diamond
    for j in range(size):
        print(" " * j, end="")  # left side space
        print("\\" * (size - j), end="")  # left side of diamond
        print("/" * (size - j))  # right side of diamond


if __name__ == "__main__":
    main()
