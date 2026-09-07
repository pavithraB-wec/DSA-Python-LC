class Solution(object):
    def countBattleships(self, board):
        m = len(board)
        n = len(board[0])

        count = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    # Not part of a battleship coming from above
                    if i > 0 and board[i - 1][j] == 'X':
                        continue

                    # Not part of a battleship coming from the left
                    if j > 0 and board[i][j - 1] == 'X':
                        continue

                    count += 1

        return count