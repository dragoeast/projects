def string_search(grid, s):
    """Return True if the string s is in the grid.
    False otherwise.
    >>> grid = [\
    [ letter for letter in "ahcde" ],\
    [ letter for letter in "aelle" ],\
    [ letter for letter in "abcoe" ],\
    ]
    >>> string_search(grid, s='hello')
    True
    >>> string_search(grid, s='mike')
    False
    """
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid, row, col, s, i=0, visited=set()) == True:
                return True
    
    return False

def explore(grid, row, col, s, i, visited):
    """Return True if the string s found in the grid.
    Using Depth First Search for the implementation.
    """
    if not inbound(grid, row, col):
        return False
    pos = (row, col)
    if pos in visited:
        return False
    if s[i] != grid[row][col]:
        return False
    if i == len(s)-1 and s[i] == grid[row][col]:
        return True
    
    visited.add( pos )

    return explore(grid, row-1, col, s, i+1, visited) or\
           explore(grid, row+1, col, s, i+1, visited) or\
           explore(grid, row, col-1, s, i+1, visited) or\
           explore(grid, row, col+1, s, i+1, visited)

    return False

def inbound(grid, row, col):
    """Return True if the row, col position is a valid index in the grid.
    Otherwise return False.
    >>> grid = [\
        [1, 2, 3],\
        [1, 2, 3],\
        ]
    >>> inbound(grid, row=0, col=0)
    True
    >>> inbound(grid, row=0, col=2)
    True
    >>> inbound(grid, row=1, col=3)
    False
    >>> inbound(grid, row=-1, col=1)
    False
    """
    row_inbound = row in range(len(grid))
    col_inbound = col in range(len(grid[0]))

    return row_inbound and col_inbound

def testing():
    grid = [
    ['e', 'y', 'h', 'i', 'j'],
    ['q', 'x', 'e', 'r', 'p'],
    ['r', 'o', 'l', 'l', 'n'],
    ['p', 'r', 'x', 'o', 'h'],
    ['a', 'a', 'm', 'c', 'm']
    ]
    result = True
    assert string_search(grid, 'hello') == result, f"should be {result}"
    assert string_search(grid, 'proxy') == result, f"should be {result}"

    result = False
    assert string_search(grid, 'rolling') == result, f"should be {result}"
    assert string_search(grid, 'zoo') == result, f"should be {result}"

    grid = [
    ['q', 'w', 'h', 'i', 'j'],
    ['q', 'e', 'r', 'o', 'p'],
    ['h', 'y', 't', 'x', 'z'],
    ['k', 'o', 'm', 'o', 'p'],
    ]
    result = True
    assert string_search(grid, 'qwerty') == result, f"should be {result}"

    grid = [ 
    [ 'f', 'd', 'i', 'e', 'l', 'u', 'j', 't', 'q', 'v', 'o', 'p' ], 
    [ 'o', 'p', 'b', 'e', 'm', 'w', 'm', 'l', 'h', 'j', 's', 'v' ], 
    [ 'g', 'b', 's', 'm', 'i', 'w', 'w', 'h', 'l', 'm', 'l', 'n' ], 
    [ 'a', 'l', 's', 'k', 'p', 'c', 't', 'u', 'v', 'b', 'c', 'm' ], 
    [ 'm', 't', 'c', 'k', 'e', 'n', 'r', 'b', 'a', 'z', 'l', 'c' ], 
    [ 'q', 'm', 'a', 'p', 'a', 'p', 'i', 'i', 'u', 't', 'z', 'z' ], 
    [ 'd', 'u', 'z', 'o', 'e', 'r', 'a', 't', 't', 'c', 'q', 'k' ], 
    [ 'f', 'u', 'z', 'g', 'c', 'i', 'k', 'v', 'o', 'f', 's', 'w' ], 
    [ 'p', 'h', 'u', 'i', 'k', 'c', 'v', 'v', 'h', 'q', 'v', 'i' ], 
    [ 'l', 'q', 'w', 'f', 'y', 'g', 'w', 'f', 'a', 'u', 'x', 'q' ] 
    ]
    result = True
    assert string_search(grid, 'paprika') == True, f"should be {result}"

    grid = [
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'x' ],
        [ 's', 's', 's', 's', 's', 's', 's', 's', 's', 'x', 'h' ],
    ]
    result = False
    assert string_search(grid, 'ssssssssssh') == False, f"should be {result}"

    grid = [
    ['c', 'b', 'a'],
    ['d', 'x', 'x'],
    ['x', 'x', 'x'],
    ]
    result = True
    assert string_search(grid, 'abcd') == True, f"should be {result}"    


if __name__ == "__main__":
    testing()
    print("Everything passed")
