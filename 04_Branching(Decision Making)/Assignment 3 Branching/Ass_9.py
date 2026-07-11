# Input 5 subject marks from user and display grade(eg.First class,Second class ..)

subject1 = float(input("Enter the marks for subject1: "))
subject2 = float(input("Enter the marks for subject2: "))
subject3 = float(input("Enter the marks for subject3: "))
subject4 = float(input("Enter the marks for subject4: "))
subject5 = float(input("Enter the marks for subject5: "))

total_markes = subject1 + subject2 + subject3 + subject4 + subject5
persentage = (total_markes/500) * 100
print(f'{persentage} persentage.')

if (persentage >= 85):
    print("you get first class")
elif (persentage >= 75):
    print("you get second class")
elif (persentage >= 40):
    print("Pass.")
else:
    print("you are failed.")
