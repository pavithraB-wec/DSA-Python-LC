class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0:
            return 1

        mask = 0
        temp = n

        while temp:
            mask = (mask << 1) | 1
            temp >>= 1

        return n ^ mask