import heapq

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = []

        # Create events
        for left, right, height in buildings:
            events.append((left, -height, right))
            events.append((right, 0, 0))

        events.sort()

        result = []
        heap = [(0, float('inf'))]  # (-height, right)

        for x, neg_h, right in events:

            # Remove buildings that ended
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            # Add new building
            if neg_h:
                heapq.heappush(heap, (neg_h, right))

            curr_height = -heap[0][0]

            if not result or result[-1][1] != curr_height:
                result.append([x, curr_height])

        return result