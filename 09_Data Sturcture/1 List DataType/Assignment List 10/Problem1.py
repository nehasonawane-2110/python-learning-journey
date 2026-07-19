# 1.Write a program to find sum of all elements of list

def sumOfList(li):
    sum = 0  # initialize 0 is first element
    for i in range(len(li)):      # loop through each elements of list and len(li) give total ele in list
        sum += li[i]
    return sum

li = [10, 20, 30, 40, 50]
res = sumOfList(li)
print(f' sum of all elements in the list is: {res}')
