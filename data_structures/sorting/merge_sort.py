from collections import deque
from random import sample

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    
    middle = len(nums) // 2
    left_sorted  = merge_sort(nums[:middle])
    right_sorted = merge_sort(nums[middle:])

    return _merge(left_sorted, right_sorted)

def _merge(left_sorted, right_sorted):
    queue_1 = deque(left_sorted)
    queue_2 = deque(right_sorted)
    merged = []

    while queue_1 and queue_2:
        if queue_1[0] < queue_2[0]:
            merged.append(queue_1.popleft())
        else:
            merged.append(queue_2.popleft())

    merged += queue_1
    merged += queue_2

    return merged

random_nums = sample(range(1, 100), k=10)
print(f"{random_nums = }")
print(f"{merge_sort(nums=random_nums) = }")
