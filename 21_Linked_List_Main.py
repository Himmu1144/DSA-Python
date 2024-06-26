
# Linked List Main

class Node():
    def __init__(self, a_number):
        self.data = a_number
        self.next = None

node1 = Node(2)
node2 = Node(6)
node3 = Node(8)

# now we are going to define a class for the linked list

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


# Here we are manually creating a linked list 

# list1 = LinkedList()
# list1.head = node1
# list1.head.next = node2
# list1.head.next.next = node3

# print(list1.head.data, list1.head.next.data, list1.head.next.next.data)

# Here we are creating a LL using append

# list2 = LinkedList()
# list2.append(2)
# list2.append(7)
# list2.append(8)

# list2.show_elements()
# print('The length of list2 is - ', list2.length())


#---------------------------------------------------------------------------------------------------------------

""" We are going to use this as the Linked List base template code  """

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
print("Length - ", list1.length())
print("Element/Node value at postion 3 - ",list1.get_element(3))
