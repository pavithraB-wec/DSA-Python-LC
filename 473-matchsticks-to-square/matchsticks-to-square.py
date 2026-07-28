class Solution(object):
    def makesquare(self, matchsticks):
        """
        :type matchsticks: List[int]
        :rtype: bool
        """
        if not matchsticks:
            return False

        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        side = total // 4
        matchsticks.sort(reverse=True)

        if matchsticks[0] > side:
            return False

        sides = [0, 0, 0, 0]

        def dfs(index):
            if index == len(matchsticks):
                return True

            for i in range(4):
                if sides[i] + matchsticks[index] <= side:
                    sides[i] += matchsticks[index]

                    if dfs(index + 1):
                        return True

                    sides[i] -= matchsticks[index]

                if sides[i] == 0:
                    break

            return False

        return dfs(0)