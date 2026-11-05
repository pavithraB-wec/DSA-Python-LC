import heapq

class Solution(object):
    def kthLargestValue(self, matrix, k):
        m = len(matrix)
        n = len(matrix[0])

        heap = []

        for i in range(m):
            for j in range(n):
                if i > 0:
                    matrix[i][j] ^= matrix[i - 1][j]

                if j > 0:
                    matrix[i][j] ^= matrix[i][j - 1]

                if i > 0 and j > 0:
                    matrix[i][j] ^= matrix[i - 1][j - 1]

                heapq.heappush(heap, -matrix[i][j])

        for _ in range(k):
            result = -heapq.heappop(heap)

        return result