# Linear search Technique(algorithm)
# - One by one elements are Fetched - Traversing
# - Linar search is the simplest searching technique it check each element in list one by one until it finds the target value.
# example -

def LinearSearch(li, searchEle):
    for ind in range(len(li)): 
        # loop through each index of list

        if (li[ind] == searchEle):
            # check if current element matches search element

            return ind
            # return index if element found

    else:
        return -1
        # return -1 if element not found


li = [12, 35, 84, 53, 67]
# list of elements

searchEle = int(input("Enter the element to search: "))
# take input from user and convert to integer

res = (LinearSearch(li, searchEle))
# call function and store result

if (res != -1):
    # if element is found

    print(f'{searchEle} is found in the list index {res}.')
    # print index of found element

else:
    print(f'{searchEle} is not found in the list at index {res}.')
    # print message if not found
