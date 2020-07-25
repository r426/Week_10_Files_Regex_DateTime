# Write a Python program to print the date of all the Sundays of a given year.
#
# The user should be able to input a year and get all the dates which were a Sunday.
#
# Sample Input: 2020
# Sample Output:
# 2020-01-05
# 2020-01-12
# 2020-01-19
# 2020-01-26
# 2020-02-02
# -----
# 2020-12-06
# 2020-12-13
# 2020-12-20
# 2020-12-27

# Built following:
# https://www.codespeedy.com/how-to-find-all-sundays-of-a-calendar-year-in-python/

from datetime import date
import calendar

try:
    userInput = input("Enter a year: ")
    assert userInput.isnumeric() and 0 <= int(userInput) <= 9999, "Invalid number."
except AssertionError as object:
    print(object)
    exit()

year = int(userInput)
calendarObj = calendar.TextCalendar(calendar.SUNDAY)
print("Sundays of year %d:" % year)

for month in range(1, 13):
    for monthday in calendarObj.itermonthdays(year, month):
        if monthday != 0:
            day = date(year, month, monthday)
            if day.weekday() == 6:
                print("%d-%02d-%02d" % (year, month, monthday))
