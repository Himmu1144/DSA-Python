class myArray:
    def __init__(self,total_size,used_size):
        self.total_size = total_size
        self.used_size = used_size
        self.data = [None]*total_size


    def show(self):
        for i in range(self.used_size):
            print(self.data[i])

    def setVal(self):
        i = 0
        while i < self.used_size:
            num = int(input(f'please enter element - {i}  : '))
            self.data[i] = num
            i += 1

    def indInsertion(self, element, index ):
        if self.used_size >= self.total_size:
            return -1
        else:
            i = self.used_size
            while (i >= index):
                self.data[i+1] = self.data[i]
                i -= 1
            self.data[index] = element
            self.used_size += 1
            return 1
        
    def indDeletion(self, index ):
        
        i = index
        while (i < self.used_size - 1):
            self.data[i] = self.data[i + 1]
            i += 1
        self.used_size -= 1
        
        




array1 = myArray(10,5)


# array1.show()
array1.setVal()

# Traversal
# array1.show()


# array1.data = [7,8,12,27,88]
print(array1.show(), "Total Size : ", array1.total_size, "Used Size : ",  array1.used_size)
# insertion_status = array1.indInsertion(45,1)
# print(array1.show(), "\nTotal Size : ", array1.total_size, "Used Size : ",  array1.used_size, "Insertion Status : ", insertion_status)

array1.indDeletion(2)
print(array1.show(), "\nTotal Size : ", array1.total_size, "Used Size : ",  array1.used_size)
