from collections import deque

def bottom_right(root):
    if root is None:
        return None
    
    item = None

    queue = deque( [ root ] )
    while queue:
        curr = queue.popleft()
        item = curr.val

        for child in (curr.left, curr.right):
            if child is not None:
                queue.append(child)

    return item

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

binary_tree = Node('a', Node('b', Node('d'), Node('e', Node('g'))), Node('c', right=Node('f')))

#             a
#           /  \ 
#          b    c
#         / \    \
#        d   e    f
#           /
#          g

print(f"{bottom_right(root=binary_tree) = }")
print(f"{bottom_right(root=Node('a')) = }")
print(f"{bottom_right(root=None) = }")
