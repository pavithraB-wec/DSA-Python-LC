class Solution(object):
    def maxLength(self, arr):
        # Remove strings that already contain duplicate characters
        valid = []

        for s in arr:
            if len(set(s)) == len(s):
                valid.append(set(s))

        self.ans = 0

        def backtrack(index, used):
            self.ans = max(self.ans, len(used))

            for i in range(index, len(valid)):
                if not (used & valid[i]):
                    backtrack(i + 1, used | valid[i])

        backtrack(0, set())

        return self.ans