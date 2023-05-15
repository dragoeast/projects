from collections import deque
import trees

def tree_levels(root):
    if root is None:
        return [ [] ]
    
    levels = []
    queue = deque( [ ( root, 0 ) ] )
    while queue:
        curr, level = queue.popleft()
        if len(levels) <= level:
            levels.append( [ ] )
        levels[level].append(curr.val)

        for child in (curr.left, curr.right):
            if child is not None:
                queue.append( ( child, level+1 ) )
    
    return levels

for bin_tree in trees.tree_lst:
    print(f"{tree_levels(root=bin_tree) = }")
