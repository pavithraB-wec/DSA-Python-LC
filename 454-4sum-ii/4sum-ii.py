from collections import defaultdict

class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        sums = defaultdict(int)

        # Store sums of nums1 and nums2
        for a in nums1:
            for b in nums2:
                sums[a + b] += 1

        count = 0

        # Find complementary sums
        for c in nums3:
            for d in nums4:
                count += sums[-(c + d)]

        return count