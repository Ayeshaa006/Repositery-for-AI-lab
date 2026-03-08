#task 5
#1.DFS with stack and node
class node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
def dfs_with_stack(start_node):
    visited = set()
    stack = [start_node]
    result = []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            result.append(current.value)
            for neighbor in reversed(current.neighbors):
                if neighbor not in visited:
                    stack.append(neighbor)
    return result
#example graph
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_a.neighbors = [node_b, node_c]
node_b.neighbors = [node_d]
node_c.neighbors = [node_d]
print("DFS Traversal:", dfs_with_stack(node_a))




#2.tree traversals
class treenode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def print_preorder(root):
    if root:
        print(root.val, end="")
        print_preorder(root.left)
        print_preorder(root.right)
def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.val, end="")
        print_inorder(root.right)
def print_postorder(root):
    if root:
        print_postorder(root.left)
        print_postorder(root.right)
        print(root.val, end="")
#constructing a sample tree
#           1
#          / \
#         2   3
root = treenode(1)
root.left = treenode(2)
root.right = treenode(3)
print("preorder: ")
print_preorder(root)
print("\ninorder: ")
print_inorder(root)
print("\npostorder: ")
print_postorder(root)
