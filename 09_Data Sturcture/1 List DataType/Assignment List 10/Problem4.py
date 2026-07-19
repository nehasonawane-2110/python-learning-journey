# 4. Write a program to remove duplicates from the list.
# function to remove duplicates

def removeDuplicates(li):
    newList = []
    # empty list to store unique elements

    for i in range(len(li)):
        # loop through each element

        if (li[i] not in newList):
            # check if element is not already in new list

            newList.append(li[i])
            # add unique element
     
    return newList
    # return final list after loop ends


li = [10, 20, 30, 50, 20, 40, 70]
res = removeDuplicates(li)
print(res)