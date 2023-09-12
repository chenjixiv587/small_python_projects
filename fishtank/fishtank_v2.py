import random
import sys
import time
try:
    import bext
except ImportError:
    sys.exit()


# 设置常量

WIDTH, HEIGHT = bext.size()
WIDTH -= 1

NUM_FISHES = 10
NUM_KELPS = 10
NUM_BUBBLE_MACHINES = 10

FRAMES_PER_SECOND = 4

FISH_TYPES = [
    {'right': ['><>'], 'left': ['<><']},
    {'right': ['>||>'], 'left': ['<||<']},
    {'right': ['>))>'], 'left': ['<[[<']},
    {'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
    {'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
    {'right': ['>-==>'], 'left': ['<==-<']},
    {'right': [r'>\\>'], 'left': ['<//<']},
    {'right': ['><)))*>'], 'left': ['<*(((><']},
    {'right': ['}-[[[*>'], 'left': ['<*]]]-{']},
    {'right': [']-<)))b>'], 'left': ['<d(((>-[']},
    {'right': ['><XXX*>'], 'left': ['<*XXX><']},
    {'right': ['_.-._.-^=>', '.-._.-.^=>',
               '-._.-._^=>', '._.-._.^=>'],
        'left': ['<=^-._.-._', '<=^.-._.-.',
                 '<=^_.-._.-', '<=^._.-._.']},
]

LONGEST_FISH_LENGTH = 10

# the x, y position in the edge of the tank
LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH

TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2


def main():
    global FISHES
    global BUBBLE_MACHINES
    global BUBBLES
    global KELPS
    global STEP

    bext.fg("black")
    bext.clear()

    # generate the global variables
    FISHES = []
    for i in range(NUM_FISHES):
        FISHES.append(generateFish())

    # 生成制造泡泡的机器
    BUBBLE_MACHINES = []
    for i in range(NUM_BUBBLE_MACHINES):
        # 泡泡即的横坐标
        BUBBLE_MACHINES.append(random.randint(LEFT_EDGE, RIGHT_EDGE))

    BUBBLES = []  # 里面存放的是字典 对应位置坐标

    KELPS = []
    for i in range(NUM_KELPS):
        # 水草的横坐标
        kelpX = random.randint(LEFT_EDGE, RIGHT_EDGE)
        # 水藻是个字典类型 横坐标和内容
        kelp = {'x': kelpX, 'segments': []}
        # generate the each segment of the kelp.
        for j in range(random.randint(6, HEIGHT - 1)):
            kelp['segments'].append(random.choice(["^", "v"]))
            KELPS.append(kelp)

    # 开始模拟
    STEP = 1
    # 执行模拟
    simulationAquarium()
    # 绘制鱼缸
    drawAquarium()
    time.sleep(1 / FRAMES_PER_SECOND)
    # 清理鱼缸
    clearAquarium()
    STEP += 1


# 得到随机的颜色
def getRandomColor():
    """return the random color"""
    return random.choice(["black", "red", "green", "yellow"])


def generateFish():
    """return the dic fish"""
    fishType = random.choice(FISH_TYPES)  # 得到的是一个字典
    fishLength = len(fishType['right'][0])
    # 设置鱼的颜色
    colors = []
    colorPattern = random.choice(["random", "head-tail", "single"])

    if colorPattern == "random":
        for i in range(fishLength):
            colors.append(getRandomColor())
    else:
        colors = [getRandomColor()] * fishLength

    if colorPattern == "head-tail":
        headTailColor = getRandomColor()
        # 头和尾巴 颜色一致
        colors[0] = headTailColor
        colors[-1] = headTailColor

    fish = {
        "right": fishType['right'],
        "left": fishType['left'],
        "colors": colors,
        "hSpeed": random.randint(1, 6),
        "vSpeed": random.randint(5, 15),
        "timeToHDirChange": random.randint(10, 60),
        "timeToVDirChange": random.randint(2, 20),
        "goingRight": random.choice([True, False]),
        "goingDown": random.choice([True, False]),
        'x': random.randint(LEFT_EDGE, RIGHT_EDGE),
        'y': random.randint(TOP_EDGE, BOTTOM_EDGE),
    }

    return fish


def simulationAquarium():
    """模拟浴缸中 鱼 泡泡 水草  泡泡生成器 动一步的场景"""
    global FISHES
    global BUBBLE_MACHINES
    global BUBBLES
    global KELPS
    global STEP

    # 模拟鱼动第一步
    for fish in FISHES:
        # 鱼第一次都是水平移动 如果步数等于他一次横向移动的速度
        # 他就可以移动
        if STEP % fish['vSpeed'] == 0:
            # 假设鱼是往右方向移动
            if fish["goingRight"]:
                # 还要看鱼初始位置是否在极限位置
                if fish['x'] != RIGHT_EDGE:
                    fish['x'] += 1
                else:
                    fish['goingRight'] = False  # 鱼在最右面 不能往右走了
                    fish['colors'].reverse()

            else:
                if fish['x'] != LEFT_EDGE:
                    fish['x'] -= 1
                else:
                    fish['goingRight'] = True
                    fish['colors'].reverse()
        # 鱼可以随机改变左右前进的方向
        fish['timeToHDirChange'] -= 1
        if fish['timeToHDirChange'] == 0:
            fish['goingRight'] = not fish['goingRight']
            fish['timeToHDirChange'] = random.randint(10, 60)

        # 改变垂直
        if STEP % fish['vSpeed'] == 0:
            if fish['goingDown']:
                if fish['y'] != BOTTOM_EDGE:
                    fish['y'] += 1
                else:
                    fish['goingDown'] = False
            else:
                if fish['y'] != TOP_EDGE:
                    fish['y'] -= 1
                else:
                    fish['goingDown'] = True

        fish['timeToVDirChange'] -= 1
        if fish['timeToVDirChange'] == 0:
            fish['goingDown'] = not fish['goingDown']
            fish['timeToVDirChange'] = random.randint(2, 20)

    # 模拟泡泡第一步
    # 生成泡泡
    for bubble_machine in BUBBLE_MACHINES:
        # 泡泡生成器有五分之一的机会产生泡泡
        if random.randint(1, 5) == 1:
            # 默认的泡泡位置在 泡泡生成器的x 位置 和最底下
            BUBBLES.append({'x': bubble_machine, 'y': HEIGHT - 2})

    # 泡泡出发第一步
    for bubble in BUBBLES:
        # 泡泡默认的总是会向上移动
        bubble['y'] -= 1
        diceRoll = random.randint(1, 6)
        if diceRoll == 1 and bubble['x'] != LEFT_EDGE:
            bubble['x'] -= 1
        elif diceRoll == 4 and bubble['x'] != RIGHT_EDGE:
            bubble['x'] += 1

    # 泡泡一旦到最上面 就爆炸
    # 反着删 不会出现问题
    for i in range(len(BUBBLES)-1, -1, -1):
        if BUBBLES[i]['y'] == TOP_EDGE:
            del BUBBLES[i]

    # 模拟水草漂浮一步
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            # 水草有 二十分之一的概率 摇晃
            if random.randint(1, 20) == 1:
                if kelpSegment == "^":
                    kelp['segments'][i] = "v"
                else:
                    kelp['segments'][i] = "^"


def drawAquarium():
    """在屏幕上画水箱"""
    global FISHES
    global BUBBLE_MACHINES
    global BUBBLES
    global KELPS
    global STEP

    # 退出的提示信息
    bext.fg("white")
    bext.goto(0, 0)
    print("fish tank Ctrl-c to quit")

    # 开始画泡泡
    bext.fg("white")
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(random.choice(('o', 'O')), end=" ")

    # 开始画鱼
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])
        # 根据鱼的方向 显示鱼的身体
        if fish['goingRight']:
            fishText = fish['right'][STEP % len(fish['right'])]
        else:
            fishText = fish['left'][STEP % len(fish['left'])]

    # 给鱼的身体染上正确的颜色
    for i, fishPart in enumerate(fishText):
        bext.fg(fish['colors'][i])
        print(fishPart, end=" ")

    # 开始画水草
    bext.fg("green")
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if kelpSegment == "(":
                bext.goto(kelp['x'], BOTTOM_EDGE - i)
            else:
                bext.goto(kelp['x'] + 1, BOTTOM_EDGE - i)
            print(kelpSegment, end=" ")

    # 开始画沙子
    bext.fg("yellow")
    bext.goto(0, HEIGHT - 1)
    print(chr(9617) * (WIDTH - 1), end="")

    sys.stdout.flush()


def clearAquarium():
    """在屏幕上擦除内容"""
    global FISHES
    global BUBBLES
    global BUBBLE_MACHINES
    global KELPS

    # 清除气泡
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(" ", end=" ")

    # 清除鱼
    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])
        print(" " * len(fish['left'][0]), end=" ")

    # 清除水草
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            bext.goto(kelp['x'], HEIGHT - 2 - i)
            print(" ", end=" ")

    sys.stdout.flush()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
