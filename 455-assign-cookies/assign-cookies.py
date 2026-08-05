class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        i = 0  # child pointer
        j = 0  # cookie pointer

        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
            j += 1

        return i