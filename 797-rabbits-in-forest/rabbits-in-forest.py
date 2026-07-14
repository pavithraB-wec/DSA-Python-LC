from collections import Counter

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        count = Counter(answers)
        total = 0

        for x, freq in count.items():
            group = x + 1
            groups = (freq + group - 1) // group   # Ceiling division
            total += groups * group

        return total