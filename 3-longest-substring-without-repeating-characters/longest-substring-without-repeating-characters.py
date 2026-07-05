class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in last_seen and last_seen[s[right]] >= left:
                left = last_seen[s[right]] + 1

            last_seen[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length