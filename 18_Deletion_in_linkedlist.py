
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

# V-18 ----------------------------------------------------------------------------------------

# Case 1

def delete_at_first(head):
    head = head.next
    return head


# Case 2 

def delete_in_between(head,index):
    p = head
    i=0
    while(i!=index-1):
        p = p.next
        i += 1
    q = p.next
    p.next = q.next
    q = None
    return head
    

# Case 3

def delete_at_end(head):

    p = head
    q = head.next
    while q.next != None:
        p = p.next 
        q = q.next

    p.next = None
    q = None

    return head
    

# Case 4

def delete_by_value(head,value):
    p = head 

    if p.data == value:
        return delete_at_first(head)
    
    q = None
    while p.data != value and p.next != None:
        q = p
        p = p.next

    if (p.data == value):
        q.next = p.next
        p = None

    return head

# node1 = delete_at_first(node1)
# node1 = delete_in_between(node1, 2)
# node1 = delete_at_end(node1)
# node1 =  delete_by_value(node1,12)

print('\n')
LinkedListTraversal(node1)