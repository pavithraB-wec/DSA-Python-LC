class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        if valueDiff < 0:
            return False

        bucket_size = valueDiff + 1
        buckets = {}

        def get_bucket_id(x):
            return x // bucket_size

        for i, num in enumerate(nums):
            bucket = get_bucket_id(num)

            if bucket in buckets:
                return True

            if (bucket - 1 in buckets and
                abs(num - buckets[bucket - 1]) <= valueDiff):
                return True

            if (bucket + 1 in buckets and
                abs(num - buckets[bucket + 1]) <= valueDiff):
                return True

            buckets[bucket] = num

            if i >= indexDiff:
                old_bucket = get_bucket_id(nums[i - indexDiff])
                del buckets[old_bucket]

        return False