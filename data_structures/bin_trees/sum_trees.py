def sum_tree(root):
    if root is None:
        return 0
    
    left_sum = sum_tree(root.left)
    right_sum = sum_tree(root.right)

    return root.val + left_sum + right_sum

def sum_tree_bfs(root):
    if root is None:
        return 0
    
    total_sum = 0

    stack = [ root ]
    while stack:
        curr = stack.pop()
        total_sum += curr.val

        for child in (curr.right, curr.left):
            if child is not None:
                stack.append(child)
    
    return total_sum

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

bin_tree = Node(2, Node(5, Node(100), Node(200)), Node(10, right=Node(1000)))

print(f"{sum_tree(root=bin_tree) = }")
print(f"{sum_tree_bfs(root=bin_tree) = }")
