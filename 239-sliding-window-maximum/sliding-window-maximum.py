from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []

        for i in range(len(nums)):
            # Remove elements outside the window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller elements
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            # Window is ready
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result