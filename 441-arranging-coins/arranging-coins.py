class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2
            coins = mid * (mid + 1) // 2

            if coins == n:
                return mid
            elif coins < n:
                left = mid + 1
            else:
                right = mid - 1

        return right