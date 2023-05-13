def get_values(head):
    value_lst = []
    curr = head
    while curr is not None:
        value_lst.append(curr.val)
        curr = curr.next

    return value_lst

class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

linked_list = Node(1, Node(3, Node(5, Node(7, Node(9)))))
print(f"{get_values(head=linked_list) = }")
