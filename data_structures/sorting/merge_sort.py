from random import sample

def merge_sort(nums):
    if len(nums) < 2:
        return nums
    
    middle = len(nums) // 2
    left_sorted  = merge_sort(nums[:middle])
    right_sorted = merge_sort(nums[middle:])

    return _merge(left_sorted, right_sorted)

def _merge(left_sorted, right_sorted):
    merged = []

    while left_sorted and right_sorted:
        if left_sorted[0] < right_sorted[0]:
            merged.append(left_sorted.pop(0))
        else:
            merged.append(right_sorted.pop(0))

    merged += left_sorted
    merged += right_sorted

    return merged

random_nums = sample(range(1, 100), k=10)
print(f"{random_nums = }")
print(f"{merge_sort(nums=random_nums) = }")
