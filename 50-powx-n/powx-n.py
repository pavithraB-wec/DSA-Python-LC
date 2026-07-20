class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        ans = 1.0

        while n:
            if n % 2 == 1:
                ans *= x
            x *= x
            n //= 2

        return ans