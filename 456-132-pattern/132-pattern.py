class Solution(object):
    def find132pattern(self, nums):
        n = len(nums)

        if n < 3:
            return False

        stack = []
        second = float('-inf')

        # Traverse from right to left
        for i in range(n - 1, -1, -1):

            # nums[i] can be the "1"
            if nums[i] < second:
                return True

            # nums[i] can be the "3"
            while stack and nums[i] > stack[-1]:
                # The popped value can be the "2"
                second = stack.pop()

            stack.append(nums[i])

        return False