# Binary search Technique(algorithm)
# - Binary search is the fast searching technique that work onlu on a stored list.
# - instead of checking one by one (like linear search)
# - find the middle element
# - comapre it with target value
# - eliminate half of the list each time
# - it divided into tow part
# example -

def BinarySearch(li, searchEle):
    beg = 0
    end = len(li) - 1
    while (beg <= end):
        # print("in loop")
        mid = (beg + end) // 2
        if (li[mid] == searchEle):
            return mid
        elif (li[mid] < searchEle):
            beg = mid + 1
        elif (li[mid] > searchEle):
            end = mid - 1
    else:
        return -1


li = [10, 20, 30, 40, 50, 60, 70]
searchEle = int(input('Enter the element to search: '))
res = BinarySearch(li, searchEle)
if (res != -1):
    print(f'{searchEle} is found in the list index {res}.')
else:
    print(f'{searchEle} is not found in the list at index {res}.')


# commented code -
def BinarySearch(li, searchEle):
    beg = 0
    # starting index of list

    end = len(li) - 1
    # last index of list

    while (beg <= end):
        # loop runs until search space is valid

        mid = (beg + end) // 2
        # find middle index

        if (li[mid] == searchEle):
            # check if middle element is target

            return mid
            # return index if found

        elif (li[mid] < searchEle):
            # if middle element is smaller than target

            beg = mid + 1
            # move to right side

        elif (li[mid] > searchEle):
            # if middle element is greater than target

            end = mid - 1
            # move to left side

    else:
        return -1
        # return -1 if element not found


li = [10, 20, 30, 40, 50, 60, 70]
# sorted list (important for binary search)

searchEle = int(input('Enter the element to search: '))

res = BinarySearch(li, searchEle)
# call function and store result

if (res != -1):
    # if element is found

    print(f'{searchEle} is found in the list index {res}.')
    # print index

else:
    print(f'{searchEle} is not found in the list at index {res}.')
    # print not found message
