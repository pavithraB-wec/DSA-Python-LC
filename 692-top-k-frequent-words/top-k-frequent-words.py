from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = Counter(words)

        result = sorted(count.keys(), key=lambda x: (-count[x], x))

        return result[:k]