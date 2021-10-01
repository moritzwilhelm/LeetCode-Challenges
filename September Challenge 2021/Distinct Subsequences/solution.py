from functools import lru_cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)

        @lru_cache(None)
        def count_subsequences(i, j):
            if j == m:
                return 1
            if i == n or n - i < m - j:
                return 0

            if s[i] == t[j]:
                return count_subsequences(i + 1, j) + count_subsequences(i + 1, j + 1)
            else:
                return count_subsequences(i + 1, j)

        return count_subsequences(0, 0)

