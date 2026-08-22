class Solution(object):
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                # Minimum is on the left side, including mid
                right = mid

            elif nums[mid] > nums[right]:
                # Minimum is on the right side
                left = mid + 1

            else:
                # nums[mid] == nums[right]
                # We cannot determine the sorted side
                right -= 1

        return nums[left]