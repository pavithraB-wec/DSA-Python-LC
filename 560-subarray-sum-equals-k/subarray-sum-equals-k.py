class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = {0: 1}
        curr_sum = 0
        count = 0

        for num in nums:
            curr_sum += num

            if curr_sum - k in prefix:
                count += prefix[curr_sum - k]

            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

        return count