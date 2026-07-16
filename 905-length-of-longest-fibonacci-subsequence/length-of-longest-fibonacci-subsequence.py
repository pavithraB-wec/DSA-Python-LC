class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        index = {x: i for i, x in enumerate(arr)}
        dp = {}
        ans = 0

        for i in range(n):
            for j in range(i):
                prev = arr[i] - arr[j]

                if prev < arr[j] and prev in index:
                    k = index[prev]
                    dp[(j, i)] = dp.get((k, j), 2) + 1
                    ans = max(ans, dp[(j, i)])
                else:
                    dp[(j, i)] = 2

        return ans if ans >= 3 else 0