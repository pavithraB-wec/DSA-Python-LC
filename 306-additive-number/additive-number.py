class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):

                # Leading zero check for first number
                if num[0] == '0' and i > 1:
                    break

                # Leading zero check for second number
                if num[i] == '0' and j - i > 1:
                    continue

                first = int(num[:i])
                second = int(num[i:j])

                if self.check(first, second, j, num):
                    return True

        return False

    def check(self, first, second, start, num):
        while start < len(num):
            total = first + second
            total_str = str(total)

            if not num.startswith(total_str, start):
                return False

            start += len(total_str)
            first = second
            second = total

        return True