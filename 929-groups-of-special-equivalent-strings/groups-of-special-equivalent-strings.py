class Solution(object):
    def numSpecialEquivGroups(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        groups = set()

        for word in words:
            even = ''.join(sorted(word[::2]))
            odd = ''.join(sorted(word[1::2]))
            groups.add((even, odd))

        return len(groups)