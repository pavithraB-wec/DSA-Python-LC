import random
import bisect

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix = []
        total = 0

        for weight in w:
            total += weight
            self.prefix.append(total)

        self.total = total

    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)