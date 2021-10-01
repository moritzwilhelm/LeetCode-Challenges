from itertools import combinations
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        total = sum(nums)
        target = total // k
        if k == 1:
            return total == target
        if not total % k == 0 or max(nums) > target:
            return False

        for i in range(1, len(nums) - k + 2):
            for subset in set(combinations(nums, i)):
                if sum(subset) == target:
                    for num in subset:
                        nums.remove(num)
                    return self.canPartitionKSubsets(nums, k - 1)

        return False
