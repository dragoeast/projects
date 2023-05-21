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
    left_sorted_queue = deque(left_sorted)
    right_sorted_queue = deque(right_sorted)
    merged = []

    while left_sorted_queue and right_sorted_queue:
        if left_sorted_queue[0] < right_sorted_queue[0]:
            merged.append(left_sorted_queue.popleft())
        else:
            merged.append(right_sorted_queue.popleft())

    merged += left_sorted_queue
    merged += right_sorted_queue

    return merged

random_nums = sample(range(1, 100), k=10)
print(f"{random_nums = }")
print(f"{merge_sort(nums=random_nums) = }")
