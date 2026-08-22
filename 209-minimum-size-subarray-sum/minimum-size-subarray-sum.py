class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            # Try to shrink the window
            while current_sum >= target:
                min_length = min(min_length, right - left + 1)

                current_sum -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length