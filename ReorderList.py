# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        if not head or not head.next:
            return head

        # First Step: Find middle of the linked list

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Second Step: Reverse the second half
        prev = None
        current = head

        while current:
            current.next, prev, current = prev, current, current.next
        slow.next = None

        # Third Step: Merge both

        first, second = head, prev

        while second:
            temp = first.next
            first.next = second
            first = second
            second = temp

