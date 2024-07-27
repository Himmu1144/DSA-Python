# Breadth First Search (BFS) | Uses Queue DS (First in First Out (FIFO))

'''
Algorithim -

input -  Graph (V,E) with source node s in V
Algo - 

Mark all nodes v in V as unvisited 
Mark source node s as visited
enqueue(Q,s) 
while (Q is not Empty)
    u =  dequeue(Q)
    for each unvisited neighbor v of u:
    mark v as visited
    enquque(Q,v)

'''


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

visited = [0]*7

# Graph in Matrix form
a = [
        [0,1,1,1,0,0,0],
        [1,0,1,0,0,0,0],
        [1,1,0,1,1,0,0],
        [1,0,1,0,1,0,0],
        [0,0,1,1,0,1,1],
        [0,0,0,0,1,0,0], 
        [0,0,0,0,1,0,0] 
]

size = len(a)

# Starting Node 
i = 0
visited[i] = 1
print(i,end="")
q1.enqueue(i)

while(not q1.isEmpty()):
    node = q1.dequeue()
    for j in range(size):
        if a[node][j] == 1 and visited[j] == 0:
            # This means its linked and not visited so add it in visited and enqueue in the queue
            visited[j] = 1
            print(j,end="")
            q1.enqueue(j)


