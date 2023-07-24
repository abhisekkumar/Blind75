# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times
from typing import List


# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         sorted(nums)
#         min(nums)


def findMin(nums: List[int]) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1

        else:
            right = mid
    return nums[left]


class Solution:
    pass


