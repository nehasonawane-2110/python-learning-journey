# 1). Write a program to calculate area of rectangle

def areaOfRectangle(length, breath):
    area = length * breath
    return area


length = int(input("Enter the length: "))
breath = int(input("Enter the breath: "))
res = areaOfRectangle(length, breath)
print("area of rectangle", res)
