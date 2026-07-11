# Write a program to enter P, T, R and calculate Compound Interest.
# This program calculates the compound interest based on the principal(p) amount
# time (T), and rate (R).
# input values form the user.
P = int(input("Enter the principle amount (P):"))
T = int(input("Enter the time in years (T):"))
R = int(input("Enter the rate of interest (R):"))

# calculate the amount using the formula A = P * (1 + R/100) ** T
A = P * (1 + R/100) ** T
# calculate the  compound interest
CI = A - P
# output the compound interest
print("Compound Interest is", CI)
# result display.
# Note: the formula for compound interest is CI = A - P,
# where A is the total amount after interest.
