from string import ascii_letters


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        start = 0
        end = len(s) - 1
        res = ''

        while start < len(s):
            if s[start] not in ascii_letters:
                res += s[start]
                start += 1
            elif s[end] not in ascii_letters:
                end -= 1
            else:
                res += s[end]
                start += 1
                end -= 1

        return res
