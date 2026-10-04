class Solution(object):
    def numSteps(self, s):
        steps = 0
        carry = 0

        for i in range(len(s) - 1, 0, -1):
            bit = int(s[i]) + carry

            if bit == 0:
                # Even: divide by 2
                steps += 1

            elif bit == 1:
                # Odd: add 1, then divide by 2
                steps += 2
                carry = 1

            else:
                # bit == 2
                # Becomes 0 after carrying
                steps += 1

        return steps + carry