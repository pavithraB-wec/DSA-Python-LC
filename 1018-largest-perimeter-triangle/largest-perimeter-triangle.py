class Solution(object):
    def largestPerimeter(self, nums):
        nums.sort(reverse=True)

        for i in range(len(nums) - 2):
            a = nums[i]
            b = nums[i + 1]
            c = nums[i + 2]

            if b + c > a:
                return a + b + c

        return 0