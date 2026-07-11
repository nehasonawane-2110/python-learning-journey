# WAP to calculates the Days year week and day.

days = int(input("Enter the number of days: "))  # input for days

year = days // 365    # calculating year
days = days % 365      # remaining days after calculating year
week = days // 7      # calculating week
days = days % 7       # remaining days after calculating week
print(f'{year}year, {week} week, days is: {days}.')  # print the result
