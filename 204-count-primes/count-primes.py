class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        isPrime = [True] * n
        isPrime[0] = False
        isPrime[1] = False

        p = 2
        while p * p < n:
            if isPrime[p]:
                for multiple in range(p * p, n, p):
                    isPrime[multiple] = False
            p += 1

        return sum(isPrime)