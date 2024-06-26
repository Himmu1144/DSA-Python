
# This is just a very simple representation of a linked list do not use this code for notes

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
node4.next = None

print(node1.data, node2.data , node3.data)

# Traversing through the above linkedlist

def LinkedListTraversal(Node):
    while Node != None:
        print(f"Element : {Node.data}")
        Node = Node.next

LinkedListTraversal(node1)

# V-16 ----------------------------------------------------------------------------------------

# Case 1
def insert_at_first(head, data):
    ptr = Node(data)
    ptr.next = head
    return ptr

# Case 2 

def insert_in_between(head,data,index):
    ptr = Node(data)
    p = head
    i=0
    while(i!=index-1):
        p = p.next
        i += 1
    ptr.next = p.next
    p.next = ptr
    return head

# Case 3

def insert_at_end(head,data):
    ptr = Node(data)
    p = head
    while p.next != None:
        p = p.next
    p.next = ptr
    ptr.next = None
    return head

# Case 4

def insert_after_node(head,node,data):
    ptr = Node(data)

    ptr.next = node.next
    node.next = ptr

    return head

# node1 = insert_at_first(node1,10)
# node1 = insert_in_between(node1, 56, 2)
# node1 = insert_at_end(node1, 99)
# node1 = insert_after_node(node1,node2,21)


print('\n')
LinkedListTraversal(node1)