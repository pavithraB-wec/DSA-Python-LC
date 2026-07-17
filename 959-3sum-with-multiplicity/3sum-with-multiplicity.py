from collections import Counter

class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        count = Counter(arr)
        ans = 0

        nums = sorted(count.keys())

        for i in range(len(nums)):
            x = nums[i]
            for j in range(i, len(nums)):
                y = nums[j]
                z = target - x - y

                if z < y or z not in count:
                    continue

                if x == y == z:
                    c = count[x]
                    ans += c * (c - 1) * (c - 2) // 6

                elif x == y != z:
                    c = count[x]
                    ans += c * (c - 1) // 2 * count[z]

                elif x != y == z:
                    c = count[y]
                    ans += count[x] * c * (c - 1) // 2

                else:
                    ans += count[x] * count[y] * count[z]

        return ans % MOD