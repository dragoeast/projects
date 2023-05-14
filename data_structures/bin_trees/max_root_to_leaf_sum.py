is_leaf = lambda node: node.left is None and node.right is None

def max_path_sum(root):
    if root is None:
        return float('-inf')
    if is_leaf(root):
        return root.val
    
    left_path_sum = max_path_sum(root.left)
    right_path_sum = max_path_sum(root.right)

    return root.val + max(left_path_sum, right_path_sum)

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

right_subtree = Node(10, Node(20), Node(25))
linked_list = Node(2, Node(3, right=right_subtree), Node(5, right=Node(30)))

#              2
#           /   \
#          3     5
#           \     \
#           10     30
#          /  \   
#        20   25

print(f"{max_path_sum(root=linked_list) = }")
