class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        bad = set()

        # Numbers that can never be good
        for f, b in zip(fronts, backs):
            if f == b:
                bad.add(f)

        ans = float('inf')

        for x in fronts + backs:
            if x not in bad:
                ans = min(ans, x)

        return 0 if ans == float('inf') else ans