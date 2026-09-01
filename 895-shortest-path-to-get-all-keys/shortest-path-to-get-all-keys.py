from collections import deque

class Solution(object):
    def shortestPathAllKeys(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Find starting position and total number of keys
        start_r = start_c = 0
        total_keys = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '@':
                    start_r, start_c = r, c
                elif 'a' <= grid[r][c] <= 'f':
                    total_keys = max(total_keys, ord(grid[r][c]) - ord('a') + 1)

        # All keys collected
        target = (1 << total_keys) - 1

        # BFS state: (row, column, keys_collected)
        queue = deque()
        queue.append((start_r, start_c, 0))

        # visited[row][column][key_mask]
        visited = set()
        visited.add((start_r, start_c, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        steps = 0

        while queue:
            for _ in range(len(queue)):
                r, c, keys = queue.popleft()

                # All keys collected
                if keys == target:
                    return steps

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    cell = grid[nr][nc]

                    # Wall
                    if cell == '#':
                        continue

                    new_keys = keys

                    # Pick up a key
                    if 'a' <= cell <= 'f':
                        key = ord(cell) - ord('a')
                        new_keys |= (1 << key)

                    # Lock
                    elif 'A' <= cell <= 'F':
                        key = ord(cell) - ord('A')

                        # Don't have the corresponding key
                        if not (keys & (1 << key)):
                            continue

                    state = (nr, nc, new_keys)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            steps += 1

        return -1

