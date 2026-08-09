from functools import cmp_to_key

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = list(map(str, nums))

        def compare(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1

        nums.sort(key=cmp_to_key(compare))

        result = ''.join(nums)

        # Handle case like [0,0]
        return '0' if result[0] == '0' else result