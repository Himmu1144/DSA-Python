
# Binary Search Tree - 

"""
Properties - 

1. All the nodes of left subtree are lesser
2. All the nodes of right subtree are greater
3. No duplicate values
4. In a BST left & right subtrees are also BST's
5. InOrder Traversal of BST gives an ascending sorted array

"""

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

def InOrder(root):
    if root != None:
        InOrder(root.left)
        print(root.data, end=" ")
        InOrder(root.right)

def isBST(root,prev=None):

    if root != None:
        
        if not isBST(root.left, prev):
            return False
        
        if prev is not None and root.data <= prev.data:
            return False
            
        prev = root

        return isBST(root.right,prev)
    
    else:
        return True
        


InOrder(p)

print(isBST(p))
