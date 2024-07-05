
# Binary Tree Traversal

"""
1. PreOerder Traversal -  root , left subtree , right subtree
2. PostOrder Traversal -  left subtree , right subtree , root 
3. InOrder Traversal - left subtree , root , right subtree 
"""

class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

p = Node(4) # root node
p1 = Node(1) 
p2 = Node(6) 
p3 = Node(5)  
p4 = Node(2) 

# linking root node with other nodes

p.left = p1
p.right = p2
p1.left = p3
p1.right = p4

# The Tree looks like this - 
"""            4
              / \
             1   6
            / \
           5   2 
"""

'''----------------------------------------------------------------------------------------------------'''

# PreOrder Traversal -

def preOrder(root):
    if root != None:
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)

preOrder(p)
print('')

'''----------------------------------------------------------------------------------------------------'''

# PostOrder Traversal -

def postOrder(root):
    if root != None:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")

postOrder(p)
print('')

'''----------------------------------------------------------------------------------------------------'''

# InOrder Traversal -

def InOrder(root):
    if root != None:
        InOrder(root.left)
        print(root.data, end=" ")
        InOrder(root.right)

InOrder(p)
