class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math

        nums = [str(i) for i in range(1, n + 1)]
        k -= 1  # Convert to 0-based index
        ans = []

        for i in range(n, 0, -1):
            fact = math.factorial(i - 1)
            index = k // fact
            ans.append(nums.pop(index))
            k %= fact

        return "".join(ans)