class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        answer = 0

        for top in range(m):
            col_sum = [0] * n

            for bottom in range(top, m):
                # Add the current row to each column
                for col in range(n):
                    col_sum[col] += matrix[bottom][col]

                # Count subarrays with sum = target
                count = {0: 1}
                prefix = 0

                for value in col_sum:
                    prefix += value

                    if prefix - target in count:
                        answer += count[prefix - target]

                    count[prefix] = count.get(prefix, 0) + 1

        return answer