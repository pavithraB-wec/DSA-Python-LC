from collections import defaultdict

class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        waiting = defaultdict(list)

        for word in words:
            waiting[word[0]].append((word, 0))

        ans = 0

        for ch in s:
            current = waiting[ch]
            waiting[ch] = []

            for word, idx in current:
                idx += 1
                if idx == len(word):
                    ans += 1
                else:
                    waiting[word[idx]].append((word, idx))

        return ans