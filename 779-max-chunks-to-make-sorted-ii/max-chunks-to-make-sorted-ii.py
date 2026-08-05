class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)

        prefixMax = [0] * n
        suffixMin = [0] * n

        prefixMax[0] = arr[0]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], arr[i])

        suffixMin[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            suffixMin[i] = min(suffixMin[i + 1], arr[i])

        chunks = 1
        for i in range(n - 1):
            if prefixMax[i] <= suffixMin[i + 1]:
                chunks += 1

        return chunks