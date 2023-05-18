class Node:
    def __init__(self, val, children=[]) -> None:
        self.val = val
        self.children = children[:]


class Tree:
    def __init__(self) -> None:
        self.root = None
    

# def longest_path(file_system: str) -> int:
#     """Suppose we represent our file system as a string.
#     For example, the string "user\n\tpictures\n\tdocuments\n\t\tnotes.txt" represents:
#     user
#         pictures
#         documents
#             notes.txt
#     We want to find the longest (as determined by the number of characters)
#     absolute path to a file within our system. 
#     """
#     root = parse_string_to_tree(fs=file_system)

#     return highest_sum_from_root_to_leaf(root)

def get_triplets(file_names: list[str]) -> tuple[str,int,int]:
    triplets = []

    for file_name in file_names:
        indentation = 0
        i = 0
        while file_name[i] == '\t':
            indentation += 1
            i += 1
        triplet = (file_name[i:], indentation, len(file_name[i:]))
        triplets.append(triplet)
    return triplets

def parse_string_to_tree(fs: str) -> Node:
    """Parse the string 'fs' into a tree where each nodes represent 
    the name of the folder/file name, the indentation/level,
    and the lenght of the folder/file name.
    Return the root of the tree.
    >>> fs = "user\n\tchris\n\tmark\n\t\ttoys.txt"
    >>> parse_string_to_tree(fs)
    >>> #       ( 'user', 0, 4 )
    >>> #             /  \ 
    >>> #            /    \ 
    >>> #           /      \ 
    >>> # ( 'chris', 1, 5 ) ( 'mark', 1, 4 ) 
    >>> #                        /   
    >>> #                       /     
    >>> #                      /       
    >>> #             ( 'toys.txt', 2, 4 )
    """
    file_names = fs.split('\n')
    print(file_names)
    triplets = get_triplets(file_names)
    print(triplets)

fs = "user\n\tchris\n\tmark\n\t\ttoys.txt"
parse_string_to_tree(fs)
