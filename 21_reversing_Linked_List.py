
""" Here's a simple program to reverse a linked list """

def reverse(l):

    if l.head == None:
        return # this means this linked list is empty 
    
    # now we are gonna use two pointers current_node and next_node and gonna slide them till the current node reaches the last node

    current_node = l.head
    prev_node = None 

    while current_node is not None:

        next_node = current_node.next

        # now we gotta swap - make next the previous node , move the previous and make it the current and the current becomes the next do this until the current node is none 
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    
    l.head = prev_node




# -------------------------------------------------------------------------------------------
# checking whether it works or not


# First create a node class

class Node():
    def __init__(self, a_number):
        self.data = a_number
        self.next = None

# Second create a LinkedList Class

class LinkedList():
    def __init__(self):
        self.head = None  # i think the LinkedList class does nothing but creates an object that contains the head
    
    # now we are gonna write a function to append a node in a linked list
    def append(self, value):
        if self.head == None:
            self.head = Node(value) # this means that this LL object doesn't have any head means it's empty rn
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    # now we are gonna write a function that travers through the linked list
    def show_elements(self):
        current_node = self.head
        while current_node is not None:
            print("Element : ",current_node.data)
            current_node = current_node.next

    # a function to show the length of the LL
    def length(self):
        current_node = self.head
        i = 0
        while current_node is not None:
            current_node = current_node.next
            i += 1
        return i
    
    # a function to get a node usnig index
    def get_element(self, index):
        current_node = self.head

        i = 0
        while current_node is not None:
            if i == index:
                return current_node.data
            current_node = current_node.next
            i += 1
        return None            
    
# now intialize it 

list1 = LinkedList()
list1.append(10)
list1.append(20)
list1.append(30)
list1.append(40)

list1.show_elements()

reverse(list1)

print('\n')
list1.show_elements()