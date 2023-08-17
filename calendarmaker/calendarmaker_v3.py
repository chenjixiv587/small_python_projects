import datetime
# set up the constants
DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday")
MONTHS = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")
print("Welcome to the calendar display system")


# ask the user to get the valid year
while True:
    print("Please enter a valid year")
    response = input("> ").strip()
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    print("Please enter the numeric string")
    continue

# ask the user to get the valid month
while True:
    print("Please enter the valid month")
    response = input("> ").strip()
    if not response.isdecimal():
        print("Please enter the numeric string")
        continue
    response = int(response)
    if 1 <= response <= 12:
        month = response
        break


def getCalendarFor(year: int, month: int):
    # define the display string
    calText = ""
    # display the month and year at the top of the calendar
    calText += " " * 34 + str(MONTHS[month - 1]) + " " + str(year) + "\n"
    calText += "....Sunday...Monday...Tuesday...Wednesday..Thrusday..Friday..Saturday...\n"
    weekSeparator = "+----------" * 7 + "|\n"
    rowBlank = "|            " * 7 + "\n"

    currentDate = datetime.date(year=year, month=month, day=1)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)
    # show the main content

    while True:
        calText += weekSeparator
        rowDays = ""
        # show the each row of the day
        for i in range(0, 7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            rowDays += "|" + dayNumberLabel + " " * 7
            # get the next day
            currentDate += datetime.timedelta(days=1)
            # print(currentDate, currentDate.month, end="")
        rowDays += "|\n"
        calText += rowDays
        for _ in range(0, 3):
            calText += rowBlank

        # 需要在一行输出7天之后 再判断
        if currentDate.month != month:
            break

    calText += weekSeparator
    return calText


calText = getCalendarFor(year=year, month=month)
storeCalendarFile = f"{year}_{month}.txt"
with open(storeCalendarFile, "w") as f:
    f.write(calText)
print(f"File saved to {storeCalendarFile}")
