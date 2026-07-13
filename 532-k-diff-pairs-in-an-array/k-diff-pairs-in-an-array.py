from collections import Counter

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        freq = Counter(nums)
        count = 0

        if k == 0:
            for num in freq:
                if freq[num] > 1:
                    count += 1
        else:
            for num in freq:
                if num + k in freq:
                    count += 1

        return count