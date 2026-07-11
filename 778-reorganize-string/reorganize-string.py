import heapq
from collections import Counter

class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        n = len(s)

        if max(count.values()) > (n + 1) // 2:
            return ""

        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)

        result = []

        while len(heap) >= 2:
            f1, c1 = heapq.heappop(heap)
            f2, c2 = heapq.heappop(heap)

            result.append(c1)
            result.append(c2)

            if f1 + 1 < 0:
                heapq.heappush(heap, (f1 + 1, c1))
            if f2 + 1 < 0:
                heapq.heappush(heap, (f2 + 1, c2))

        if heap:
            result.append(heap[0][1])

        return "".join(result)