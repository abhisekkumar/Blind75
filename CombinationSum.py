# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def dfs(target, start, path):
            if target == 0:
                result.append(path)
                return

            for i in range(start, len(candidates)):

                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if target - candidates[i] < 0:
                    break
                dfs(target - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


import unittest


class TestCombinationSum(unittest.TestCase):
    def test_cases(self):
        # Test Case 1: Basic test case (Passing)
        self.assertEqual(Solution.combinationSum([2, 3, 6, 7], 7), [[2, 2, 3], [7]])
        print("Test Case 1 passed.")

        # Test Case 2: Single number multiple times (Passing)
        self.assertEqual(Solution.combinationSum([2], 4), [[2, 2]])
        print("Test Case 2 passed.")

        # Test Case 3: Incorrect target (Failing)
        # self.assertEqual(Solution.combinationSum([2, 3, 5], 7), [[2, 2, 2]])
        # print("Test Case 3 passed.")  # Will not be printed

        # Test Case 4: No solution, but incorrect expected result (Failing)
        # self.assertEqual(Solution.combinationSum([2, 3, 5], 1), [[1]])
        # print("Test Case 4 passed.")  # Will not be printed

        # Test Case 5: Empty list (Passing)
        self.assertEqual(Solution.combinationSum([], 1), [])
        print("Test Case 5 passed.")


if __name__ == '__main__':
    unittest.main()
