# WAP to calculate the percentage of a 5 subject exam.
# input marks of 5 subjects.
# use int function to convert the input string to an integer
# total marks of 5 subject is 100

M1 = float(input("Enter the marks of subject 1: "))
M2 = float(input("Enter the marks of subject 2: "))
M3 = float(input("Enter the marks of subject 3: "))
M4 = float(input("Enter the marks of subject 4: "))
M5 = float(input("Enter the marks of subject 5: "))

Total_Marks = M1 + M2 + M3 + M4 + M5   # total makrs calculation
percentage = (Total_Marks / 500) * 100  # percentage calculation
print(f'The percentage of 5 subject is: {percentage}%.')   # print the percentage
