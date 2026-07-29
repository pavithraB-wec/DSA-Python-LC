class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)

        # Sum of every subarray of length k
        window = [0] * (n - k + 1)
        s = sum(nums[:k])
        window[0] = s

        for i in range(1, len(window)):
            s += nums[i + k - 1] - nums[i - 1]
            window[i] = s

        m = len(window)

        # Best subarray from the left
        left = [0] * m
        best = 0
        for i in range(m):
            if window[i] > window[best]:
                best = i
            left[i] = best

        # Best subarray from the right
        right = [0] * m
        best = m - 1
        for i in range(m - 1, -1, -1):
            if window[i] >= window[best]:
                best = i
            right[i] = best

        ans = [-1, -1, -1]
        max_sum = 0

        for mid in range(k, m - k):
            l = left[mid - k]
            r = right[mid + k]
            total = window[l] + window[mid] + window[r]

            if total > max_sum:
                max_sum = total
                ans = [l, mid, r]

        return ans