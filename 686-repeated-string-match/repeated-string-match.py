class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        repeated = a
        count = 1

        while len(repeated) < len(b):
            repeated += a
            count += 1

        if b in repeated:
            return count

        repeated += a
        if b in repeated:
            return count + 1

        return -1