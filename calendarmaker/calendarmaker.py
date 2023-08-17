import datetime


# set up the constants
DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday")
MONTHS = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

print("Calendar Maker by bruce.chen")

while True:  # loop to get a year from the user
    print("Enter the year for the calendar.")
    response = input("> ").strip()

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print("Please enter a numeric year, like 2023")
    continue


while True:  # loop to get a month from user
    print("Enter a month for the calendar, like  1 - 12")
    response = input("> ").strip()
    if not response.isdecimal():
        print("Please enter a numeric month , like 3 for March")
        continue
    month = int(response)
    if 1 <= month <= 12:
        break

    print("Please enter a numeric month, 1 - 12")


def getCalendarFor(year: int, month: int):
    calText = ""  # calText will contain the string of our calendar

    # put the month and year at the top of the calendar
    calText += (" " * 34) + MONTHS[month - 1] + " " + str(year) + "\n"

    # add the days of the week labels to the calendar
    # (!) try changing this to abbreviations : SUN, MON, TUE, etc.
    calText += "...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n"

    # the horizontal line string that separate weeks
    weekSeparator = ("+----------" * 7) + "+\n"

    # the blank rows have ten spaces in between the | day separators:
    blankRow = ("|         " * 7) + "|\n"

    # get the first date in the month.(the datetime module handles all
    # the complicated calendar stuff for us here.)
    currentDate = datetime.date(year, month, 1)

    # roll back currentDate until it is Sunday(Weekday() returns 6
    # for sunday , not 0.)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:  # loop over each week in the month.
        calText += weekSeparator
        # dayNumberRow is the row with the day number labels
        dayNumberRow = ""
        for i in range(0, 7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += "|" + dayNumberLabel + (" " * 7)
            currentDate += datetime.timedelta(days=1)  # go to next day
        dayNumberRow += "|\n"  # add the vertical line after saturday

        # add the day number row and 3 blank rows to the calendar text
        calText += dayNumberRow
        for i in range(3):  # (！)try changing the 4 to a 5 or 10
            calText += blankRow

        # check if we're done with the month
        if currentDate.month != month:
            break
    # add the horizontal line at the very bottom of the calendar
    calText += weekSeparator
    return calText


calText = getCalendarFor(year, month)
print(calText)  # display the calendar


# save the calendar to a text file

calendarFilename = f"calendar_{year}_{month}.txt"
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)

print(f"saved to {calendarFilename}")
