# 1) Python Program to Put Even and Odd elements of a List into two Different Lists.
def separateEvenOdd(li):
    even = []
    odd = []
    for i in li:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd


li = [1, 2, 3, 4, 6, 7, 10, 15, 20]
even, odd = separateEvenOdd(li)
print("Even List:", even)
print("Odd list:", odd)
