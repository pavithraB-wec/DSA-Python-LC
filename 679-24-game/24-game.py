class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        EPS = 1e-6

        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS

            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    rest = []
                    for k in range(len(nums)):
                        if k != i and k != j:
                            rest.append(nums[k])

                    a, b = nums[i], nums[j]

                    for val in [a + b, a - b, b - a, a * b]:
                        if dfs(rest + [val]):
                            return True

                    if abs(b) > EPS:
                        if dfs(rest + [a / b]):
                            return True

                    if abs(a) > EPS:
                        if dfs(rest + [b / a]):
                            return True

            return False

        return dfs([float(x) for x in cards])