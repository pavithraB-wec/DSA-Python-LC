class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])

        count = 0
        end = float('-inf')

        for left, right in pairs:
            if left > end:
                count += 1
                end = right

        return count