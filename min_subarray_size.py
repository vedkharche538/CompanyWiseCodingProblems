"""
Given an array of positive integers nums and a positive integer target,
return the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.
"""

from typing import List

# target = 7
# nums = [2, 3, 1, 2, 4, 3]
# target = 4
# nums = [1,4,4]
target = 11
nums = [1, 1, 1, 1, 1, 1, 1, 1]


def min_length_subarry(nums: List[int], target: int):
    left = 0
    subarray: List[int] = []
    count_length = float("inf")
    right = 0
    while right < len(nums):
        subarray.append(nums[right])
        while target <= sum(subarray):
            count_length = min(count_length, len(subarray))
            subarray.pop(0)
            left += 1
        right += 1

    return count_length if count_length != float("inf") else 0


result = min_length_subarry(nums, target)
print(result)
