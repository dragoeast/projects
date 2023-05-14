class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

empty_tree = None
single_tree = Node('a')
bin_tree = Node('a', Node('b', Node('d'), Node('e')), Node('c', right=Node('f')))
#             a
#           /  \ 
#          b    c
#         / \    \
#        d   e    f
#           /
#          g


bin_tree_2 = Node('a', Node('b', Node('d'), Node('e', Node('g'))), Node('c', right=Node('f')))
#             a
#           /  \ 
#          b    c
#         / \    \
#        d   e    f
#           /
#          g
