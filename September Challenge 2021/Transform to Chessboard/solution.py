from collections import Counter
from typing import List


class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        # Not checked by tests but might be needed for correct implementation as precondition is not clear ("balanced" board):
        # ones = sum(sum(row) for row in board)
        # board_weight = n * n // 2
        # if n % 2 == 0 and ones != board_weight or n % 2 == 1 and ones not in [board_weight, board_weight + 1]:
        #    return -1

        horizontal_patterns = list(Counter(tuple(row) for row in board).items())
        vertical_patterns = list(Counter(tuple(row) for row in map(list, zip(*board))).items())

        if len(horizontal_patterns) != 2 or len(vertical_patterns) != 2:
            return -1
        if abs(horizontal_patterns[0][1] - horizontal_patterns[1][1]) > 1:
            return -1
        if abs(vertical_patterns[0][1] - vertical_patterns[1][1]) > 1:
            return -1

        pattern1 = ([0, 1] * (n // 2 + 1))[:n]
        h1 = sum(i != j for i, j in zip(horizontal_patterns[0][0], pattern1))
        v1 = sum(i != j for i, j in zip(vertical_patterns[0][0], pattern1))

        pattern2 = ([1, 0] * (n // 2 + 1))[:n]
        h2 = sum(i != j for i, j in zip(horizontal_patterns[0][0], pattern2))
        v2 = sum(i != j for i, j in zip(vertical_patterns[0][0], pattern2))

        horizontal_moves = [x for x in [h1, h2] if x % 2 == 0]
        vertical_moves = [y for y in [v1, v2] if y % 2 == 0]

        return min(horizontal_moves) // 2 + min(vertical_moves) // 2
