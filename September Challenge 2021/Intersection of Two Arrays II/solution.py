from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        occurrences = defaultdict(int)
        for num in nums1:
            occurrences[num] += 1

        res = []
        for num in nums2:
            if occurrences[num] > 0:
                res.append(num)
                occurrences[num] -= 1

        return res
