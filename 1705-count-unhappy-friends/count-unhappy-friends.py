class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        partner = [-1] * n
        rank = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n - 1):
                rank[i][preferences[i][j]] = j

        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        unhappy = 0

        for x in range(n):
            y = partner[x]

            for u in preferences[x]:
                if u == y:
                    break

                v = partner[u]

                if rank[u][x] < rank[u][v]:
                    unhappy += 1
                    break

        return unhappy