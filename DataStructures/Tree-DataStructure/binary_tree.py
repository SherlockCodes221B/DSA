class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.data == key:
            return root
        elif root.data < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ------>')
        inorder(root.right)

def preorder(root):
    if root:
        print(root.data, end=' ------>')
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=' ------>')


root_value = int(input("Enter the root node: "))
root = Node(root_value)
number_of_elements = int(input("Enter the total number of elements in the tree: "))
print("Enter the elements: ")
for _ in range(number_of_elements):
    element = int(input())
    root = insert(root, element)

print("Inorder traversal: ")
inorder(root)
print("\nPreorder traversal: ")
preorder(root)
print("\nPostorder traversal: ")
postorder(root)


