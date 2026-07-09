class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('A') >= 2:
            return False

        if "LLL" in s:
            return False

        return True