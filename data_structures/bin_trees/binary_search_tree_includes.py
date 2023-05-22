class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst_includes(root, target):
    """Return True if the Binary Search Tree includes the value, target.
    Otherwise return False.
    >>> bst = Node(10, Node(5, Node(2), Node(8)), Node(20, right=Node(50)))
    >>> bst_includes(root=bst, target=2)
    True
    >>> bst_includes(root=bst, target=50)
    True
    >>> bst_includes(root=bst, target=3)
    False
    """
    if root is None:
        return False
    if root.val == target:
        return True
    
    if target < root.val:
        return bst_includes(root.left, target)
    else:
        return bst_includes(root.right, target)
