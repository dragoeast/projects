def tree_value_count(root, target):
    if root is None:
        return 0
    
    match = 1 if root.val == target else 0
    
    left_count = tree_value_count(root.left, target)
    right_coutt = tree_value_count(root.right, target)

    return match + left_count + right_coutt

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

binary_tree = Node(2, Node(5, Node(4), Node(5)), Node(6, right=Node(5)))

print(f"{tree_value_count(root=binary_tree, target=5) = }")
