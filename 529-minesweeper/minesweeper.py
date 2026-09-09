from collections import deque

class Solution(object):
    def updateBoard(self, board, click):
        m = len(board)
        n = len(board[0])

        r, c = click

        # Clicked on a mine
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        queue = deque()
        queue.append((r, c))

        while queue:
            r, c = queue.popleft()

            # Count adjacent mines
            mines = 0

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if board[nr][nc] == 'M':
                        mines += 1

            # Has adjacent mines
            if mines > 0:
                board[r][c] = str(mines)

            # No adjacent mines
            else:
                board[r][c] = 'B'

                # Reveal adjacent unrevealed cells
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        if board[nr][nc] == 'E':
                            queue.append((nr, nc))
                            board[nr][nc] = 'B'

        return board