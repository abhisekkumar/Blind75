# https://leetcode.com/problems/invert-binary-tree/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Recursive Approach
        if root is None:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Iterative Approach

        if root is None:
            return None

        stack = [root]

        while stack:
            node.stack(pop)

            node.left, node.right = node.right, node.left

            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

        return root

