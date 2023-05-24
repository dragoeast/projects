class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def find_middle_element(head):
    """Return the value of the middle element in a linked list.
    >>> odd_head = Node('a', Node('b', Node('c', Node('d', Node('e')))))
    >>> find_middle_element(head=odd_head)
    'c'
    >>> even_head = Node('a', Node('b', Node('c', Node('d', Node('e', Node('f'))))))
    >>> find_middle_element(head=even_head)
    'd'
    """
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
    
    return slow.val
