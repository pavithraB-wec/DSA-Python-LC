class Solution(object):
    def removeDuplicateLetters(self, s):
        last = {}

        for i in range(len(s)):
            last[s[i]] = i

        stack = []
        seen = set()

        for i in range(len(s)):
            ch = s[i]

            if ch in seen:
                continue

            while stack and ch < stack[-1] and last[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)