def tolerant_teams(rivalries):
    """
    A rivalry is a pair of people who should not be placed on the same team.
    The function should return a boolean indicating whether or not it is possible 
    to separate people into two teams, without rivals being on the same team. 
    The two teams formed do not have to be the same size.
    """
    graph = _get_graph(edges = rivalries)

    return _can_color(graph)

def _get_graph(edges):
    """Return the directed adjecency list of the Graph created from the edges."""
    graph = {}

    for edge in edges:
        for node in edge:
            if node not in graph:
                graph[node] = []
        node_a, node_b = edge
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)

    return graph

def _can_color(graph):
    coloring = {}

    for node in graph:
        if node not in coloring:
            if _validate(graph, node, coloring, current_color=False) == False:
                return False
    
    return True

def _validate(graph, node, coloring, current_color):
    if node in coloring:
        return coloring[node] == current_color
    
    coloring[node] = current_color

    for neighbor in graph[node]:
        if neighbor is not None:
            if _validate(graph, neighbor, coloring, not current_color) == False:
                return False
    
    return True


rivalries_1 = [
  ('Joe', 'Chris'),
  ('Tom', 'Mark')
] # -> True

rivalries_2 = [
  ('Joe', 'Chris'),
  ('Tom', 'Mark'),
  ('Tom', 'Joe'),
  ('Chris', 'Tom')
] # -> False

rivalries_lst = [
    rivalries_1,
    rivalries_2,
]

for rivalries in rivalries_lst:
    print(f"{tolerant_teams(rivalries=rivalries) = }")
