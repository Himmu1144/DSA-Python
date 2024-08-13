# Depth First Search (DFS) | Uses Stack DS (Last in First Out (LIFO))

visited = [0]*7

# Graph in Matrix form
a = [
        [0,1,1,1,0,0,0],
        [1,0,1,0,0,0,0],
        [1,1,0,1,1,0,0],
        [1,0,1,0,1,0,0],
        [0,0,1,1,0,1,1],
        [0,0,0,0,1,0,0], 
        [0,0,0,0,1,0,0] 
]

size = len(a)

def DFS(i):
    print(i,end="")
    visited[i] = 1
    for j in range(size):
        if a[i][j] == 1 and visited[j] == 0:
            DFS(j)

DFS(0)