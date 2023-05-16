def _validate(graph, node, coloring, current_color):
    """Helper function for the can_color function.
    Return True if the current connected component can be colored with two colors,
    Otherwise return False.
    """
    if node in coloring:
        return coloring[node] == current_color
    
    coloring[node] = current_color

    for neighbor in graph[node]:
        if neighbor is not None:
            if _validate(graph, neighbor, coloring, not current_color) == False:
                return False
    return True


def can_color(graph):
    """Return True if the graph can be colored with two colors in such a way that all adjecent nodes are different colors
    Return False otherwise.
    """
    coloring = {}
    for node in graph:
        if node not in coloring:
            if _validate(graph, node, coloring, current_color=False) == False:
                return False
    
    return True

graph = {
  "x": ["y"],
  "y": ["x","z"],  #  x------y------z
  "z": ["y"]       # Blue   Red   Blue
} # -> True

print(f"{can_color(graph) = }")

