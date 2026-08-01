import heapq

class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        # Add destination as a station with 0 fuel
        stations.append([target, 0])

        max_heap = []
        fuel = startFuel
        prev = 0
        stops = 0

        for pos, gas in stations:
            fuel -= (pos - prev)

            while fuel < 0:
                if not max_heap:
                    return -1
                fuel += -heapq.heappop(max_heap)
                stops += 1

            heapq.heappush(max_heap, -gas)
            prev = pos

        return stops