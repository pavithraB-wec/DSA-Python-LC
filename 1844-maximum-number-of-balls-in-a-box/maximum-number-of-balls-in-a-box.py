class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        count = {}

        for num in range(lowLimit, highLimit + 1):
            x = num
            digit_sum = 0

            while x > 0:
                digit_sum += x % 10
                x //= 10

            count[digit_sum] = count.get(digit_sum, 0) + 1

        return max(count.values())