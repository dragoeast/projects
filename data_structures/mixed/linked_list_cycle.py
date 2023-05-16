from ...data_structures.linked_list.linked_list_testing import testing_lst


# def has_cycle(head):
#     slow, fast = head, head.next
#     while fast is not None and fast.next is None:
#         if slow == fast:
#             return True
#         slow, fast = slow.next, fast.next.next

#     return False

# def linked_list_to_str(head):
#     values = []
#     curr = head
#     while curr:
#         values.append(curr.val)
#         curr = curr.next

#     return '->'.join( [ str(value) for value in values ] )

# for linked_list in testing_lst:
#     print(f"{linked_list_to_str(linked_list)}===> {has_cycle(head=linked_list)}")
