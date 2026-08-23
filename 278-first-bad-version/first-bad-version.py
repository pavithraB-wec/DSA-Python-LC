class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                # mid is bad, so first bad is mid or before it
                right = mid
            else:
                # mid is good, so first bad is after mid
                left = mid + 1

        return left