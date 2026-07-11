class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        count = [0] * 26

        # Count frequency of characters in s
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        result = []

        # Add characters according to custom order
        for ch in order:
            idx = ord(ch) - ord('a')
            while count[idx] > 0:
                result.append(ch)
                count[idx] -= 1

        # Add remaining characters
        for i in range(26):
            while count[i] > 0:
                result.append(chr(i + ord('a')))
                count[i] -= 1

        return "".join(result)