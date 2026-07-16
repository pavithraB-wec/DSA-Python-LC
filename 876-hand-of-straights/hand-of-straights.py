from collections import Counter

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for x in sorted(count):
            while count[x] > 0:
                for i in range(groupSize):
                    if count[x + i] == 0:
                        return False
                    count[x + i] -= 1

        return True