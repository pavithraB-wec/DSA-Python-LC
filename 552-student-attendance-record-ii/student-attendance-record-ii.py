class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7

        dp = [[0] * 3 for _ in range(2)]
        dp[0][0] = 1

        for _ in range(n):
            new = [[0] * 3 for _ in range(2)]

            for a in range(2):
                for l in range(3):
                    if dp[a][l] == 0:
                        continue

                    # Present
                    new[a][0] = (new[a][0] + dp[a][l]) % MOD

                    # Absent
                    if a == 0:
                        new[1][0] = (new[1][0] + dp[a][l]) % MOD

                    # Late
                    if l < 2:
                        new[a][l + 1] = (new[a][l + 1] + dp[a][l]) % MOD

            dp = new

        ans = 0
        for a in range(2):
            for l in range(3):
                ans = (ans + dp[a][l]) % MOD

        return ans