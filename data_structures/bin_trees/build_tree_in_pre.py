from traverses import get_pre_order, get_in_order, _get_post_order


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def build_tree_in_pre(in_order, pre_order):
    """Return the root of the binary tree with the same in order and pre order traverses.
    >>> in_order = [ letter for letter in "bac" ]
    >>> pre_order = [ letter for letter in "abc" ]
    >>> bin_tree = build_tree_in_pre(in_order, pre_order)
    >>> #         a
    >>> #       /  \
    >>> #      b    c
    >>> get_in_order(root=bin_tree) == in_order
    True
    >>> get_pre_order(root=bin_tree) == pre_order
    True
    >>> in_order_2 = [ letter for letter in "dbeacf" ]
    >>> pre_order_2 = [ letter for letter in "abdecf" ]
    >>> bin_tree_2 = build_tree_in_pre(in_order_2, pre_order_2)
    >>> #         a
    >>> #       /  \
    >>> #      b    c
    >>> #    /  \     \
    >>> #  d     e     f
    >>> get_in_order(root=bin_tree_2) == in_order_2
    True
    >>> get_pre_order(root=bin_tree_2) == pre_order_2
    True
    
    """
    if len(in_order) == 0:
        return None
    
    root_val = pre_order[0]
    root = Node(root_val)
    mid = in_order.index(root_val)

    left_in_order = in_order[:mid]
    right_in_order = in_order[mid+1:]

    left_pre_order = pre_order[1: 1+len(left_in_order)]
    right_pre_order = pre_order[1+len(left_in_order):]

    root.left = build_tree_in_pre(left_in_order, left_pre_order)
    root.right = build_tree_in_pre(right_in_order, right_pre_order)

    return root

in_order   = [ letter for letter in "bac" ]
pre_order = [ letter for letter in "abc" ]

root = build_tree_in_pre(in_order, pre_order)

