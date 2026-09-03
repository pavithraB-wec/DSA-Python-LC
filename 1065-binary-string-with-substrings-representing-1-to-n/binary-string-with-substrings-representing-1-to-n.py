class Solution(object):
    def queryString(self, s, n):
        # Numbers with more than 10 bits are at least 512.
        # Since s has length <= 1000, checking numbers individually
        # is practical only for a bounded range.
        
        # Check numbers from 1 to 10 directly
        for x in range(1, min(n, 10) + 1):
            if bin(x)[2:] not in s:
                return False

        # For larger numbers, check each binary length separately.
        max_bits = len(bin(n)) - 2

        for bits in range(4, max_bits + 1):
            if bits > len(s):
                return False

            start = 1 << (bits - 1)
            end = min(n, (1 << bits) - 1)

            # There are only len(s)-bits+1 substrings of this length.
            # If more numbers are required than possible substrings,
            # it is impossible.
            if end - start + 1 > len(s) - bits + 1:
                return False

            for x in range(start, end + 1):
                if bin(x)[2:] not in s:
                    return False

        return True