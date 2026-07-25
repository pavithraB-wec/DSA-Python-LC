class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = int(c ** 0.5)

        while left <= right:
            s = left * left + right * right

            if s == c:
                return True
            elif s < c:
                left += 1
            else:
                right -= 1

        return False