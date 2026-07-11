# WAP to calculate total salary of employee based on basic, da=10% of basic,
# ta=12% of basic, hra=15% of basic.

Basic = float(input("Enter the basic salary of employee: "))
ta = (12 / 100) * Basic
da = (10 / 100) * Basic
hra = (15 / 100) * Basic
Total_Salary = Basic + ta + da + hra
print(f'The total salary of employee is: {Total_Salary}.')
