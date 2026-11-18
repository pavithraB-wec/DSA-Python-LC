class Solution(object):
    def rearrangeArray(self, nums):
        n = len(nums)
        result = [0] * n

        pos = 0
        neg = 1

        for num in nums:
            if num > 0:
                result[pos] = num
                pos += 2
            else:
                result[neg] = num
                neg += 2

        return result