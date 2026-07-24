class Solution(object):
    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        num = int(n)
        max_m = num.bit_length() - 1

        for m in range(max_m, 1, -1):
            left = 2
            right = int(num ** (1.0 / m)) + 1

            while left <= right:
                mid = (left + right) // 2

                total = 1
                curr = 1

                for _ in range(m):
                    curr *= mid
                    total += curr
                    if total > num:
                        break

                if total == num:
                    return str(mid)
                elif total < num:
                    left = mid + 1
                else:
                    right = mid - 1

        return str(num - 1)