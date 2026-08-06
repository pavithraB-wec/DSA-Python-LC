class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 1:
            ans = s
            for i in range(1, len(s)):
                rotation = s[i:] + s[:i]
                if rotation < ans:
                    ans = rotation
            return ans

        return "".join(sorted(s))