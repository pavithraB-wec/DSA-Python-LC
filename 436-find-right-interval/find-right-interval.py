import bisect

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))

        start_values = [x[0] for x in starts]

        ans = []

        for start, end in intervals:
            idx = bisect.bisect_left(start_values, end)

            if idx == len(starts):
                ans.append(-1)
            else:
                ans.append(starts[idx][1])

        return ans