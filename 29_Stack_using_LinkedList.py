
# -----------------------------------------------------------------------------------------------------------
""" 
Creating Stack Uisng Linked List 

1) Side1/Head Side will be used for push and pop operations
2) Head is now Top
3) Stack is Empty when Top is Null
4) Stak is Full when Heap Memory is Exhausted
5) Custom size can be set 

"""

class Node():
    def __init__(self, a_number):
        self.data = a_number
        self.next = None

class LinkedList():

    def __init__(self,size):
        self.top = None
        self.max_size = size
    
    def push(self,value):
        if(self.isFull()):
            print('Stack Overflow')
        else:
            if self.top == None:
                self.top = Node(value)   
            else:
                next = self.top
                self.top = Node(value)
                self.top.next = next

    def isEmpty(self):
        return self.top == None
    
    def isFull(self):
        return self.length() == self.max_size
    
    def stackTop(self):
        return self.top.data
    
    def stackBottom(self):
        current_node = self.top
        while current_node.next is not None:
            current_node = current_node.next
        return current_node.data
    
    def pop(self):
        if self.isEmpty():
            print('The Stack is Empty')
            return -1
        else:
            popped_value = self.top.data
            self.top = self.top.next
            return popped_value
        
    def peek(self,position):
        if position == 1:
            return self.top.data
        
        if position <= self.length():
            current_node = self.top
            i = 1
            while current_node is not None:
                i += 1
                current_node = current_node.next
                if position == i:
                    return current_node.data
        else:
            return "Invalid Position"
        
        
    # now we are gonna write a function that travers through the linked list
    def show_elements(self):
        current_node = self.top
        while current_node is not None:
            print("Element : ",current_node.data)
            current_node = current_node.next

    # a function to show the length of the LL
    def length(self):
        current_node = self.top
        i = 0
        while current_node is not None:
            current_node = current_node.next
            i += 1
        return i
            
            
    

list1 = LinkedList(3)
list1.push(10) 
list1.push(20)
list1.push(30)
# list1.push(30)

print(list1.show_elements(), list1.length(), list1.stackBottom())
print("peeking at position - 2 : ", list1.peek(2))
    
list1.pop()

print(list1.show_elements(), list1.length(), list1.stackBottom())

list1.pop()

print(list1.show_elements(), list1.length())