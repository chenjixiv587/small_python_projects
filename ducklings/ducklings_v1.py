import shutil
import sys
import time
import random
# set up the constants

PAUSE = 0.2
DENSITY = 0.1

DUCKLING_WIDTH = 5
LEFT = "left"
RIGHT = "right"
BEADY = "beady"
WIDE = "wide"
HAPPY = "happy"
ALOOF = "aloof"
CHUBBY = "chubby"
VERY_CHUBBY = "very_chubby"
OPEN = "open"
CLOSED = "closed"
OUT = "out"
DOWN = "down"
UP = "up"
HEAD = "head"
BODY = "body"
FEET = "feet"

# get the size of the terminal
WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1


def main():
    print("there are so many ducklings coming....")
    print("press CTRL-C to quit...")
    time.sleep(2)

    # the amount of the ducklings
    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:  # the main loop
        # 也是一行一行输出
        for laneNum, ducklingObj in enumerate(ducklingLanes):
            # 生成
            if ducklingObj is None and random.random() < DENSITY:
                ducklingObj = Duckling()
                ducklingLanes[laneNum] = ducklingObj

            # 展示
            if ducklingObj is not None:
                # draw a duckling if there is one in this lane
                print(ducklingObj.getNextBodyPart(), end="")
                # delete the duckling if we have finished drawing it
                if ducklingObj.partToDisplayNext is None:
                    ducklingLanes[laneNum] = None
            else:
                # draw five spaces since there is no duckling here
                print(" " * DUCKLING_WIDTH, end="")
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)


class Duckling:
    def __init__(self) -> None:
        """create a new duckling with random body feature"""
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])

        if self.body == CHUBBY:
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])

        # 即将展示的部分
        self.partToDisplayNext = HEAD

    def getHeadStr(self):
        """return the string of the duckling's head"""
        headStr = ""

        if self.direction == LEFT:
            if self.mouth == OPEN:
                headStr += ">"
            else:
                headStr += "="

            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += "''"
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += "'' "
            elif self.eyes == WIDE:
                headStr += "' '"
            elif self.eyes == HAPPY:
                headStr += "^^"
            elif self.eyes == ALOOF:
                headStr += "``"

            headStr += ")"

        if self.direction == RIGHT:
            headStr += "("
            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += "''"
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += " ''"
            elif self.eyes == WIDE:
                headStr += "' '"
            elif self.eyes == HAPPY:
                headStr += "^^"
            elif self.eyes == ALOOF:
                headStr += "``"

            if self.mouth == OPEN:
                headStr += "<"
            else:
                headStr += "="

            if self.body == CHUBBY:
                headStr += " "

        return headStr

    def getBodyStr(self):
        bodyStr = "("
        if self.direction == LEFT:
            if self.body == CHUBBY:
                bodyStr += " "
            elif self.body == VERY_CHUBBY:
                bodyStr += "  "

            if self.wing == OUT:
                bodyStr += ">"
            elif self.wing == UP:
                bodyStr += "^"
            elif self.wing == DOWN:
                bodyStr += "v"

        if self.direction == RIGHT:
            if self.wing == OUT:
                bodyStr += "<"
            elif self.wing == UP:
                bodyStr += "^"
            elif self.wing == DOWN:
                bodyStr += "v"
        bodyStr += ")"
        if self.body == CHUBBY:
            bodyStr += " "
        return bodyStr

    def getFeetStr(self):
        feetStr = ""
        if self.body == CHUBBY:
            feetStr += "^^"
        elif self.body == VERY_CHUBBY:
            feetStr += " ^ ^ "
        return feetStr

    def getNextBodyPart(self):
        if self.partToDisplayNext == HEAD:
            self.partToDisplayNext = BODY
            return self.getHeadStr()
        elif self.partToDisplayNext == BODY:
            self.partToDisplayNext = FEET
            return self.getBodyStr()
        elif self.partToDisplayNext == FEET:
            self.partToDisplayNext = None
            return self.getFeetStr()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
