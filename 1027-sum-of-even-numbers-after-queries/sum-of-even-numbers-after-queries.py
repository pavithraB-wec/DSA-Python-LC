class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        evenSum = 0

        for num in nums:
            if num % 2 == 0:
                evenSum += num

        answer = []

        for val, index in queries:
            if nums[index] % 2 == 0:
                evenSum -= nums[index]

            nums[index] += val

            if nums[index] % 2 == 0:
                evenSum += nums[index]

            answer.append(evenSum)

        return answer