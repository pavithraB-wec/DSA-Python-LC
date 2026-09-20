class Solution(object):
    def subarraysDivByK(self, nums, k):
        count = {0: 1}

        remainder = 0
        answer = 0

        for num in nums:
            remainder = (remainder + num) % k

            if remainder in count:
                answer += count[remainder]

            count[remainder] = count.get(remainder, 0) + 1

        return answer