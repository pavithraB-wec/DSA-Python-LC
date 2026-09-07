from heapq import heappush, heappop

class Solution(object):
    def trapRainWater(self, heightMap):
        m = len(heightMap)
        n = len(heightMap[0])

        if m < 3 or n < 3:
            return 0

        heap = []
        visited = [[False] * n for _ in range(m)]

        # Add all boundary cells
        for i in range(m):
            heappush(heap, (heightMap[i][0], i, 0))
            heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][0] = True
            visited[i][n - 1] = True

        for j in range(1, n - 1):
            heappush(heap, (heightMap[0][j], 0, j))
            heappush(heap, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = True
            visited[m - 1][j] = True

        water = 0

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while heap:
            height, i, j = heappop(heap)

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if 0 <= ni < m and 0 <= nj < n:
                    if not visited[ni][nj]:
                        visited[ni][nj] = True

                        new_height = max(height, heightMap[ni][nj])

                        if height > heightMap[ni][nj]:
                            water += height - heightMap[ni][nj]

                        heappush(heap, (new_height, ni, nj))

        return water