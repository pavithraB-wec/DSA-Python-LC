class Solution(object):
    def containVirus(self, isInfected):
        m = len(isInfected)
        n = len(isInfected[0])

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        total_walls = 0

        while True:
            regions = []
            visited = set()

            # Find all infected regions
            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and (i, j) not in visited:

                        stack = [(i, j)]
                        visited.add((i, j))

                        cells = []
                        frontier = set()
                        walls = 0

                        while stack:
                            r, c = stack.pop()
                            cells.append((r, c))

                            for dr, dc in directions:
                                nr = r + dr
                                nc = c + dc

                                if 0 <= nr < m and 0 <= nc < n:
                                    if isInfected[nr][nc] == 0:
                                        frontier.add((nr, nc))
                                        walls += 1

                                    elif isInfected[nr][nc] == 1:
                                        if (nr, nc) not in visited:
                                            visited.add((nr, nc))
                                            stack.append((nr, nc))

                        regions.append((cells, frontier, walls))

            # No region can spread
            if not regions:
                break

            # Find the region threatening the most cells
            max_index = -1
            max_frontier = 0

            for i in range(len(regions)):
                if len(regions[i][1]) > max_frontier:
                    max_frontier = len(regions[i][1])
                    max_index = i

            # If nobody can infect a new cell, stop
            if max_index == -1 or max_frontier == 0:
                break

            # Quarantine the most dangerous region
            cells, frontier, walls = regions[max_index]

            total_walls += walls

            for r, c in cells:
                isInfected[r][c] = -1

            # Spread all other regions
            for i in range(len(regions)):
                if i == max_index:
                    continue

                cells, frontier, walls = regions[i]

                for r, c in frontier:
                    isInfected[r][c] = 1

        return total_walls