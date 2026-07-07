class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0

        for ch in columnTitle:
            result = result * 26 + (ord(ch) - ord('A') + 1)

        return result