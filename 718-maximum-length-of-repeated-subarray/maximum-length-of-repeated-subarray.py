class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        m = len(nums1)
        n = len(nums2)

        dp = [0] * (n + 1)
        ans = 0

        for i in range(1, m + 1):
            for j in range(n, 0, -1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = dp[j - 1] + 1
                    ans = max(ans, dp[j])
                else:
                    dp[j] = 0

        return ans