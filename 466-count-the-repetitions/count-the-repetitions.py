class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        if n1 == 0:
            return 0

        index = 0
        count2 = 0
        recall = {}

        s1_count = 0

        while s1_count < n1:
            s1_count += 1

            for ch in s1:
                if ch == s2[index]:
                    index += 1
                    if index == len(s2):
                        count2 += 1
                        index = 0

            if index in recall:
                prev_s1, prev_count2 = recall[index]

                cycle_s1 = s1_count - prev_s1
                cycle_s2 = count2 - prev_count2

                remaining = n1 - s1_count

                cycles = remaining // cycle_s1

                count2 += cycles * cycle_s2
                s1_count += cycles * cycle_s1
            else:
                recall[index] = (s1_count, count2)

        return count2 // n2