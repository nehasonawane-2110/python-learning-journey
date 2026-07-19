# Write a program to print all numbers which are divisible by m and n in the list.

def divisibleByMandN(li, m, n):
    newList = []
    for i in range(len(li)):
        if (li[i] % m == 0 and li[i] % n == 0):  # check if element is divisible by m and n
            newList.append(li[i])  
    return newList

li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
m = 10   # element which we want to check for divisibility
n = 5 
res = divisibleByMandN(li, m, n)
print(res)
