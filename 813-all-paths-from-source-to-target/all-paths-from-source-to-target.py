class Solution(object):
    def allPathsSourceTarget(self, graph):
        result = []
        path = [0]
        target = len(graph) - 1

        def dfs(node):
            if node == target:
                result.append(path[:])
                return

            for neighbor in graph[node]:
                path.append(neighbor)
                dfs(neighbor)
                path.pop()

        dfs(0)
        return result