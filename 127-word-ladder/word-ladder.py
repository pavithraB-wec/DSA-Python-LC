from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            wordChars = list(word)

            for i in range(len(wordChars)):
                original = wordChars[i]

                for c in "abcdefghijklmnopqrstuvwxyz":
                    wordChars[i] = c
                    newWord = "".join(wordChars)

                    if newWord in wordSet:
                        queue.append((newWord, length + 1))
                        wordSet.remove(newWord)

                wordChars[i] = original

        return 0