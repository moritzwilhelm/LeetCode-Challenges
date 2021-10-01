from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 1
        start = 0

        def cmp(a, b):
            return (a > b) - (a < b)

        for i in range(1, len(arr)):
            c = cmp(arr[i - 1], arr[i])
            if c == 0:
                start = i
            elif i == len(arr) - 1 or c * cmp(arr[i], arr[i + 1]) != -1:
                res = max(res, i - start + 1)
                start = i
        return res
