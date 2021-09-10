from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """Solution avoiding the usage of defaultdict"""
        res = 0

        arithmetic_subsequences = {}
        for i in range(len(nums)):
            arithmetic_subsequences[i] = {}
            for j in range(i):
                delta = nums[j] - nums[i]
                if delta not in arithmetic_subsequences[i]:
                    arithmetic_subsequences[i][delta] = 1
                else:
                    arithmetic_subsequences[i][delta] += 1

                if delta in arithmetic_subsequences[j]:
                    arithmetic_subsequences[i][delta] += arithmetic_subsequences[j][delta]
                    res += arithmetic_subsequences[j][delta]
        return res
