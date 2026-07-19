# 5. WAP to create a list with elements according to user requirment

def createList(n):
    newList = []
    for i in range(n):
        ele = int(input(f"Enter element: "))   # take input from user and convert to integer
        newList.append(ele)        # add element to list
    return newList


n = int(input("Enter the number of elements you want to add in the list: "))
li = createList(n)
print(li)
 