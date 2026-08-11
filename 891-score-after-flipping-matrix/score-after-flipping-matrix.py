class Solution(object):
    def matrixScore(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        # Step 1: Make the first column all 1s
        for i in range(rows):
            if grid[i][0] == 0:
                for j in range(cols):
                    grid[i][j] ^= 1

        # Step 2: For each remaining column,
        # make the number of 1s as large as possible
        for j in range(1, cols):
            ones = 0

            for i in range(rows):
                if grid[i][j] == 1:
                    ones += 1

            # If zeros are more, flip the column
            if ones < rows - ones:
                for i in range(rows):
                    grid[i][j] ^= 1

        # Step 3: Calculate the score
        score = 0

        for i in range(rows):
            for j in range(cols):
                score += grid[i][j] * (2 ** (cols - j - 1))

        return score