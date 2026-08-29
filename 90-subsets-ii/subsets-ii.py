class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        result = []

        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                # Skip duplicates at the same level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result