class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n

        min_row = m
        min_col = n

        for a, b in ops:
            min_row = min(min_row, a)
            min_col = min(min_col, b)

        return min_row * min_col