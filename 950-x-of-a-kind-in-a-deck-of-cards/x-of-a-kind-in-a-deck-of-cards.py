from collections import Counter

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        count = Counter(deck)

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g = 0
        for freq in count.values():
            g = gcd(g, freq)

        return g >= 2