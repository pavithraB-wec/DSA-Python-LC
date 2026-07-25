class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        k = 1

        while k * (k - 1) // 2 < n:
            remain = n - k * (k - 1) // 2
            if remain % k == 0:
                ans += 1
            k += 1

        return ans