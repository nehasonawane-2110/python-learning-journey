# Sorting Techniques 
# - sorting techniques are method used to arrange elements of list in a specific order.
# common sorting techniques are:
# 1. Bubble sort
# 2. selection sort
# 3. insertion sort
# 4. merge sort
# 5. quick sort


### Bubble sort
# - bubble sort is a simple sorting technique where adjacent elements are compared and swappwd if they are in wrong order.
# - it keep repeating this process until the list is sorted.
# example 
def BubbleSort(li):
    for i in range(1, len(li)):
        # outer loop for number of passes

        for j in range(len(li) - 1):
            # inner loop to compare adjacent elements

            if (li[j] > li[j + 1]):
                # check if current element is greater than next

                li[j], li[j + 1] = li[j + 1], li[j]
                # swap elements

                print(li)
                # print list after each swap

    return li
    # return sorted list


li = [60, 50, 40, 30, 20, 10]
print("List before sort: ", li)
res = BubbleSort(li)
print("List after sort: ", res)
