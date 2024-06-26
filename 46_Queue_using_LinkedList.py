
class Node():
    def __init__(self, a_number):
        self.data = a_number
        self.next = None

# now we are going to define a class for the linked list

class Queue():
    def __init__(self,size):
        self.front = None  # Stores the front/head node
        self.rear = None  # Stores the Rear
        self.size = size  # Stores the Rear
        self.length = 0
    

    def isFull(self):
        return self.length == self.size # If True means the Queue is Full

    def isEmpty(self):
        return self.front == None 

    def enqueue(self,value):

        if self.isFull():
            print('Queue Overflow')
        else:
            self.length += 1
            # Handling the special case where we are inserting the head
            if self.isEmpty():
                self.front = self.rear = Node(value)
                print('Head/Front Enqueued - ', value)
            else:
                # This means that queue already has elements
                ptr = Node(value)
                self.rear.next = ptr
                self.rear = ptr
                print('Element Enqueued - ', value)

    def dequeue(self):
        if not self.isEmpty():
            self.length -= 1
            previous_front = self.front
            self.front = self.front.next
            value = previous_front.data
            previous_front = None
            print('Dequeuing the element -', value)
            return value
        else:
            print('The Queue is Empty')

    # now we are gonna write a function that travers through the linked list
    def show_elements(self):
        current_node = self.front
        while current_node is not None:
            print("Element : ",current_node.data)
            current_node = current_node.next
        

    
    # a function to get a node usnig index
    def get_element(self, index):
        current_node = self.front

        i = 0
        while current_node is not None:
            if i == index:
                return current_node.data
            current_node = current_node.next
            i += 1
        return None            

q1 = Queue(100)

q1.show_elements()
q1.dequeue()

q1.enqueue(22)
q1.enqueue(19)
q1.enqueue(74)
q1.enqueue(33)

q1.show_elements()
print(q1.front.data,q1.rear.data)

q1.dequeue()
q1.dequeue()

q1.show_elements()
print(q1.front.data,q1.rear.data)

print('The length of the queue is - ', q1.length)