import trees

is_leaf = lambda node: node.left is None and node.right is None

def all_tree_path(root):
    if root is None:
        return []
    if is_leaf(root):
        return [ root.val ]

    paths = []
    left_paths = all_tree_path(root.left)
    right_paths = all_tree_path(root.right)
    for path in (*left_paths, *right_paths):
        if path is not None:
            paths.append( [root.val, *path] )
    
    return paths

print(f"{all_tree_path(root=trees.bin_tree) = }")
print(f"{all_tree_path(root=trees.bin_tree_2) = }")
