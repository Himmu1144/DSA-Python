

class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

p = Node(5) # root node
p1 = Node(3) 
p2 = Node(6) 
p3 = Node(1)  
p4 = Node(4) 

# linking root node with other nodes

p.left = p1
p.right = p2
p1.left = p3
p1.right = p4

# The Tree looks like this - 
"""            5
              / \
             3   6
            / \
           1   4 
"""

# InOrder Traversal -

def InOrder(root):
    if root != None:
        InOrder(root.left)
        print(root.data, end=" ")
        InOrder(root.right)

# --------------------------------------------------------------------------------------------------------
# Insertion in a Binary Search Tree - Time Complexity - Average Case - O(logn), Worst Case (Skewed Tree) - O(n)

def insertBST(root,key):
    prev = root
    while(root is not None):
        prev = root
        if key == root.data:
            return 'Can Not Insert'
        elif key < root.data:
            root = root.left
        else:
            root = root.right

    if key < prev.data:
        prev.left = Node(key)
    else:
        prev.right = Node(key)

    return 'Successful Insertion'

InOrder(p)

insertBST(p,9)
insertBST(p,2)
print()
print(p.data,p.left.data,p.right.data,p.right.right.data,p.left.left.right.data)

InOrder(p)

