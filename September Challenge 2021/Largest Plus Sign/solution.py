from typing import List


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        if len(mines) == n * n:
            return 0

        if len(mines) > n * n - 4:
            return 1

        forbidden = {(x, y) for x, y in mines}

        res = 0
        order = [[0] * n for _ in range(n)]

        for i in range(n):
            # 1st direction
            count = 0
            for j in range(n):
                count = count + 1 if (i, j) not in forbidden else 0
                order[i][j] = count

            # 2nd direction
            count = 0
            for j in range(n - 1, -1, -1):
                count = count + 1 if (i, j) not in forbidden else 0
                if count < order[i][j]:
                    order[i][j] = count

        for j in range(n):
            # 3rd direction
            count = 0
            for i in range(n):
                count = count + 1 if (i, j) not in forbidden else 0
                if count < order[i][j]:
                    order[i][j] = count

            # 4th direction
            count = 0
            for i in range(n - 1, -1, -1):
                count = count + 1 if (i, j) not in forbidden else 0
                if count < order[i][j]:
                    order[i][j] = count
                # update result
                if order[i][j] > res:
                    res = order[i][j]

        return res
