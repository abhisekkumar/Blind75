# https://leetcode.com/problems/3sum/
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = val + nums[left] + nums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    result.append([val, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return result

    def test(self):
        test_cases = [
            ([-1, 0, 1], [[-1, 0, 1]]),
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([1, 2, 3, 4, 5], []),
            ([-1, 0, 1, 2, -1, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([1], [])
        ]

        for i, test_case in enumerate(test_cases):
            result = self.threeSum(test_case[0])
            if result != test_case[1]:
                print(f"Test case {i} failed: expected {test_case[1]}, but got {result}")
            else:
                print(f"Test case {i} succeeded")


s = Solution()
s.test()


#Another Solution:

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplet = []

        i = 0

        for i in range(len(nums) - 2):




            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = [i] + nums[left] + nums[right]
                if triplet < 0:
                    left += 1
                elif triplet > 0:
                    right -= 1

                else:
                    triplet.append([i, nums[left], nums[right]])








