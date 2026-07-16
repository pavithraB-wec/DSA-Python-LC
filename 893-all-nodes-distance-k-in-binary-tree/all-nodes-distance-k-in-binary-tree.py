from collections import deque

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parent = {}

        # Build parent map
        def dfs(node, par):
            if not node:
                return
            parent[node] = par
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        queue = deque([(target, 0)])
        visited = set([target])

        ans = []

        while queue:
            node, dist = queue.popleft()

            if dist == k:
                ans.append(node.val)
                continue

            for nxt in (node.left, node.right, parent[node]):
                if nxt and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, dist + 1))

        return ans