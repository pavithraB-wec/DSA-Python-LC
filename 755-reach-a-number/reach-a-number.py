class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        total = 0
        step = 0

        while total < target or (total - target) % 2 != 0:
            step += 1
            total += step

        return step