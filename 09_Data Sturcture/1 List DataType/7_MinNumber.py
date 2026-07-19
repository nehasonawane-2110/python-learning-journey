# minimum number in the list -
li = [10, 20, 50, 30, 40, 70]
min = li[0]
for i in range(1, len(li)):
    if (li[i] < min):
        min = li[i]

print("Minimum element in the list is:", min)
