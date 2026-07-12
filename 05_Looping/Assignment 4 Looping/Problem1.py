# WAP to print the even number  until n.

# using while loop 
num = int(input("Enter the number: "))
i = 1
while (i <= num):
    if (i % 2 == 0):
        print(i)
    i += 1

# using for loop

n = int(input("Enter the number: "))
for num in range(1, n + 1):  #(n+1) is used to include n in the range.
    if (num % 2 == 0):
        print(num, end=' ')  # end='  is used to print the output in the same line with space between them.
