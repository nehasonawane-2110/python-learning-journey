# 2) selction sort
# - selction sort is a sorting technique where you find the smallest element and place it at the correct position.
# select the smallest elements and swap with first element
# - then repeat for reamining unsorted list
# example

def SelectionSort(li):
    for i in range(len(li)):   # len(li) give total number of elements in list
        # outer loop for number of passes

        ind = i
        # assume current index is smallest

        for j in range(i + 1, len(li)):   # i + 1 to start from next element
            # inner loop to find smallest element in unsorted list

            if (li[j] < li[ind]):
                # check if current element is smaller than smallest
                ind = j
                # update index of smallest element
            li[i], li[ind] = li[ind], li[i]
            # swap smallest element with first element of unsorted list
            print(li)
    return li
    # return sorted list


li = [60, 50, 40, 30, 20, 10]
print("List before sort: ", li)
res = SelectionSort(li)
print("List after sort: ", res)