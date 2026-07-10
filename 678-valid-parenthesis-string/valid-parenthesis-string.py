class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = 0
        high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                if low > 0:
                    low -= 1
                high -= 1
            else:  # '*'
                if low > 0:
                    low -= 1
                high += 1

            if high < 0:
                return False

        return low == 0