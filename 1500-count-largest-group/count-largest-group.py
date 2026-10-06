class Solution(object):
    def countLargestGroup(self, n):
        count = [0] * 37

        for num in range(1, n + 1):
            x = num
            digit_sum = 0

            while x > 0:
                digit_sum += x % 10
                x //= 10

            count[digit_sum] += 1

        maximum = max(count)
        answer = 0

        for value in count:
            if value == maximum:
                answer += 1

        return answer