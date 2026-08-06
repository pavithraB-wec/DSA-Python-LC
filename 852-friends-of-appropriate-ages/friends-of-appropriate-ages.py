class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        ans = 0
        left = 0
        right = 0
        n = len(ages)

        for i in range(n):
            if ages[i] < 15:
                continue

            while ages[left] <= ages[i] / 2.0 + 7:
                left += 1

            while right + 1 < n and ages[right + 1] <= ages[i]:
                right += 1

            ans += right - left

        return ans