
# COuntSort - Time Complexity - O(n) similar to O(m+n), Space Complexity - O(m), where m = max(array) + 1, not stable , not adaptive , not in-pace

def countSort(array):

    max_num = max(array)
    count = [0]*(max_num + 1)

    for i in array:
        count[i] = count[i] + 1

    i,j = 0,0

    while(i<=max_num):
        if count[i] > 0:
            array[j] = i   
            count[i] = count[i] - 1
            j += 1
        else:
            i += 1


A = [9, 1, 4, 14, 4, 15, 6]

print(A)
countSort(A)
print(A)


