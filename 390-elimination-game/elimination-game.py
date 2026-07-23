class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        head = 1
        step = 1
        left = True
        remaining = n

        while remaining > 1:
            if left or remaining % 2 == 1:
                head += step

            remaining //= 2
            step *= 2
            left = not left

        return head