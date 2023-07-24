# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHash = {}

        for i, n in enumerate(nums):
            diff = target - i

            if diff in prevHash:
                return [prevHash[diff], i]
            prevHash = [i]
