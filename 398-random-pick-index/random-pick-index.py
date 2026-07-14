import random
from collections import defaultdict

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.mp = defaultdict(list)

        for i, num in enumerate(nums):
            self.mp[num].append(i)

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        indices = self.mp[target]
        return indices[random.randint(0, len(indices) - 1)]