# WAP to find the maximum number in a list.

li = [10, 20, 50, 30, 40, 70]
max = li[0]         # we are assuming that the first element is the maximum element in the list.
for i in range(1, len(li)):   # i is index of list and reange start from 1 because we are assuming that the first elements max li[0] is max element in the list
    if (li[i] > max):
        max = li[i]     # if the current element is greater than the maximum element then we update the maximum element to the current element

print("Maximum element in the list is:", max)