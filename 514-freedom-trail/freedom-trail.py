from collections import defaultdict

class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        positions = defaultdict(list)

        for i, ch in enumerate(ring):
            positions[ch].append(i)

        memo = {}
        n = len(ring)

        def dfs(i, pos):
            if i == len(key):
                return 0

            if (i, pos) in memo:
                return memo[(i, pos)]

            ans = float('inf')

            for nxt in positions[key[i]]:
                dist = abs(pos - nxt)
                step = min(dist, n - dist)

                ans = min(ans, step + 1 + dfs(i + 1, nxt))

            memo[(i, pos)] = ans
            return ans

        return dfs(0, 0)