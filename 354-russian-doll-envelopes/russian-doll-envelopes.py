class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        tails = []

        for _, h in envelopes:
            left, right = 0, len(tails)

            while left < right:
                mid = (left + right) // 2
                if tails[mid] < h:
                    left = mid + 1
                else:
                    right = mid

            if left == len(tails):
                tails.append(h)
            else:
                tails[left] = h

        return len(tails)