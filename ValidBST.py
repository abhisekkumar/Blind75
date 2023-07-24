# https://leetcode.com/problems/validate-binary-search-tree/submissions/972337204/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(node, left, right):

            if not node:
                return True

            if not (right > node.val > left):
                return False

            return self.isValidBST(node.left, left, node.val) and self.isValidBST(node.right, node.val, right)

        return root, float("-inf"), float("inf")
