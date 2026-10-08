class Solution(object):
    def numPairsDivisibleBy60(self, time):
        count = [0] * 60
        answer = 0

        for t in time:
            remainder = t % 60
            needed = (60 - remainder) % 60

            answer += count[needed]
            count[remainder] += 1

        return answer