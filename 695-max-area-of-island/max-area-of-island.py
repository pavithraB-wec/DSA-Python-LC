from collections import deque

class Solution(object):
    def maxAreaOfIsland(self, grid):
        m = len(grid)
        n = len(grid[0])

        max_area = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue = deque([(i, j)])
                    grid[i][j] = 0

                    area = 0

                    while queue:
                        r, c = queue.popleft()
                        area += 1

                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc

                            if 0 <= nr < m and 0 <= nc < n:
                                if grid[nr][nc] == 1:
                                    grid[nr][nc] = 0
                                    queue.append((nr, nc))

                    max_area = max(max_area, area)

        return max_area