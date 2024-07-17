

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

# the right most node of the left subtree of a node is its inorder pre
def inorderPre(root):
    root = root.left 
    while(root.right != None):
        root = root.right
    return root

def deletionNode(root,value):

    if root is None:
        return None
    elif root.left is None and root.right is None:
        del root
        return None

    if value < root.data:
        root.left = deletionNode(root.left,value)
    elif value >  root.data:
        root.right = deletionNode(root.right, value)
    else:
        inprev = inorderPre(root)
        root.data = inprev.data
        root.left = deletionNode(root.left,inprev.data)
    return root 



InOrder(p)
print()
deletionNode(p,5)
InOrder(p)

