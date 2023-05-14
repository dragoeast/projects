def tree_value_count_iterative(root, target):
    if root is None:
        return 0
    
    counter = 0
    stack = [ root ]
    while stack:
        curr = stack.pop()
        if curr.val == target:
            counter += 1
        
        for child in (curr.right, curr.left):
            if child is not None:
                stack.append(child)

    return counter

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
print(f"{tree_value_count_iterative(root=binary_tree, target=5) = }")
