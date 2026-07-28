class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        dp = {stone: set() for stone in stones}
        dp[0].add(0)

        stone_set = set(stones)

        for stone in stones:
            for jump in dp[stone]:
                for step in (jump - 1, jump, jump + 1):
                    if step > 0 and stone + step in stone_set:
                        dp[stone + step].add(step)

        return len(dp[stones[-1]]) > 0