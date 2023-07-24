# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/921532009/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        # initialize both fast and slow pointers to point to the dummy node
        slow = fast = dummy

        # move the pointer n steps forward
        for i in range(n):
            fast = fast.next

        # move both pointers forward one node at a time until the fast pointer reaches the end of the list
        while fast.next:
            fast = fast.next
            slow = slow.next

        # at this point, the slow pointer is pointing to the node just before the nth node from the end
        # remove the nth node by setting the slow node's next pointer to the node after the nth node
        slow.next = slow.next.next

        # return the head of the modified linked list, which is the node after the dummy node
        return dummy.next
