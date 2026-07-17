from collections import defaultdict

class Solution(object):
    def largestComponentSize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        parent = list(range(n))
        size = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return

            if size[px] < size[py]:
                px, py = py, px

            parent[py] = px
            size[px] += size[py]

        factor_to_index = {}

        for i, num in enumerate(nums):
            x = num
            d = 2

            while d * d <= x:
                if x % d == 0:
                    if d in factor_to_index:
                        union(i, factor_to_index[d])
                    else:
                        factor_to_index[d] = i

                    while x % d == 0:
                        x //= d
                d += 1

            if x > 1:
                if x in factor_to_index:
                    union(i, factor_to_index[x])
                else:
                    factor_to_index[x] = i

        ans = 1
        for i in range(n):
            ans = max(ans, size[find(i)])

        return ans