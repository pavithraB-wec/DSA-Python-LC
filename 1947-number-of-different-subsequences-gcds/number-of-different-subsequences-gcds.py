class Solution(object):
    def countDifferentSubsequenceGCDs(self, nums):
        maximum = max(nums)

        present = [False] * (maximum + 1)

        for num in nums:
            present[num] = True

        answer = 0

        for g in range(1, maximum + 1):
            current_gcd = 0

            for multiple in range(g, maximum + 1, g):
                if present[multiple]:
                    if current_gcd == 0:
                        current_gcd = multiple
                    else:
                        a = current_gcd
                        b = multiple

                        while b:
                            a, b = b, a % b

                        current_gcd = a

                    if current_gcd == g:
                        answer += 1
                        break

        return answer