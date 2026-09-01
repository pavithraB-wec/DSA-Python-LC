class Solution(object):
    def binaryGap(self, n):
        last = -1
        position = 0
        answer = 0

        while n > 0:
            # Check if the current bit is 1
            if n & 1:
                if last != -1:
                    answer = max(answer, position - last)

                last = position

            n >>= 1
            position += 1

        return answer