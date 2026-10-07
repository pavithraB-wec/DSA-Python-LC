class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atMost(k):
            count = {}
            left = 0
            answer = 0

            for right in range(len(nums)):
                count[nums[right]] = count.get(nums[right], 0) + 1

                while len(count) > k:
                    count[nums[left]] -= 1

                    if count[nums[left]] == 0:
                        del count[nums[left]]

                    left += 1

                answer += right - left + 1

            return answer

        return atMost(k) - atMost(k - 1)