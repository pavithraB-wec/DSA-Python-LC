from collections import Counter

class Solution(object):
    def reorderedPowerOf2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        target = Counter(str(n))

        for i in range(31):
            if Counter(str(1 << i)) == target:
                return True

        return False