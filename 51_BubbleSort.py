
# Bubble Sortis used to sort an array
# Bubble Sort - Time Complexity - O(n^2) , Space Complexity - inplace sorting algorithim , Adaptive Initially Not

def bubbleSort(arr,n):
    for i in range(n-1):
        # This loop will run the number of passes which goes to 5 passes 0 1 2 3 4 for an arr of 6 elements so basically loop of 0 < n-1

        print('Pass Number - ',i+1)
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                # here we are gonna swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
# Adaptive version of bubble sort
def bubbleSortAdaptive(arr,n):
    for i in range(n-1):
        # This loop will run the number of passes which goes to 5 passes 0 1 2 3 4 for an arr of 6 elements so basically loop of 0 < n-1

        print('Pass Number - ',i+1)

        isSorted = 1
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                # here we are gonna swap the elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSorted = 0

        if isSorted:
            return

# arr = [12,54,65,60,23,9]
arr = [1,2,3,4,78,92,45]
print(arr) # printing the array before sorting

# bubbleSort(arr,len(arr))
bubbleSortAdaptive(arr,len(arr))

print(arr) # printing the array after sorting