class Solution(object):
    def splitArraySameAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        total = sum(nums)

        # Quick check: there must exist a subset size k
        # such that total * k is divisible by n.
        possible = False
        for k in range(1, n // 2 + 1):
            if (total * k) % n == 0:
                possible = True
                break
        if not possible:
            return False

        dp = [set() for _ in range(n + 1)]
        dp[0].add(0)

        for num in nums:
            for k in range(n - 1, -1, -1):
                for s in list(dp[k]):
                    dp[k + 1].add(s + num)

        for k in range(1, n // 2 + 1):
            if (total * k) % n == 0:
                target = (total * k) // n
                if target in dp[k]:
                    return True

        return False