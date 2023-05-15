def palindrome(head):
    value_lst = _get_values(head)

    return _palindrome(lst=value_lst)

def _get_values(head):
    value_lst = []

    curr = head
    while curr:
        value_lst.append(curr.val)
        curr = curr.next

    return value_lst

def _palindrome(lst):
    left, right = 0, len(lst)-1
    while left < right:
        if lst[left] != lst[right]:
            return False
        left, right = left+1, right-1
    
    return True



class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def add(self, value):
        prev, curr = None, self.head
        while curr:
            prev = curr
            curr = curr.next
        if self.head is None:
            self.head = Node(value)
        else:
            prev.next = Node(value)
    def __repr__(self) -> str:
        values = []
        curr = self.head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return '->'.join(values)

linked_list = LinkedList()
for ch in "abcde":
    linked_list.add(ch)


print(f"{linked_list = }")

print(f"{palindrome(head=linked_list) = }")
