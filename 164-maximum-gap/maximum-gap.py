class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        if min_val == max_val:
            return 0

        bucket_size = max(1, (max_val - min_val) // (n - 1))
        bucket_count = ((max_val - min_val) // bucket_size) + 1

        buckets = [[None, None] for _ in range(bucket_count)]

        for num in nums:
            idx = (num - min_val) // bucket_size

            if buckets[idx][0] is None:
                buckets[idx][0] = num
                buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)

        ans = 0
        prev_max = min_val

        for bmin, bmax in buckets:
            if bmin is None:
                continue

            ans = max(ans, bmin - prev_max)
            prev_max = bmax

        return ans