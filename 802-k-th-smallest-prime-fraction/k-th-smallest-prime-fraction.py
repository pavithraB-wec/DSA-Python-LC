import heapq

class Solution(object):
    def kthSmallestPrimeFraction(self, arr, k):
        n = len(arr)
        heap = []

        # Start with 1 / every other number
        for j in range(1, n):
            heapq.heappush(heap, (float(arr[0]) / arr[j], 0, j))

        # Remove the smallest fraction k-1 times
        for _ in range(k - 1):
            value, i, j = heapq.heappop(heap)

            # Move to the next numerator
            if i + 1 < j:
                heapq.heappush(
                    heap,
                    (float(arr[i + 1]) / arr[j], i + 1, j)
                )

        value, i, j = heapq.heappop(heap)

        return [arr[i], arr[j]]