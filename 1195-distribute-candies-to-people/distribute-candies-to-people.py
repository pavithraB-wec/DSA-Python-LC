class Solution(object):
    def distributeCandies(self, candies, num_people):
        answer = [0] * num_people

        i = 0
        give = 1

        while candies > 0:
            amount = min(give, candies)

            answer[i % num_people] += amount
            candies -= amount

            give += 1
            i += 1

        return answer