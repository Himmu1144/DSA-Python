

# The Time Complexity for selection sort is also O(n^2), It is neither Stable nor Adaptive

def selectionSort(arr,n):

    # I+1 is the number of passes
    for i in range(n-1): # number of passes are n-1

        # print('Pass Number - ',i+1,', i = ',i)
        minIndex = i     # initially we are taking i as the minimum index

        for j in range(i+1,n): 

            if arr[j] < arr[minIndex]:
                minIndex = j

        # Here we'll get a value of j as the min index, now swapping but we'll only swap if i is not j
        if i != minIndex:
            arr[i],arr[minIndex] = arr[minIndex], arr[i]

            



arr = [4, 2, 6, 3, 4]

print(arr) # Printing the array before sorting
selectionSort(arr,len(arr))
print(arr) # Printing the array after using selectionSort
