from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        i = 0
        j = len(matrix[0])
        k = len(matrix)
        while True:
            if i >= j:
                break
            for idx in range(i, j):
                res.append(matrix[i][idx])
            if i + 1 >= k:
                break
            for idx in range(i + 1, k):
                res.append(matrix[idx][j - 1])
            if j - 2 <= i - 1:
                break
            for idx in range(j - 2, i - 1, -1):
                res.append(matrix[k - 1][idx])
            if k - 2 <= i:
                break
            for idx in range(k - 2, i, -1):
                res.append(matrix[idx][i])
            i += 1
            j -= 1
            k -= 1

        return res
