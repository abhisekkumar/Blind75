# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [1] * len(nums)

        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]

        product = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * product
            product = product * nums[i]

        return output

