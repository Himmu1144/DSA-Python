
# The Time Complexity for insertion sort is also O(n^2)

def insertionSort(arr,n):
    # I is the number of passes
    for i in range(1,n):

        key = arr[i]    # The element that's gonna get compared to the sorted array
        j = i-1         # We are gonna loop each pass before the ith element , for i=3, sorted array j is 0 1 2
    
        # Now usnig the loop for each pass
        while(j>=0 and arr[j] > key): # means j can be -1 and gonna go from i-th element to 0 covering all the sorted array and compairing if the jth element is bigger than ith or not
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key
        

# arr = [7,12,54,65,23,9]
arr = [4, 2, 6, 3, 4, 6, 2, 1]

print(arr) # Printing the array before sorting
insertionSort(arr,len(arr))
print(arr) # Printing the array after using insertionSort
