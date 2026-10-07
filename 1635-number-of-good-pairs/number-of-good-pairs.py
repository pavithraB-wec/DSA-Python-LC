class Solution(object):
    def numIdenticalPairs(self, nums):
        count = {}
        answer = 0

        for num in nums:
            if num in count:
                answer += count[num]

            count[num] = count.get(num, 0) + 1

        return answer