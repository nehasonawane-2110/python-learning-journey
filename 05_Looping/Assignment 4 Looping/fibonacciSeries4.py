# WAP to print fibonacci series upto n. 
num = int(input("Enter Number: "))
a = -1
b = 1
for i in range(num):
    c = a + b
    print(c, end=' ')
    a = b   # Move 'a' forward (shift values).
    b = c   # Move 'b' forward (update to latest number).
