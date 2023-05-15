from collections import deque
import trees


def level_averages(root):
    averages = []
    levels = _tree_levels(root)

    for level in levels:
        averages.append( sum(level)/len(level) )

    return averages

def _tree_levels(root):
    if root is None:
        return []
    
    levels = []
    queue = deque( [ ( root, 0 ) ] )
    while queue:
        curr, level = queue.popleft()
        if len(levels) <= level:
            levels.append( [] )
        levels[level].append(curr.val)

        for child in (curr.left, curr.right):
            if child is not None:
                queue.append( ( child, level+1 ) )

    return levels


print(f"{_tree_levels(root=trees.bin_tree_numbers) = }")
print(f"{level_averages(root=trees.bin_tree_numbers) = }")
