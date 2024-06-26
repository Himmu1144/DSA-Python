
# In Normal queue the storage was getting used inefficiently thats why we use circular queue

class circularQueue():
    def __init__(self,size):
        self.size = size
        self.f = 0
        self.r = 0
        self.arr = [None]*size

    def isEmpty(self):
        return self.f == self.r

    def isFull(self):
        return (self.r + 1)%self.size == self.f
    
    def enqueue(self, value):
        if self.isFull():
            print('Queue Overflow')
        else:
            print('Enquing Element - ',value)
            self.r = (self.r + 1)%self.size 
            self.arr[self.r] = value
        
    def dequeue(self):
        a = -1
        if not self.isEmpty():
            self.f = (self.f + 1)%self.size
            a = self.arr[self.f] 
            self.arr[self.f] = None
        return a
    
    def show(self):
        return self.arr

q1 = circularQueue(5)
print(q1.show(),q1.f,q1.r)

q1.enqueue(10)
q1.enqueue(12)
q1.enqueue(18)
q1.enqueue(19)

print(q1.show(),q1.f,q1.r)
print(q1.isFull())
q1.enqueue(10)



print(f'Dequeuing element - ',q1.dequeue())
print(f'Dequeuing element - ',q1.dequeue())
q1.enqueue(10)
q1.enqueue(11)
q1.enqueue(12)
print(q1.show(),q1.f,q1.r)
