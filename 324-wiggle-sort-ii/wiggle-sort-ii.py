class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """
        arr = sorted(nums)
        n = len(nums)

        mid = (n + 1) // 2

        left = arr[:mid][::-1]
        right = arr[mid:][::-1]

        i = 0

        for x in left:
            nums[i] = x
            i += 2

        i = 1

        for x in right:
            nums[i] = x
            i += 2