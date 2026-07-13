# Write a program to check if entered year is a leap year or not.

def LeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter the year: "))
if LeapYear(year):
    print(year, "is a Leap year.")
else:
    print(year, "is not a leap year.")
