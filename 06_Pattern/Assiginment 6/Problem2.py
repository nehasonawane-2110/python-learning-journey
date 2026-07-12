# write program to print the following pattern:
# 1
# 2 3
# 4 5 6
# 7 8 9 10


k = 1   # variable to keep track of the current number to print
for i in range(1, 5):
    for j in range(1, i + 1):
        print(k, end=" ")    # print the current number following by a space
        k += 1   # increment the number like 1+1= 2, 2+1=3, and so on
    print()
