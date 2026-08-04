class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        ans = 0

        for k in range(n - 1, 1, -1):
            left = 0
            right = k - 1

            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    ans += right - left
                    right -= 1
                else:
                    left += 1

        return ans