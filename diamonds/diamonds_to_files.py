
def main():
    print("Diamonds,.......")

    # display diamonds of sizes 1 through 6

    for diamondSize in range(1, 6):
        outlineDiamond = makeOutlineDiamond(diamondSize)
        filledDiamond = makeFilledDiamond(diamondSize)
        diamond = outlineDiamond + "\n" + filledDiamond
        with open(f"diamonds_{diamondSize}.txt", "w") as f:
            f.write(diamond)

# pay attention drawing line and line


def makeOutlineDiamond(size):
    # display the top half of the diamond
    # space / space \
    outlineTopHalf = ""
    for i in range(size):
        outlineTopHalf += " " * (size - i - 1) + "/" + \
            " " * (i * 2) + "\\" + "\n"

    # display the bottom half of the diamond
    outlineBottomHalf = ""
    for j in range(size):
        outlineBottomHalf += " " * j + "\\" + \
            " " * (size - j - 1) * 2 + "/" + "\n"

    return outlineTopHalf + outlineBottomHalf

# display filled Diamonds


def makeFilledDiamond(size):
    # display the top half of the diamond
    filledTopHalf = ""
    for i in range(size):
        filledTopHalf += " " * (size - i - 1) + "/" * \
            (i + 1) + "\\" * (i + 1) + "\n"
    # display the bottom half of the diamond
    filledBottomHalf = ""
    for j in range(size):
        filledBottomHalf += " " * j + "\\" * \
            (size - j) + "/" * (size - j) + "\n"
    return filledTopHalf + filledBottomHalf


if __name__ == "__main__":
    main()
