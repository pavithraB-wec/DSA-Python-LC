from collections import deque

class Solution(object):
    def kSimilarity(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if s1 == s2:
            return 0

        queue = deque([(s1, 0)])
        visited = set([s1])

        while queue:
            curr, steps = queue.popleft()

            # Find first mismatch
            i = 0
            while curr[i] == s2[i]:
                i += 1

            curr_list = list(curr)

            for j in range(i + 1, len(curr)):
                if curr_list[j] == s2[i] and curr_list[j] != s2[j]:
                    nxt = curr_list[:]
                    nxt[i], nxt[j] = nxt[j], nxt[i]
                    nxt = "".join(nxt)

                    if nxt == s2:
                        return steps + 1

                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append((nxt, steps + 1))