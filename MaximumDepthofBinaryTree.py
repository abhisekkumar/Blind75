# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursive Approach
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root is None:
#             return 0
#         else:
#             leftRoot = self.maxDepth(root.left)
#             rightRoot = self.maxDepth(root.right)
#         return max(leftRoot, rightRoot) + 1

# Iterative Approach

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        queue = [(root, 1)]
        max_depth = 0

        while queue:
            node, depth = queue.pop(0)
            max_depth = max(max_depth, depth)

            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return max_depth

