class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        MOD = 1337

        def modPow(x, n):
            result = 1
            x %= MOD

            while n > 0:
                if n & 1:
                    result = (result * x) % MOD
                x = (x * x) % MOD
                n >>= 1

            return result

        result = 1

        for digit in b:
            result = (modPow(result, 10) * modPow(a, digit)) % MOD

        return result