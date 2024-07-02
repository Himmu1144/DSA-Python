
# Quick Sort -
'''
Worst Case Complexity - O(n^2)
Best Case Complexity - O(nlogn)
'''

def partition(arr, low, high):
    # first we take the first element as pivot then we go from low+1 to high , starting from i,j at same start of pivot + 1 and check if j is less than pivot if yes than swap j with i and do i+1 this moves the small element right beside pivot and high at the right and in the end swap pivot with i-1 and return i-1 as pivotIndex pi

    pivot = arr[low]
    i = low+1
    for j in range(low+1, high+1):
        if arr[j] < pivot:
            # swap j with i and increment i
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    # now swap pivot with i-1 and return i-1 as pi
    arr[low], arr[i-1] = arr[i-1], arr[low]
    return i-1

def quickSort(arr, low, high):
    if low < high: # only start sorting when array is not empty
        pi = partition(arr , low, high)
        quickSort(arr, low, pi-1) # sort the left part
        quickSort(arr, pi+1, high) # sort the right part


nums = [5, 2, 9, 1, 5, 6]

print(nums) # before sorting

quickSort(nums, 0, len(nums)-1)

print(nums) # after sorting
