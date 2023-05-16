# python -m doctest -v -v ./mixed/lefty_nodes.py

class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def _lefty_nodes(root, items, level):
    if root is None:
        return
    
    if len(items) <= level:
        items.append(root.val)
    
    _lefty_nodes(root.left, items, level+1)
    _lefty_nodes(root.right, items, level+1)


def lefty_nodes(root):
    """Return a list of the first elements from each level from the left.

    >>> bin_tree = Node('a', Node('b', Node('d'), Node('e', Node('g'))), Node('c', right=Node('f')))
    >>> lefty_nodes(root=bin_tree) 
    ['a', 'b', 'd', 'g']
    >>> #      a
    >>> #    /  \ 
    >>> #   b    c
    >>> #  / \    \
    >>> # d   e    f
    >>> #    /
    >>> #   g
    """
    lefty_values = []
    _lefty_nodes(root, items=lefty_values, level=0)

    return lefty_values
