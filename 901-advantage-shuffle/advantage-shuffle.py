class Solution(object):
    def advantageCount(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        n = len(nums1)

        nums2_sorted = sorted((num, i) for i, num in enumerate(nums2))

        ans = [0] * n
        left = 0
        right = n - 1

        for num in nums1:
            if num > nums2_sorted[left][0]:
                ans[nums2_sorted[left][1]] = num
                left += 1
            else:
                ans[nums2_sorted[right][1]] = num
                right -= 1

        return ans