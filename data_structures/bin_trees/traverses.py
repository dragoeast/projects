class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def get_in_order(root):
    """Return the values in an in order traverse list.
    >>> bin_tree = Node('a', Node('b'), Node('c'))
    >>> get_in_order(root=bin_tree)
    ['b', 'a', 'c']
    >>> bin_tree_2 = Node(10, Node(5, Node(3), Node(8)), Node(20, right=Node(100)))
    >>> get_in_order(root=bin_tree_2)
    [3, 5, 8, 10, 20, 100]
    """
    values = []
    _get_in_order(root, values)
    return values

def _get_in_order(root, values):
    if root is None:
        return
    _get_in_order(root.left, values)
    values.append(root.val)
    _get_in_order(root.right, values)

def get_pre_order(root):
    """Return the values in an in order traverse list.
    >>> bin_tree = Node('a', Node('b'), Node('c'))
    >>> get_pre_order(root=bin_tree)
    ['a', 'b', 'c']
    >>> bin_tree_2 = Node(10, Node(5, Node(3), Node(8)), Node(20, right=Node(100)))
    >>> get_pre_order(root=bin_tree_2)
    [10, 5, 3, 8, 20, 100]
    """
    values = []
    _get_pre_order(root, values)
    return values

def _get_pre_order(root, values):
    if root is None:
        return
    values.append(root.val)
    _get_pre_order(root.left, values)
    _get_pre_order(root.right, values)

def get_post_order(root):
    """Return the values in an in order traverse list.
    >>> bin_tree = Node('a', Node('b'), Node('c'))
    >>> get_post_order(root=bin_tree)
    ['b', 'c', 'a']
    >>> bin_tree_2 = Node(10, Node(5, Node(3), Node(8)), Node(20, right=Node(100)))
    >>> get_post_order(root=bin_tree_2)
    [3, 8, 5, 100, 20, 10]
    """
    values = []
    _get_post_order(root, values)
    return values

def _get_post_order(root, values):
    if root is None:
        return
    _get_post_order(root.left, values)
    _get_post_order(root.right, values)
    values.append(root.val)
