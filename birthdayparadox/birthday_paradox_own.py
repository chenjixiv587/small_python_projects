"""
需求：算出一定数量的人数中 生日相同的概率
思路：
1 询问一次需要生成多少个随机的生日 注意校验
2 利用getBirthdays() 生成随机的生日
3 利用getMatch() 获取相同的生日的日期
4 模拟 100,000 次 计算生日相同的概率
"""


import datetime
import random


def main():

    while True:  # Keep looping  until the user enter the valid data
        print('How many birthdays do you want to generate? (max 100)')
        birthdayCount = input('> ')
        if birthdayCount.isdecimal() and (0 < int(birthdayCount) <= 100):
            numBDdays = int(birthdayCount)
            break
        else:
            print('please enter the valid data: ')

    def getBirthdays(numBDdays):
        """Return the random birthdays list"""
        birthdays = []
        baseBirthday = datetime.date(month=1, day=1)
        for i in range(0, numBDdays):
            birthday = datetime.timedelta(
                days=random.randint(0, 364)) + baseBirthday
            birthdays.append(birthday)
        return birthdays

    def getMatch(birthdays):
        """Return the macth one"""
        for a, birthdayA in enumerate(birthdays):
            for b, birthdayB in enumerate(birthdays[a + 1:]):
                if birthdayA == birthdayB:
                    return birthdayA

    # make the birthdays perform by month
    birthdays = getBirthdays(numBDdays)
    MONTHs = ['Jan', 'Feb', 'Mat', 'Apr', 'May', "Jun",
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(', ', end="")
        monthOfBirthday = MONTHs[birthday.month - 1]
        dayOfBirthday = birthday.day
        print(f'{monthOfBirthday} {dayOfBirthday}', end='')

    print()
    print()

    # show the match one
    match = getMatch(birthdays)
    if match is not None:
        matchMonth = MONTHs[match.month - 1]
        macthDay = match.day
        print(f'{matchMonth} {macthDay}', end='')
    else:
        print('There are no same birthdays')
    print()
    print()

    # Simulations 100,000 times
    simMacth = 0
    for i in range(0, 100_000):
        if i % 10_000 == 0:
            print(f'{i} simulations run..')
        birthdays = getBirthdays(numBDdays)
        match = getMatch(birthdays)
        if match is not None:
            simMacth += 1
    percentMatch = round(simMacth * 100 / 100_000, 2)
    print(percentMatch)
    print('100,000 simulations run.')


if __name__ == "__main__":
    main()
