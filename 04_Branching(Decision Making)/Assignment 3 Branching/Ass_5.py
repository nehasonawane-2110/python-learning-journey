# Write a program to check whether the triangle is equilateral, isosceles or scalene
# triangle.

side1 = float(input("Enter the first side of triangle: "))
side2 = float(input("Enter the second side of triangle: "))
side3 = float(input("Enter the third side of triangle: "))

if (side1 == side2 == side3):      # euilateral triangle are all side are equal.
    print("The triangle is equilateral.")
elif (side1 == side2) or (side2 == side3) or (side1 == side3):   # isosceles triangle two angle are equal.
    print("The triangle is isosceles.")
else:                                # scalene triangle all side are different.
    print("The triangle is scalene.")
