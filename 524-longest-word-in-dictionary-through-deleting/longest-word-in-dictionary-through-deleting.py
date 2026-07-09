class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        def isSubsequence(word, s):
            i = j = 0
            while i < len(word) and j < len(s):
                if word[i] == s[j]:
                    i += 1
                j += 1
            return i == len(word)

        ans = ""

        for word in dictionary:
            if isSubsequence(word, s):
                if len(word) > len(ans) or \
                   (len(word) == len(ans) and word < ans):
                    ans = word

        return ans