def get_sum(head):
    total_sum = 0
    curr = head
    while curr is not None:
        total_sum += curr.val
        curr = curr.next
    
    return total_sum

def get_sum_recursive(head):
    if head is None:
        return 0
    sum_of_the_rest = get_sum_recursive(head.next)
    return head.val + sum_of_the_rest

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

linked_list = Node(2, Node(4, Node(6, Node(8, Node(10)))))
print(f"{get_sum(head=linked_list) = }")
print(f"{get_sum_recursive(head=linked_list) = }")
