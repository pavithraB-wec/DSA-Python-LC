class Solution(object):
    def findTheLongestSubstring(self, s):
        first = {0: -1}

        mask = 0
        answer = 0

        vowels = {
            'a': 1,
            'e': 2,
            'i': 4,
            'o': 8,
            'u': 16
        }

        for i in range(len(s)):
            if s[i] in vowels:
                mask ^= vowels[s[i]]

            if mask in first:
                answer = max(answer, i - first[mask])
            else:
                first[mask] = i

        return answer