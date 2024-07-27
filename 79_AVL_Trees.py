
""" 
AVL Tress

1. AVL Trees are height balanced binary search trees.
2. BF (Balanced Factor) =  Height of Right Subtree - Height of Left Subtree
3. |BF| <= 1

left rotate wrt a node - node is moved toward the left
right rotate wrt a node - node is moved toward the right
-------------------------------------------------------------------

Balancing of AVL Tree after insertion

1. For a Left-Left Insertion       - Right rotate once WRT first imbalanced node
2. For a Right-Right Insertion     - Left rotate once WRT first imbalanced node

3. For a Left-Right Insertion      - Left rotate once wrt child of FIB and then right rotate once wrt FIB
4. For a Right-Left Insertion      - Right rotate once wrt child of FIB and then left rotate once wrt FIB

"""

class Node():
    def __init__(self,data):
        self.key = data
        self.left = None
        self.right = None
        self.height = 1

def getBalancedFactor(node):
    if node == None:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def getHeight(node):
    if node == None:
        return 0
    return node.height

def rightRotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = max(getHeight(y.left), getHeight(y.right)) + 1
    x.height = max(getHeight(x.left), getHeight(x.right)) + 1

    return x

def leftRotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    y.height = max(getHeight(y.left), getHeight(y.right)) + 1
    x.height = max(getHeight(x.left), getHeight(x.right)) + 1

    return y

def preOrder(root):
    if root != None:
        print(root.key, end=" ")
        preOrder(root.left)
        preOrder(root.right)

def InOrder(root):
    if root != None:
        InOrder(root.left)
        print(root.key, end=" ")
        InOrder(root.right)

def insertAVL(node,key):

    if node == None:
        return Node(key)
    
    if key < node.key:
        node.left = insertAVL(node.left,key)
    elif key > node.key:
        node.right = insertAVL(node.right, key)
    else:
        return node

    node.height = 1 + max(getHeight(node.left) , getHeight(node.right))
    bf = getBalancedFactor(node)

    # Left Left 

    if(bf > 1 and key < node.left.key):
        return rightRotate(node)

    # Right Right 

    if(bf < -1 and key > node.right.key):
        return leftRotate(node)

    # Left Right 

    if(bf > 1 and key > node.left.key):
        node.left = leftRotate(node.left)
        return rightRotate(node)

    # Right Left 

    if(bf < -1 and key < node.right.key):
        node.right = rightRotate(node.right)
        return leftRotate(node)

    return node


root = None

root = insertAVL(root, 1)
root = insertAVL(root, 2)
root = insertAVL(root, 4)
root = insertAVL(root, 5)
root = insertAVL(root, 6)
root = insertAVL(root, 3)

preOrder(root)
print('')
InOrder(root)
print()

print(root.key, root.left.key,root.right.key)
