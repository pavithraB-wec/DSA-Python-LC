from collections import Counter

class Solution(object):
    def wordSubsets(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: List[str]
        """
        required = Counter()

        # Maximum frequency needed for each letter
        for word in words2:
            count = Counter(word)
            for ch in count:
                required[ch] = max(required[ch], count[ch])

        ans = []

        for word in words1:
            count = Counter(word)
            ok = True

            for ch in required:
                if count[ch] < required[ch]:
                    ok = False
                    break

            if ok:
                ans.append(word)

        return ans