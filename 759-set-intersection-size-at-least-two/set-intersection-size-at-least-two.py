class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: (x[1], -x[0]))

        a = -1   # second last chosen
        b = -1   # last chosen
        ans = 0

        for start, end in intervals:
            if start <= a:
                # already have two numbers
                continue
            elif start <= b:
                # have only one number
                ans += 1
                a = b
                b = end
            else:
                # have no numbers
                ans += 2
                a = end - 1
                b = end

        return ans