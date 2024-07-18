class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right= None
from collections import deque
def BFS(root):
    if root == None:
        return 
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# Call DFS
BFS(root)  # Output: 1 2 4 5 3