class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def get_in_order(root):
    values = []
    _get_in_order(root, values)
    return values

def _get_in_order(root, values):
    if root is None:
        return
    _get_in_order(root.left, values)
    values.append(root.val)
    _get_in_order(root.right, values)

def get_post_order(root):
    values = []
    _get_post_order(root, values)
    return values

def _get_post_order(root, values):
    if root is None:
        return
    _get_post_order(root.left, values)
    _get_post_order(root.right, values)
    values.append(root.val)


def build_tree_in_post(in_order, post_order):
    """Return the root of the binary tree with the same in_order and post_order.
    >>> in_order = [ letter for letter in "bac" ]
    >>> post_order = [ letter for letter in "bca" ]
    >>> bin_tree = build_tree_in_post(in_order, post_order)
    >>> get_in_order(root=bin_tree) == in_order
    True
    >>> get_post_order(root=bin_tree) == post_order
    True
    """
    if len(in_order) == 0:
        return None
    
    root_val = post_order[-1]
    root = Node(root_val)
    mid = in_order.index(root_val)
    left_in_order = in_order[:mid]
    right_in_order = in_order[mid+1:]

    left_post_order = post_order[:len(left_in_order)]
    right_post_order = post_order[len(left_in_order):-1]

    root.left = build_tree_in_post(left_in_order, left_post_order)
    root.right = build_tree_in_post(right_in_order, right_post_order)

    return root



in_order   = [ letter for letter in "bac" ]
post_order = [ letter for letter in "bca" ]

root = build_tree_in_post(in_order, post_order)

print(f"{get_in_order(root) = }")
print(f"{get_post_order(root) = }")
