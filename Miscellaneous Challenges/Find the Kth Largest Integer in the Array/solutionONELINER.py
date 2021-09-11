from typing import List


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        return sorted(nums, reverse=True, key=lambda x: int(x))[k - 1]
