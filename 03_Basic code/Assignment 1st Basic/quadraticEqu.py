# Program to Find the Roots of a Quadratic Equation.

# take the input from the user

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

ans = b**2 - 4 * a * c
ans = ans ** 0.5  # square root = 1/2 = 0.5 value
root1 = (-b + ans) / (2 * a)
root2 = (-b - ans) / (2 * a)
print(f'The root of the quadratic equation are {root1} and {root2}.')
