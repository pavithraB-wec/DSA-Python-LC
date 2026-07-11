class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        result = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])

            if i == end:
                result.append(end - start + 1)
                start = i + 1

        return result