class Solution(object):
    def countConsistentStrings(self, allowed, words):
        allowed_set = set(allowed)
        answer = 0

        for word in words:
            good = True

            for ch in word:
                if ch not in allowed_set:
                    good = False
                    break

            if good:
                answer += 1

        return answer