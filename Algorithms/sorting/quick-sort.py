'''
Algorithm:
1) pick an element  and put all the elements less than it to the left and all the elements greater than it to the right
2) repeat step 1 for sub-arrays

Time Complexity:
worst-case: O(n**2)
average-case: O(nlogn)
best-case: O(nlogn)

Space Complexity:
O(nlogn)
'''

def quickSort(arr, l, r):

    if l >= r:
        return arr

    x = arr[l]
    i = l
    j = r

    while i <= j:
        while arr[i] < x:
            i += 1
        while arr[j] > x:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    quickSort(arr, l, j)
    quickSort(arr, i, r)


    return arr


arr = [11,1,22,2,100]

quickSort( arr, 0, len(arr)-1)