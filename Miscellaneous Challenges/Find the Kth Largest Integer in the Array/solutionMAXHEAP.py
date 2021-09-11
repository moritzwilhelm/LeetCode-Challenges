import heapq
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """Finds kth largest number in nums by transforming nums into a (big) max heap"""
        nums = [-int(num) for num in nums]  # parse numbers

        if k == 1:
            return str(-min(nums))
        if k == len(nums):
            return str(-max(nums))

        # build max heap & pop root k times
        heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)

        return str(-res)
