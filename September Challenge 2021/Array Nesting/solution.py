from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        longest_cycle = 0
        for i in range(len(nums)):
            if nums[i] >= 0:        # only consider non-visited indices
                cycle_length = 0
                while nums[i] >= 0:
                    tmp = nums[i]
                    nums[i] = -1    # mark index as visited
                    i = tmp
                    cycle_length += 1

                if cycle_length > longest_cycle:
                    longest_cycle = cycle_length
        return longest_cycle
