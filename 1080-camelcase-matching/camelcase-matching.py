class Solution(object):
    def camelMatch(self, queries, pattern):
        answer = []

        for query in queries:
            j = 0
            valid = True

            for ch in query:
                if j < len(pattern) and ch == pattern[j]:
                    j += 1
                elif ch.isupper():
                    valid = False
                    break

            if j != len(pattern):
                valid = False

            answer.append(valid)

        return answer