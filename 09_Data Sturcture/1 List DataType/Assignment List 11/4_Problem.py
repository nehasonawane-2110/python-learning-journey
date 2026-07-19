# 4) Python Program to Find the Second Largest Number in a List Using Bubble Sort

li = [10, 40, 20, 60, 50, 30]
n = len(li)    # total ele in list
for i in range(n):  # check the list multile times
    for j in range(0, n - i - 1):    # 0 from start to n-i-1 because last i elements are already in place
        if li[j] > li[j + 1]:    # current ele is bigger than swap
            li[j], li[j + 1] = li[j + 1], li[j]      # swap
print(f'Second largest element in the list is: {li[-2]}')
