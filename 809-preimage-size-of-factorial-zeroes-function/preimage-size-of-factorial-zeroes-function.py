class Solution(object):
    def preimageSizeFZF(self, k):
        """
        :type k: int
        :rtype: int
        """

        def zeta(x):
            cnt = 0
            while x:
                x //= 5
                cnt += x
            return cnt

        left, right = 0, 5 * (k + 1)

        while left < right:
            mid = (left + right) // 2
            if zeta(mid) < k:
                left = mid + 1
            else:
                right = mid

        return 5 if zeta(left) == k else 0