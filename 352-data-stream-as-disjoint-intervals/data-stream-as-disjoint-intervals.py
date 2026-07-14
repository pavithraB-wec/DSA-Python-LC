class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = set()

    def addNum(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.nums.add(value)

    def getIntervals(self):
        """
        :rtype: List[List[int]]
        """
        if not self.nums:
            return []

        arr = sorted(self.nums)
        result = []

        start = end = arr[0]

        for num in arr[1:]:
            if num == end + 1:
                end = num
            else:
                result.append([start, end])
                start = end = num

        result.append([start, end])

        return result