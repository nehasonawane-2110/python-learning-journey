# second maximum number in the list -
li = [10, 80, 20, 30, 40, 50, 70]
max = li[0]
smax = 0        # we assume that second max element is 0 
for i in range(1, len(li)):   # loop from second element
    if (li[i] > max):         # if current element > max
        smax = max            # update second max
        max = li[i]           # update max
    elif (li[i] > smax):      # if element > second max
        smax = li[i]          # update second max

print("Maximum element in the list is:", max)
print("Second maximum element in the list is:", smax)
