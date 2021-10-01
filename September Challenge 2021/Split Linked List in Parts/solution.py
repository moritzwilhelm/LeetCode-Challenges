from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        current = head
        while current is not None:
            n += 1
            current = current.next
        part_size = n // k
        bigger_parts = n % k

        res = []
        for i in range(k):
            part = head
            for i in range(part_size + (i < bigger_parts) - 1):
                head = head.next
            if head is not None:
                head.next, head = None, head.next
            res.append(part)

        return res
