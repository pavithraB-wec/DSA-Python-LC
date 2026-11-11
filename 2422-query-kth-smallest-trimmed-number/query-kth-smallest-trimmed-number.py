class Solution(object):

    def smallestTrimmedNumbers(self, nums, queries):
        answer = []

        for k, trim in queries:
            arr = []

            for i in range(len(nums)):
                trimmed = nums[i][-trim:]
                arr.append((trimmed, i))

            arr.sort()

            answer.append(arr[k - 1][1])

        return answer