from collections import deque

class Solution(object):
    def shortestSubarray(self, nums, k):
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        dq = deque()
        answer = n + 1

        for i in range(n + 1):

            while dq and prefix[i] - prefix[dq[0]] >= k:
                answer = min(answer, i - dq.popleft())

            while dq and prefix[i] <= prefix[dq[-1]]:
                dq.pop()

            dq.append(i)

        if answer == n + 1:
            return -1

        return answer