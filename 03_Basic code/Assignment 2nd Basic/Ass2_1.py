# Convert the time entered in hh,min and sec into seconds.
hh = int(input("Enter Hours: "))
min = int(input("Enter Minutes: "))
sec = int(input("Enter Seconds:  "))

totalSeconds = (hh * 3600) + (min * 60) + sec    # 60 * 60 = 3600
print(f'Total Seconds: {totalSeconds}')
