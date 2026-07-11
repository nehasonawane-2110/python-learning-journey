# Write a Program to input two angles from user and
# find third angle of triangle.

# take two angle from the user.
angle1 = float(input("Enter the first angle: "))
angle2 = float(input("Enter the seond angle: "))

# formula to take third angle of triangle
angle3 = 180 - (angle1 + angle2)

# display the result
print(f'Third angle of triangle, {angle3}.')
