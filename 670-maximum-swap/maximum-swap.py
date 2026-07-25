class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        last = {}

        for i, d in enumerate(digits):
            last[int(d)] = i

        for i, d in enumerate(digits):
            for bigger in range(9, int(d), -1):
                if bigger in last and last[bigger] > i:
                    j = last[bigger]
                    digits[i], digits[j] = digits[j], digits[i]
                    return int("".join(digits))

        return num