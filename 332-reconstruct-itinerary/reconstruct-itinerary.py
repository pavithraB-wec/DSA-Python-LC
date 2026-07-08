from collections import defaultdict

class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)

        # Sort in reverse so we can pop the smallest destination
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        itinerary = []

        def dfs(airport):
            while graph[airport]:
                nxt = graph[airport].pop()
                dfs(nxt)
            itinerary.append(airport)

        dfs("JFK")

        return itinerary[::-1]