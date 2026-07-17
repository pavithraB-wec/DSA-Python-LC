from collections import defaultdict
from bisect import bisect_right

class TopVotedCandidate(object):

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.times = times
        self.leaders = []

        count = defaultdict(int)
        leader = -1

        for p in persons:
            count[p] += 1
            if leader == -1 or count[p] >= count[leader]:
                leader = p
            self.leaders.append(leader)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        idx = bisect_right(self.times, t) - 1
        return self.leaders[idx]