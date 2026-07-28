class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = []

        for num in nums:
            left, right = 0, len(tails)

            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num

        return len(tails)