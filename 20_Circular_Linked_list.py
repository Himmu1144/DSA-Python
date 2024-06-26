
# This is just a very simple representation of a circular linked list do not use this code for notes

class Node():
    def __init__(self, a_number):
        self.data = a_number
        self.next = None

node1 = Node(11)
node2 = Node(12)
node3 = Node(6)
node4 = Node(16)

# now linking all the three nodes 
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

# ------------------------------------------------------------

''' Converting the above singly linked list to a doubly linked list '''

# class Node():
#     def __init__(self, a_number):
#         self.data = a_number
#         self.prev = None
#         self.next = None

# node1 = Node(11)
# node2 = Node(12)
# node3 = Node(6)
# node4 = Node(16)

# # now linking all the three nodes 
# node1.prev = None
# node1.next = node2

# node2.prev = node1
# node2.next = node3

# node3.prev = node2
# node3.next = node4

# node4.prev = node3
# node4.next = None

# ------------------------------------------------------------

# print(node1.data, node2.data , node3.data)

# Traversing through the above linkedlist

def LinkedListTraversal(Node):
    head = Node
    while Node.next != head:
        print(f"Element : {Node.data}")
        Node = Node.next
        
    print(f"Element : {Node.data}")
    

LinkedListTraversal(node1)

# V-20 ----------------------------------------------------------------------------------------

# Case 1
def insert_at_first(head, data):
    ptr = Node(data)
    p = head.next
    while(p.next != head):
        p = p.next   
    p.next = ptr 
    ptr.next = head 
    head = ptr   
    return head


print('\n')
LinkedListTraversal(node1)