from collections import Counter

class Solution(object):
    def findMinStep(self, board, hand):
        hand = Counter(hand)
        memo = {}

        def shrink(s):
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                if j - i >= 3:
                    return shrink(s[:i] + s[j:])
                i = j
            return s

        def dfs(board, hand):
            board = shrink(board)

            if not board:
                return 0

            key = (board, tuple(sorted(hand.items())))
            if key in memo:
                return memo[key]

            ans = float('inf')

            for i in range(len(board) + 1):
                for c in "RYBGW":
                    if hand[c] == 0:
                        continue

                    if i > 0 and board[i - 1] == c:
                        continue

                    if (i < len(board) and board[i] == c) or \
                       (i > 0 and i < len(board) and board[i - 1] == board[i] and board[i] != c):

                        hand[c] -= 1
                        res = dfs(board[:i] + c + board[i:], hand)
                        if res != float('inf'):
                            ans = min(ans, res + 1)
                        hand[c] += 1

            memo[key] = ans
            return ans

        ans = dfs(board, hand)
        return -1 if ans == float('inf') else ans