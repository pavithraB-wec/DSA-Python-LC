class Solution(object):
    def numberOfSubarrays(self, nums, k):
        count = {0: 1}

        odd_count = 0
        answer = 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1

            if odd_count - k in count:
                answer += count[odd_count - k]

            count[odd_count] = count.get(odd_count, 0) + 1

        return answer