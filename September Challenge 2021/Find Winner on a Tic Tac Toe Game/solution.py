from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5:
            return 'Pending'

        board = [['', '', ''], ['', '', ''], ['', '', '']]
        for idx, (x, y) in enumerate(moves):
            board[x][y] = 'A' if idx % 2 == 0 else 'B'

        for i in range(3):
            # verticals
            if board[i][0] in ['A', 'B'] and board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]
            # horizontals
            if board[0][i] in ['A', 'B'] and board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]

        # diagonals
        if board[1][1] in ['A', 'B'] \
                and (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
            return board[1][1]

        return 'Pending' if len(moves) < 9 else 'Draw'
