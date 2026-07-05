class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        from collections import Counter

        wordLen = len(words[0])
        wordCount = len(words)
        totalLen = wordLen * wordCount

        target = Counter(words)
        result = []

        for offset in range(wordLen):

            left = offset
            current = Counter()
            count = 0

            for right in range(offset, len(s) - wordLen + 1, wordLen):

                word = s[right:right + wordLen]

                if word in target:

                    current[word] += 1
                    count += 1

                    while current[word] > target[word]:
                        leftWord = s[left:left + wordLen]
                        current[leftWord] -= 1
                        left += wordLen
                        count -= 1

                    if count == wordCount:
                        result.append(left)

                        leftWord = s[left:left + wordLen]
                        current[leftWord] -= 1
                        left += wordLen
                        count -= 1

                else:
                    current.clear()
                    count = 0
                    left = right + wordLen

        return result