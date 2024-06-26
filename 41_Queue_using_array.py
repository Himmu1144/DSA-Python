
class Queue():
    def __init__(self,size):
        self.size = size
        self.f = -1
        self.r = -1
        self.arr = [None]*size

    def isEmpty(self):
        return self.f == self.r

    def isFull(self):
        return self.r == (self.size - 1)
    
    def enqueue(self, value):
        if self.isFull():
            print('Queue Overflow')
        else:
            self.r += 1
            self.arr[self.r] = value
        
    def dequeue(self):
        a = -1
        if not self.isEmpty():
            self.f += 1
            a = self.arr[self.f] 
        return a
    
    def show(self):
        if not self.isEmpty():
            return self.arr[self.f+1:self.r+1]

q1 = Queue(100)
q1.enqueue(10)
q1.enqueue(12)
q1.enqueue(18)
q1.enqueue(19)

q1.dequeue()
q1.dequeue()

print(q1.show(),q1.f,q1.r)