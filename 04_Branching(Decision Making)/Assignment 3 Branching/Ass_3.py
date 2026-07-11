# Write a program to input angles of a triangle and check whether triangle is valid or not.
# in the above program we take three angle of triangle from user anf chack the triangle is valid or not.
# 60 degree + 60 degree + 60 degree = 180 degree(valid triangle)


angle1 = float(input("Enter the first angle of triangle: ")) # take the input from user
angle2 = float(input("Enter the second angle of triangle: "))
angle3 = float(input("Enter the third angle of triangle: "))
if (angle1 + angle2 + angle3) == 180:    # sum of all angle is equal to 180 degree.
# total addition of triangle angle is 180 degree.
    print(f'Triangle is valid.')   # print valid triangle.
else:
    print(f'Triangle is not valid.')


