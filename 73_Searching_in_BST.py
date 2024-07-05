

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

# Searching in BST - Time complexity - best case = O(logn) , worst case = O(n)

def search(root,key):

    if root is None:
        return None
    
    if key == root.data:
        return root
    elif key < root.data:
        return search(root.left , key)
    else:
        return search(root.right, key)
    
key_node = search(p,3)

if key_node is not None:
    print(key_node.data,key_node.left.data,key_node.right.data)
else:
    print('key not found')
    
# ----------------------------------------------------------------------------------------------------

# Iterative Search in BST

def iterSearch(root,key):
    while(root is not None):
        if key == root.data:
            return root
        elif key < root.data:
            root = root.left
        else:
            root = root.right
    return None 

key_node = iterSearch(p,3)

if key_node is not None:
    print(key_node.data,key_node.left.data,key_node.right.data)
else:
    print('key not found')