class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

testing_lst = [
    None,
    Node(2), Node('a'),
    Node(2, Node(3)), Node('a', Node('b')),
    Node(2, Node(3, Node(5))), Node('a', Node('b', Node('c'))),
]

cycle_1 = Node('a', Node('b', Node('c', Node('d'))))
cycle_1.next.next.next.next = cycle_1.next.next

testing_with_cycle = [
    cycle_1,
]