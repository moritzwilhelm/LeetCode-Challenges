import heapq
from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """Finds kth largest number in nums by using a (small) min heap"""
        nums = [int(num) for num in nums]  # parse numbers

        if k == 1:
            return str(max(nums))
        if k == len(nums):
            return str(min(nums))

        res = min(nums[:k])

        # build priority queue of elements bigger than current res
        pq = nums[:k]
        heapq.heapify(pq)
        heapq.heappop(pq)  # remove res

        for i in range(k, len(nums)):
            if nums[i] > res:
                res = heapq.heappushpop(pq, nums[i])

        return str(res)
