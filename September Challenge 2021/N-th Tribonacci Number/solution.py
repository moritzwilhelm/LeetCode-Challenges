class Solution:
    def tribonacci(self, n: int) -> int:
        trib = [0, 1, 1] + [0 for _ in range(n - 2)]

        for i in range(3, n + 1):
            trib[i] = trib[i - 3] + trib[i - 2] + trib[i - 1]

        return trib[n]
