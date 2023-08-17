import datetime


# set up the constants
DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday")
MONTHS = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

print("Here is the calendar")


while True:  # keep looping until get the valid year
    print("Please enter the year")
    response = input("> ").strip()
    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    print("please enter the valid year")
    continue


while True:  # keep looping until get the valid month
    print("please enter the valid month, 1- 12")
    response = input().strip()
    if not response.isdecimal():
        print("Please enter a numeric month , like 3 for March")
        continue
    response = int(response)
    if 1 <= response <= 12:
        month = int(response)
        break


def showTheCalendar(year: int, month: int):
    calText = ""  # calText will contain the string of our calendar

    # put the month and year at the top of the calendar
    calText += (" " * 34) + MONTHS[month - 1] + " " + str(year) + "\n"

    # add the days of the week labels to the calendar
    calText += "...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n"
    # the horizontal line string that separate the weeks
    weekSeparator = ("+----------" * 7) + "+\n"

    # the blank rows have ten spaces in between the | day separators
    blankRow = ("|         " * 7) + "|\n"

    # get the first date in the month

    currentDate = datetime.date(year, month, 1)

    # roll back currentDate until it is Sunday
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:  # loop over each week in the month
        calText += weekSeparator
        # dayNumberRow is the row with the day number labels
        dayNumberRow = ""
        for i in range(0, 7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += "|" + dayNumberLabel + (" " * 7)
            currentDate += datetime.timedelta(days=1)  # get the next dat
        dayNumberRow += "|\n"  # add the vertical line after saturday

        # add the day number row and 3 blank rows to the calendar
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow

        # check if we're done with the month
        if currentDate.month != month:
            break

    # add the horizontal line at the very bottom of the calendar
    calText += weekSeparator
    return calText


calText = showTheCalendar(year, month)
print(calText)

calendarFileName = f"calendar_{year}_{month}.txt"
with open(calendarFileName, "w") as fileObj:
    fileObj.write(calText)

print(f"saved to {calendarFileName}")
