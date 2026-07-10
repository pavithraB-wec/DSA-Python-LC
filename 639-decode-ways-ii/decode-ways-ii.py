class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10 ** 9 + 7

        def one(c):
            if c == '*':
                return 9
            if c == '0':
                return 0
            return 1

        def two(c1, c2):
            if c1 == '*' and c2 == '*':
                return 15
            elif c1 == '*':
                if '0' <= c2 <= '6':
                    return 2
                else:
                    return 1
            elif c2 == '*':
                if c1 == '1':
                    return 9
                elif c1 == '2':
                    return 6
                else:
                    return 0
            else:
                num = int(c1 + c2)
                return 1 if 10 <= num <= 26 else 0

        n = len(s)

        prev2 = 1
        prev1 = one(s[0])

        for i in range(1, n):
            curr = (one(s[i]) * prev1 + two(s[i - 1], s[i]) * prev2) % MOD
            prev2 = prev1
            prev1 = curr

        return prev1