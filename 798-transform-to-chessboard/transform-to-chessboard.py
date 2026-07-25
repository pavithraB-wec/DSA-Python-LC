class Solution(object):
    def movesToChessboard(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)

        # Check validity
        for i in range(n):
            for j in range(n):
                if (board[0][0] ^ board[i][0] ^
                    board[0][j] ^ board[i][j]):
                    return -1

        rowSum = sum(board[0])
        colSum = sum(board[i][0] for i in range(n))

        if not (n // 2 <= rowSum <= (n + 1) // 2):
            return -1
        if not (n // 2 <= colSum <= (n + 1) // 2):
            return -1

        rowSwap = 0
        colSwap = 0

        for i in range(n):
            if board[i][0] == i % 2:
                rowSwap += 1
            if board[0][i] == i % 2:
                colSwap += 1

        if n % 2:
            if rowSwap % 2:
                rowSwap = n - rowSwap
            if colSwap % 2:
                colSwap = n - colSwap
        else:
            rowSwap = min(rowSwap, n - rowSwap)
            colSwap = min(colSwap, n - colSwap)

        return (rowSwap + colSwap) // 2