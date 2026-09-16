class Solution(object):
    def longestWPI(self, hours):
        first = {}
        score = 0
        answer = 0

        for i in range(len(hours)):
            if hours[i] > 8:
                score += 1
            else:
                score -= 1

            if score > 0:
                answer = i + 1
            else:
                if score - 1 in first:
                    answer = max(answer, i - first[score - 1])

            if score not in first:
                first[score] = i

        return answer