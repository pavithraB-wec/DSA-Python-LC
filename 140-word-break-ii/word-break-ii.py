class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in wordSet:
                    for suffix in dfs(end):
                        if suffix:
                            result.append(word + " " + suffix)
                        else:
                            result.append(word)

            memo[start] = result
            return result

        return dfs(0)