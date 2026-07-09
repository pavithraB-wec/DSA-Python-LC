class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        head = 2
        num = 1
        count = 1  # One '1' in the initial string

        while len(s) < n:
            repeat = s[head]

            for _ in range(repeat):
                s.append(num)
                if num == 1 and len(s) <= n:
                    count += 1

            num = 2 if num == 1 else 1
            head += 1

        return count