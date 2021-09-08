from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = ''
        shift = 0

        for i in range(len(shifts) - 1, -1, -1):
            shift += shifts[i]
            shift %= 26
            val = ord(s[i]) + shift
            res += chr(val if val <= 122 else val - 26)

        return res[::-1]
