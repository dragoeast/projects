def topological_order(graph):
    """Return one of the topological order of the DAG,
       represented by the adjacency list, graph.
    >>> graph = {'a': ['b'], 'b': ['c'], 'c': []}
    >>> topological_order(graph)
    ['a', 'b', 'c']
    """
    orders = []

    num_parents = get_num_parents(graph)
    ready = [ node for node in num_parents if num_parents[node] == 0 ]
    while ready:
        curr = ready.pop()
        orders.append(curr)

        for neighbor in graph[curr]:
            num_parents[neighbor] -= 1
            if num_parents[neighbor] == 0:
                ready.append(neighbor)
    
    return orders

def get_num_parents(graph):
    """Return the num_parents dictionary where
    key: the node
    value: the number of parents the node has.
    >>> graph = {'a': ['b', 'c'], 'b': ['c'], 'c': ['d'], 'd': []}
    >>> get_num_parents(graph)
    {'a': 0, 'b': 1, 'c': 2, 'd': 1}
     """
    num_parents = {}

    for node in graph:
        num_parents[node] = 0
    
    for node in graph:
        for neighbor in graph[node]:
            num_parents[neighbor] += 1

    return num_parents

def testing():
    assert topological_order({
  "a": ["f"],
  "b": ["d"],
  "c": ["a", "f"],
  "d": ["e"],
  "e": [],
  "f": ["b", "e"],
}) == ['c', 'a', 'f', 'b', 'd', 'e'], "should be ['c', 'a', 'f', 'b', 'd', 'e']"

    assert topological_order({
  "h": ["l", "m"],
  "i": ["k"],
  "j": ["k", "i"],
  "k": ["h", "m"],
  "l": ["m"],
  "m": [],
}) == ['j', 'i', 'k', 'h', 'l', 'm'], "should be ['j', 'i', 'k', 'h', 'l', 'm']"
    
if __name__ == "__main__":
    testing()
    print("Everything passed")
