class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n
        ans = [0] * n

        # Post-order DFS
        def dfs(node, parent):
            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
                count[node] += count[nei]
                ans[node] += ans[nei] + count[nei]

        # Pre-order DFS (re-root)
        def dfs2(node, parent):
            for nei in graph[node]:
                if nei == parent:
                    continue
                ans[nei] = ans[node] - count[nei] + (n - count[nei])
                dfs2(nei, node)

        dfs(0, -1)
        dfs2(0, -1)

        return ans