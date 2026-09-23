class Solution(object):

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def gcdSum(self, nums):
        prefixGcd = []
        maximum = 0

        for num in nums:
            maximum = max(maximum, num)
            prefixGcd.append(self.gcd(num, maximum))

        prefixGcd.sort()

        answer = 0
        left = 0
        right = len(prefixGcd) - 1

        while left < right:
            answer += self.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return answer