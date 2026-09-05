from collections import deque

class Solution(object):
    def minFlips(self, mat):
        m = len(mat)
        n = len(mat[0])

        start = 0

        # Convert matrix to a bitmask
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    start |= 1 << (i * n + j)

        if start == 0:
            return 0

        queue = deque([(start, 0)])
        visited = set([start])

        directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            state, steps = queue.popleft()

            for i in range(m):
                for j in range(n):
                    new_state = state

                    # Flip current cell and its neighbors
                    for di, dj in directions:
                        ni = i + di
                        nj = j + dj

                        if 0 <= ni < m and 0 <= nj < n:
                            bit = 1 << (ni * n + nj)
                            new_state ^= bit

                    if new_state == 0:
                        return steps + 1

                    if new_state not in visited:
                        visited.add(new_state)
                        queue.append((new_state, steps + 1))

        return -1