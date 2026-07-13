# 2). Write a program to calculate area of circle

def areaOfCircle(radius):
    area = 3.14 * radius * radius
    return area


r = float(input("Enter the radius: "))
res = areaOfCircle(r)
print(res)
