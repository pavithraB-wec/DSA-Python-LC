import heapq

class Solution(object):
    def getSkyline(self, buildings):
        events = []

        for left, right, height in buildings:
            # Start event
            events.append((left, -height, right))

            # End event
            events.append((right, 0, 0))

        events.sort()

        heap = [(0, float('inf'))]
        answer = []
        i = 0

        while i < len(events):
            x = events[i][0]

            # Process all events at this x
            while i < len(events) and events[i][0] == x:
                _, neg_height, right = events[i]

                if neg_height != 0:
                    heapq.heappush(heap, (neg_height, right))

                i += 1

            # Remove buildings that have ended
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)

            current_height = -heap[0][0]

            # Add key point only when height changes
            if not answer or answer[-1][1] != current_height:
                answer.append([x, current_height])

        return answer