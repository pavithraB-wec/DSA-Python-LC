from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(string):
            balance = 0
            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    if balance == 0:
                        return False
                    balance -= 1
            return balance == 0

        result = []
        visited = set([s])
        queue = deque([s])
        found = False

        while queue:
            curr = queue.popleft()

            if isValid(curr):
                result.append(curr)
                found = True

            if found:
                continue

            for i in range(len(curr)):
                if curr[i] not in "()":
                    continue

                nxt = curr[:i] + curr[i + 1:]

                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)

        return result