# 3. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

def countElement(li, searchEle):
    count = 0
    for i in range(len(li)):
        if (li[i] == searchEle):
            count += 1   # if element is found then increase count by 1
    return count


li = [10, 20, 30, 30, 50, 40, 10, 50]
searchEle = int(input('Enter the element to search: '))
res = countElement(li, searchEle)
if (res > 0): # if count is greater than 0 then element is present in the list
    print(f'{searchEle} is found in the list {res} times')
else:
    print(f'{searchEle} is not found in the list')
