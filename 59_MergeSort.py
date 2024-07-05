
# MergeSort alorithm - Time Complexity is O(nlogn) , Space Complexity - O(n), It is not Adaptive , not in-place sorting algorithm, It is Stable 

def merge(array1,array2):

    merged = []
    i,j = 0, 0

    while i < len(array1) and j < len(array2):

        if array1[i] <= array2[j]:
            merged.append(array1[i])
            i += 1
        else:
            merged.append(array2[j])
            j += 1

    # now we gotta get the remaining tails 
    array1_tail = array1[i:]
    array2_tail = array2[j:]

    return merged + array1_tail + array2_tail

def mergeSort(array):

    if len(array) <= 1 :  # This will make sure that the array has more than 1 element
        return array
    
    # Now getting the Mid Point
    mid = len(array)//2

    # Now splittig the array into left and right
    left = array[:mid]
    right = array[mid:]

    # recursively apply merge sort until its divided till one element
    left_sorted , right_sorted = mergeSort(left), mergeSort(right)

    sorted_array = merge(left_sorted, right_sorted)

    return sorted_array

A = [9, 1, 4, 14, 4, 15, 6]

print(A) # Printing Array before Sorting

A = mergeSort(A)

print(A) # Printing Array after MergeSort



