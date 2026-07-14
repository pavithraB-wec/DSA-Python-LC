class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        mask = 0

        for i in range(31, -1, -1):
            mask |= (1 << i)

            prefixes = set()
            for num in nums:
                prefixes.add(num & mask)

            candidate = ans | (1 << i)

            for p in prefixes:
                if (candidate ^ p) in prefixes:
                    ans = candidate
                    break

        return ans