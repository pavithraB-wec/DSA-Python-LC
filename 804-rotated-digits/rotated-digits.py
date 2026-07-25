class Solution(object):
    def rotatedDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        invalid = {3, 4, 7}
        change = {2, 5, 6, 9}

        ans = 0

        for num in range(1, n + 1):
            x = num
            good = False

            while x > 0:
                digit = x % 10

                if digit in invalid:
                    good = False
                    break

                if digit in change:
                    good = True

                x //= 10

            if good:
                ans += 1

        return ans