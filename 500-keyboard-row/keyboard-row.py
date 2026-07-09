class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            w = word.lower()

            if all(c in row1 for c in w) or \
               all(c in row2 for c in w) or \
               all(c in row3 for c in w):
                result.append(word)

        return result