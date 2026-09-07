from collections import deque

class Solution(object):
    def pacificAtlantic(self, heights):
        m = len(heights)
        n = len(heights[0])

        pacific = set()
        atlantic = set()

        pacific_queue = deque()
        atlantic_queue = deque()

        # Pacific: top row and left column
        for i in range(m):
            pacific.add((i, 0))
            pacific_queue.append((i, 0))

        for j in range(n):
            pacific.add((0, j))
            pacific_queue.append((0, j))

        # Atlantic: bottom row and right column
        for i in range(m):
            atlantic.add((i, n - 1))
            atlantic_queue.append((i, n - 1))

        for j in range(n):
            atlantic.add((m - 1, j))
            atlantic_queue.append((m - 1, j))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        # BFS from an ocean
        def bfs(queue, visited):
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        if (nr, nc) not in visited:
                            if heights[nr][nc] >= heights[r][c]:
                                visited.add((nr, nc))
                                queue.append((nr, nc))

        bfs(pacific_queue, pacific)
        bfs(atlantic_queue, atlantic)

        result = []

        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])

        return result