# write the program to calculate the total salary of
# employee Based on basic da = 10% of basic ta = 12% of basic hra = 15% of basic.

basic = float(input("Enter the basic salary:"))
da = (10 / 100) * basic
ta = (12 / 100) * basic
hra = (15 / 100) * basic
totalSalary = basic + da + ta + hra
print(f'Total salary is: {totalSalary}')
