class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def get_middle(head):
    """Return the middle pointer in the linked list
    >>> head = Node(2, Node(3, Node(4)))
    >>> middle = get_middle(head)
    >>> middle.val
    3
    >>> head2 = Node('a', Node('b', Node('c', Node('d'))))
    >>> middle2 = get_middle(head2)
    >>> middle2.val
    'c'
    """
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next
    middle = slow
    return middle
#    head
#    a---->b---->c---->d---->e
#                slow                 
#                            fast          
#                middle
#                head2
#                reverse from here
#    a---->b---->c<---d<----e
#                            head2
# ===============================
#    head
#    a---->b---->c---->d---->e---->f
#                      slow                 
#                                          fast          
#                      middle
#                      head2
#                      reverse from here
#    a---->b---->c None<-d<----e<----f
#                                  head2
# 

def reverse(head):
    """Reverse the linked list and return the new head.
    >>> head = Node(1, Node(2, Node(3)))
    >>> reversed_head = reverse(head)
    >>> head.val
    1
    >>> reversed_head.val
    3
    """
    prev, curr = None, head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev


def match(head_1, head_2):
    """Return True if the two linked list's values match node by node,
    Otherwise return False.
    >>> match(head_1=Node(1, Node(2, Node(3))), head_2=Node(1, Node(2, Node(3))))
    True
    >>> match(head_1=Node(1, Node(2, Node(3))), head_2=Node(1, Node(4, Node(3))))
    False
    """
    curr_1, curr_2 = head_1, head_2
    while curr_1 and curr_2:
        if curr_1.val != curr_2.val:
            return False
        curr_1, curr_2 = curr_1.next, curr_2.next

    return True


def palindrome(head):
    """Return True if the linked list is a palindrome, otherwise return False.
    >>> palindrome(head=Node(1, Node(2, Node(3))))
    False
    >>> palindrome(head=Node(1, Node(2, Node(1))))
    True
    >>> palindrome(head=Node(1, Node(2, Node(3, Node(1)))))
    False
    >>> palindrome(head=Node(1, Node(2, Node(2, Node(1)))))
    True
    """
    middle = get_middle(head)

    head_2 = middle
    reversed_head_2 = reverse(head_2)

    return match(head, reversed_head_2)
