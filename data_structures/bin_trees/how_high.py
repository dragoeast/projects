is_leaf = lambda node: node.left is None and node.right is None 

def how_high(root):
    if root is None:
        return -1
    if is_leaf(root):
        return 0
    
    left_height = how_high(root.left)
    right_height = how_high(root.right)

    return 1 + max(left_height, right_height)

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

binary_tree = Node('a', Node('b', Node('d'), Node('e', Node('g'))), Node('c', right=Node('f')))

print(f"{how_high(root=binary_tree) = }")
print(f"{how_high(root=Node('a')) = }")
print(f"{how_high(root=None) = }")
