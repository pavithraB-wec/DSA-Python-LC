class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        n = len(score)
        ans = [""] * n

        athletes = sorted(
            [(score[i], i) for i in range(n)],
            reverse=True
        )

        for rank, (_, idx) in enumerate(athletes, 1):
            if rank == 1:
                ans[idx] = "Gold Medal"
            elif rank == 2:
                ans[idx] = "Silver Medal"
            elif rank == 3:
                ans[idx] = "Bronze Medal"
            else:
                ans[idx] = str(rank)

        return ans