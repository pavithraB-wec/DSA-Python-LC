class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def backtrack(pos, mask):
            if pos > n:
                return 1

            count = 0
            for num in range(1, n + 1):
                if not (mask & (1 << num)):
                    if num % pos == 0 or pos % num == 0:
                        count += backtrack(pos + 1, mask | (1 << num))

            return count

        return backtrack(1, 0)