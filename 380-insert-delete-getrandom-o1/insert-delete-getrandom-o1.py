import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
            return False

        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
            return False

        idx = self.pos[val]
        last = self.nums[-1]

        # Move last element into removed element's position
        self.nums[idx] = last
        self.pos[last] = idx

        # Remove last element
        self.nums.pop()
        del self.pos[val]

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.nums)