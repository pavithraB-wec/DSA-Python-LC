class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        answer = [n] * n

        # Left to right
        distance = n

        for i in range(n):
            if s[i] == c:
                distance = 0
            else:
                distance += 1

            answer[i] = distance

        # Right to left
        distance = n

        for i in range(n - 1, -1, -1):
            if s[i] == c:
                distance = 0
            else:
                distance += 1

            answer[i] = min(answer[i], distance)

        return answer