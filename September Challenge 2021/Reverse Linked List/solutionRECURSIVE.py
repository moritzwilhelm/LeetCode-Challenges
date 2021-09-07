from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            if head.next is None:
                return head, head
            else:
                res, tail = reverse(head.next)
                head.next = None
                tail.next = head
                return res, head

        return reverse(head)[0] if head is not None else head
