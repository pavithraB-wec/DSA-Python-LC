class Solution(object):
    def canMakePaliQueries(self, s, queries):
        n = len(s)

        # prefix[i][c] = count of character c in s[0:i]
        prefix = [[0] * 26 for _ in range(n + 1)]

        for i in range(n):
            prefix[i + 1] = prefix[i][:]
            prefix[i + 1][ord(s[i]) - ord('a')] += 1

        answer = []

        for left, right, k in queries:
            odd = 0

            for c in range(26):
                count = prefix[right + 1][c] - prefix[left][c]

                if count % 2 == 1:
                    odd += 1

            if odd // 2 <= k:
                answer.append(True)
            else:
                answer.append(False)

        return answer