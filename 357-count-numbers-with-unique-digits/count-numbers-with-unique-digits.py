class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        ans = 10          # Numbers with 1 digit (including 0)
        unique = 9        # Count for current digit length
        available = 9

        while n > 1 and available > 0:
            unique *= available
            ans += unique
            available -= 1
            n -= 1

        return ans