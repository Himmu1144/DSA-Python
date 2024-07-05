
class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

p = Node(2) # root node
p1 = Node(1) # second node 
p2 = Node(4) # third node 

# linking root node with p1 and p2
p.left = p1
p.right = p2
