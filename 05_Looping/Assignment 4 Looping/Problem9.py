# WAP to print all numbers in a range divisible by a given number.

start = int(input("Enter the starting No: "))
end = int(input("Entre the Ending No : "))
divisor = int(input("Entre the Divisor: "))

for i in range(start, end + 1):
    if (i % divisor == 0):
        print(i)
