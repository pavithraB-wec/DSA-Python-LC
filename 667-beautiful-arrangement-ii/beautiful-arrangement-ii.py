class Solution(object):
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        ans = []
        left, right = 1, k + 1

        while left <= right:
            ans.append(left)
            left += 1
            if left <= right:
                ans.append(right)
                right -= 1

        for i in range(k + 2, n + 1):
            ans.append(i)

        return ans