class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        last = {}

        # Last occurrence of each character
        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        seen = set()

        for i, ch in enumerate(s):

            if ch in seen:
                continue

            while stack and ch < stack[-1] and last[stack[-1]] > i:
                seen.remove(stack.pop())

            stack.append(ch)
            seen.add(ch)

        return "".join(stack)