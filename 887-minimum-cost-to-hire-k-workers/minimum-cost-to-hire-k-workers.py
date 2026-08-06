import heapq

class Solution(object):
    def mincostToHireWorkers(self, quality, wage, k):
        """
        :type quality: List[int]
        :type wage: List[int]
        :type k: int
        :rtype: float
        """
        workers = []

        for q, w in zip(quality, wage):
            workers.append((float(w) / q, q))

        workers.sort()

        max_heap = []
        quality_sum = 0
        ans = float('inf')

        for ratio, q in workers:
            heapq.heappush(max_heap, -q)
            quality_sum += q

            if len(max_heap) > k:
                quality_sum += heapq.heappop(max_heap)

            if len(max_heap) == k:
                ans = min(ans, ratio * quality_sum)

        return ans