import heapq

class Solution(object):
    def minOperations(self, nums, k):
        heapq.heapify(nums)
        count = 0

        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)

            new_value = x * 2 + y

            heapq.heappush(nums, new_value)
            count += 1

        return count