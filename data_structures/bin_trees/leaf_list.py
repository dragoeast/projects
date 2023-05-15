import trees

is_leaf = lambda node: node.left is None and node.right is None

def leaf_list(root):
    leafs = []
    
    _leaf_list(root, leaf_lst=leafs)
    
    return leafs

def _leaf_list(root, leaf_lst):
    if root is None:
        return
    if is_leaf(root):
        leaf_lst.append(root.val)
    
    _leaf_list(root.left, leaf_lst)
    _leaf_list(root.right, leaf_lst)

for bin_tree in trees.tree_lst:
    print(f"{leaf_list(root=bin_tree) = }")
