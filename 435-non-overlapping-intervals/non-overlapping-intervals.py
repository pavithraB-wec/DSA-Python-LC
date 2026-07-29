class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])

        end = intervals[0][1]
        remove = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                remove += 1
            else:
                end = intervals[i][1]

        return remove