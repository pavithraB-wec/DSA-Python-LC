class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        def isSubsequence(a, b):
            i = j = 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)

        strs.sort(key=len, reverse=True)

        for i in range(len(strs)):
            found = False

            for j in range(len(strs)):
                if i == j:
                    continue
                if isSubsequence(strs[i], strs[j]):
                    found = True
                    break

            if not found:
                return len(strs[i])

        return -1