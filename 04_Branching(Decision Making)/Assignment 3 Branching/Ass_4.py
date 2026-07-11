# Write a program to input all sides of a triangle and check whether triangle is valid or
# not.
# A triangle is valid if the sum of any two sides is greater than the third side.

side1 = float(input("Enter the length of side 1:"))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3:"))

if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")
