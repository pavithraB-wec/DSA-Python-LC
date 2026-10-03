class Solution(object):
    def tictactoe(self, moves):
        board = [[''] * 3 for _ in range(3)]

        for i in range(len(moves)):
            r, c = moves[i]

            if i % 2 == 0:
                board[r][c] = 'X'
                player = 'A'
            else:
                board[r][c] = 'O'
                player = 'B'

            # Check rows
            for row in board:
                if row[0] != '' and row[0] == row[1] == row[2]:
                    return player

            # Check columns
            for col in range(3):
                if (board[0][col] != '' and
                    board[0][col] == board[1][col] == board[2][col]):
                    return player

            # Check main diagonal
            if (board[0][0] != '' and
                board[0][0] == board[1][1] == board[2][2]):
                return player

            # Check other diagonal
            if (board[0][2] != '' and
                board[0][2] == board[1][1] == board[2][0]):
                return player

        if len(moves) == 9:
            return "Draw"

        return "Pending"