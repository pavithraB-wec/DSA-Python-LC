class Solution(object):
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        nums = []

        for row in grid:
            nums.extend(row)

        total = m * n
        k = k % total

        if k != 0:
            nums = nums[-k:] + nums[:-k]

        result = []

        for i in range(0, total, n):
            result.append(nums[i:i + n])

        return result