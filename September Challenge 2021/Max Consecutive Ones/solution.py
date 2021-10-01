from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = current = 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                res = max(res, current)
                current = 0

        return max(res, current)
