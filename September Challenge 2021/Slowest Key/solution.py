from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res_idx = 0
        longest_duration = releaseTimes[0]
        for i in range(1, len(releaseTimes)):
            # we already found max if remaining time delta is smaller than current max
            if releaseTimes[-1] - releaseTimes[i - 1] < longest_duration:
                break

            duration = releaseTimes[i] - releaseTimes[i - 1]
            if (duration, keysPressed[i]) > (longest_duration, keysPressed[res_idx]):
                res_idx = i
                longest_duration = duration

        return keysPressed[res_idx]
