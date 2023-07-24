# https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # if p is None and q is None:
        #     return True
        # elif p is None or q is None:
        #     return False
        # elif p.val != q.val:
        #     return False
        # else:
        #     return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()

            if node1 is None and node2 is None:
                return True
            elif None in [node1, node2]:
                return False
            elif node1.val != node2.val:
                return False

            if (node1.right is not None and node2.right is None) or (node1.right is None and node2.right is not None):
                return False
            if node1.right is not None and node2.right is not None:
                stack.append((node1.right, node2.right))

            # Check the existence of left children before pushing to stack
            if (node1.left is not None and node2.left is None) or (node1.left is None and node2.left is not None):
                return False
            if node1.left is not None and node2.left is not None:
                stack.append((node1.left, node2.left))

        return True
