import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.original = nums[:]

    def reset(self):
        """
        :rtype: List[int]
        """
        return self.original[:]

    def shuffle(self):
        """
        :rtype: List[int]
        """
        arr = self.original[:]
        n = len(arr)

        for i in range(n):
            j = random.randint(i, n - 1)
            arr[i], arr[j] = arr[j], arr[i]

        return arr