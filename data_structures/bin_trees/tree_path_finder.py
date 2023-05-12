def get_path(root, target):
    if root is None:
        return None
    if root.val == target:
        return [ root.val ]
    
    left_path = get_path(root.left, target)
    if left_path:
        return [ root.val, *left_path ]
    right_path = get_path(root.right, target)
    if right_path:
        return [ root.val, *right_path ]
    
    return None

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

#      a
#    /   \
#   b     c
#  / \     \
# d   e     f

print(f"{get_path(root=a, target='e') = }") # -> [ 'a', 'b', 'e' ]
print(f"{get_path(root=a, target='f') = }") # -> [ 'a', 'c', 'f' ]
print(f"{get_path(root=a, target='b') = }") # -> [ 'a', 'b' ]
print(f"{get_path(root=a, target='c') = }") # -> [ 'a', 'c' ]
print(f"{get_path(root=a, target='a') = }") # -> [ 'a' ]
print(f"{get_path(root=a, target='x') = }") # -> None
print(f"{get_path(root=None, target='x') = }") # -> None
