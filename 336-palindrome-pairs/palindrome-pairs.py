class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        def isPalindrome(s):
            return s == s[::-1]

        word_map = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):

                prefix = word[:j]
                suffix = word[j:]

                # Case 1
                if isPalindrome(prefix):
                    rev = suffix[::-1]
                    if rev in word_map and word_map[rev] != i:
                        result.append([word_map[rev], i])

                # Case 2
                # j != len(word) avoids duplicate pairs
                if j != len(word) and isPalindrome(suffix):
                    rev = prefix[::-1]
                    if rev in word_map and word_map[rev] != i:
                        result.append([i, word_map[rev]])

        return result