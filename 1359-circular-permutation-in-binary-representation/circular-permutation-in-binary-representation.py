class Solution(object):
    def circularPermutation(self, n, start):
        nums = []

        # Generate Gray Code sequence
        for i in range(1 << n):
            nums.append(i ^ (i >> 1))

        # Find start and rotate
        index = nums.index(start)

        return nums[index:] + nums[:index]