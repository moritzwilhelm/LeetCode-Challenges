from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """Slower but smaller solution using defaultdict"""
        res = 0

        arithmetic_subsequences = defaultdict(lambda: defaultdict(int))
        for i in range(len(nums)):
            for j in range(i):
                delta = nums[j] - nums[i]
                arithmetic_subsequences[i][delta] += arithmetic_subsequences[j][delta] + 1
                res += arithmetic_subsequences[j][delta]
        return res
