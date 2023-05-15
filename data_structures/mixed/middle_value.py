def middle_value(head):
    if head is None:
        return None
    
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow, fast = slow.next, fast.next.next

    return slow.val

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

def linked_list_to_str(head):
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next

    return '->'.join( [ str(value) for value in values ] )

linked_list = Node(2, Node(3, Node(5, Node(3, Node(2)))))
linked_list_2 = Node(2, Node(3, Node(5, Node(7, Node(11, Node(13))))))

linked_lists = [
    None,
    Node('a'),
    Node('a', Node('b')),
    linked_list,
    linked_list_2,
]

for linked_list in linked_lists:
    print(f"{linked_list_to_str(head=linked_list)} ==> {middle_value(head=linked_list)}")
