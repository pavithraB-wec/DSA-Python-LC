from collections import Counter

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        max_num = max(nums)

        points = [0] * (max_num + 1)

        for num in count:
            points[num] = num * count[num]

        prev2 = 0
        prev1 = 0

        for value in points:
            curr = max(prev1, prev2 + value)
            prev2 = prev1
            prev1 = curr

        return prev1