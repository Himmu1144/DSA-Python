# There are two types of DEQueues - 1) input restricted DEQueue - where you cant enqueue from front , 2) Output restricted where you cant dequeue from the rear.


class DEQueue():
    def __init__(self,size):
        self.size = size
        self.f = -1
        self.r = -1
        self.arr = [None]*size

    def isEmpty(self):
        return self.f == self.r

    def isFull(self):
        return self.r == (self.size - 1)
    
    def enqueueRear(self, value):
        if self.isFull():
            print('Queue Overflow')
        else:
            self.r += 1
            self.arr[self.r] = value

    def enqueueFront(self, value):
        if self.isFull() and self.f != -1:
            print('Queue Overflow')
        else:
            self.arr[self.f] = value
            self.f -= 1
        
    def dequeueFront(self):
        a = -1
        if not self.isEmpty():
            self.f += 1
            a = self.arr[self.f] 
        return a
    
    def dequeueRear(self):
        a = -1
        if not self.isEmpty():
            a = self.arr[self.r] 
            self.arr[self.r] = None
            self.r -= 1
        return a
    
    def show(self):
        if not self.isEmpty():
            return self.arr[self.f+1:self.r+1]

q1 = DEQueue(100)
q1.enqueueRear(10)
q1.enqueueRear(12)
q1.enqueueRear(18)
q1.enqueueRear(19)

q1.dequeueFront()
q1.dequeueFront()

print(q1.show(),q1.f,q1.r)

q1.enqueueFront(21)
q1.dequeueRear()

print(q1.show(),q1.f,q1.r)