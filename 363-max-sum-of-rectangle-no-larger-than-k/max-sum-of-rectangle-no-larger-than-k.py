from bisect import bisect_left, insort

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])

        # For efficiency, make n the smaller dimension
        if m < n:
            matrix = [list(row) for row in zip(*matrix)]
            m, n = n, m

        result = float('-inf')

        # Fix two columns
        for left in range(n):
            row_sum = [0] * m

            for right in range(left, n):
                # Add the current column
                for r in range(m):
                    row_sum[r] += matrix[r][right]

                # Now find max subarray sum <= k
                # using prefix sums + sorted list
                prefix = 0
                sorted_prefix = [0]

                for value in row_sum:
                    prefix += value

                    # Need:
                    # prefix - old_prefix <= k
                    # old_prefix >= prefix - k
                    index = bisect_left(
                        sorted_prefix,
                        prefix - k
                    )

                    if index < len(sorted_prefix):
                        result = max(
                            result,
                            prefix - sorted_prefix[index]
                        )

                    insort(sorted_prefix, prefix)

        return result