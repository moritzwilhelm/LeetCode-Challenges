from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        strings = [""]
        res = 0

        for s in arr:
            # skip string if it contains duplicate chars
            if len(s) != len(set(s)):
                continue
            for other in strings:
                current = other + s
                if len(current) == len(set(current)):
                    strings.append(current)
                    res = max(res, len(current))

                    # early exit if maximum is reached
                    if res == 26:
                        return res

        return res
