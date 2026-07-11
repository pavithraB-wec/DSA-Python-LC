class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 2:
            return s

        count = 0
        start = 0
        parts = []

        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count -= 1

            if count == 0:
                parts.append(
                    "1" +
                    self.makeLargestSpecial(s[start + 1:i]) +
                    "0"
                )
                start = i + 1

        parts.sort(reverse=True)

        return "".join(parts)