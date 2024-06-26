from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) <= 1:
        return len(nums)

    i = 0
    j = 1
    while j < len(nums):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
        else:
            j += 1

    return i + 1
