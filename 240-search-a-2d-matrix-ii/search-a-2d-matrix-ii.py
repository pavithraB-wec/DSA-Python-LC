class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            value = matrix[row][col]

            if value == target:
                return True

            elif value > target:
                # Move left
                col -= 1

            else:
                # Move down
                row += 1

        return False