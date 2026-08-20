from collections import deque

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]

        # Build adjacency list
        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Degree of each node
        degree = [len(graph[i]) for i in range(n)]

        # Add all leaf nodes
        queue = deque()

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)

        remaining = n

        # Remove leaves layer by layer
        while remaining > 2:
            size = len(queue)
            remaining -= size

            for _ in range(size):
                leaf = queue.popleft()

                for neighbor in graph[leaf]:
                    degree[neighbor] -= 1

                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)