class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        rounds = minutesToTest // minutesToDie
        states = rounds + 1

        pigs = 0
        while states ** pigs < buckets:
            pigs += 1

        return pigs