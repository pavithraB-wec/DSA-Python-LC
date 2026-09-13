class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        # Store prefix products
        prefix = 1

        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Multiply by suffix products
        suffix = 1

        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer