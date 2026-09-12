import heapq

class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)

        heap = [(grid[0][0], 0, 0)]
        visited = set()

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while heap:
            time, r, c = heapq.heappop(heap)

            if (r, c) in visited:
                continue

            visited.add((r, c))

            # Reached bottom-right
            if r == n - 1 and c == n - 1:
                return time

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < n and 0 <= nc < n:
                    if (nr, nc) not in visited:
                        new_time = max(time, grid[nr][nc])
                        heapq.heappush(heap, (new_time, nr, nc))

        return -1