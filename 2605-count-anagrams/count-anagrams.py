class Solution(object):
    def countAnagrams(self, s):
        MOD = 10**9 + 7
        words = s.split()
        result = 1

        for word in words:
            n = len(word)
            fact = [1] * (n + 1)

            for i in range(1, n + 1):
                fact[i] = fact[i - 1] * i % MOD

            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1

            ways = fact[n]

            for freq in count:
                ways = ways * pow(fact[freq], MOD - 2, MOD) % MOD

            result = result * ways % MOD

        return result