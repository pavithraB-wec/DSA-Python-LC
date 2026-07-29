class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        buckets = [0] * k

        def backtrack(index):
            if index == len(nums):
                return True

            for i in range(k):
                if buckets[i] + nums[index] <= target:
                    buckets[i] += nums[index]

                    if backtrack(index + 1):
                        return True

                    buckets[i] -= nums[index]

                if buckets[i] == 0:
                    break

            return False

        return backtrack(0)