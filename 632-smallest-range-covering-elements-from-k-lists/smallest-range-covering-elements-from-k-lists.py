import heapq

class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        heap = []
        current_max = float('-inf')

        # Initialize heap
        for i in range(len(nums)):
            val = nums[i][0]
            heapq.heappush(heap, (val, i, 0))
            current_max = max(current_max, val)

        left, right = -100000, 100000

        while True:
            current_min, row, col = heapq.heappop(heap)

            if current_max - current_min < right - left or (
                current_max - current_min == right - left and current_min < left
            ):
                left, right = current_min, current_max

            # If this list ends, we cannot continue
            if col + 1 == len(nums[row]):
                break

            next_val = nums[row][col + 1]
            heapq.heappush(heap, (next_val, row, col + 1))
            current_max = max(current_max, next_val)

        return [left, right]