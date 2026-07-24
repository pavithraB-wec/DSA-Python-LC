import random
import bisect

class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects
        self.prefix = []
        total = 0

        for a, b, x, y in rects:
            total += (x - a + 1) * (y - b + 1)
            self.prefix.append(total)

    def pick(self):
        """
        :rtype: List[int]
        """
        target = random.randint(1, self.prefix[-1])
        idx = bisect.bisect_left(self.prefix, target)

        a, b, x, y = self.rects[idx]

        return [
            random.randint(a, x),
            random.randint(b, y)
        ]