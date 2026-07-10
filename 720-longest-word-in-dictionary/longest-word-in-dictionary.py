class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort()

        valid = set([""])
        ans = ""

        for word in sorted(words, key=len):
            if word[:-1] in valid:
                valid.add(word)
                if len(word) > len(ans):
                    ans = word

        return ans