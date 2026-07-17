class Solution(object):
    def prisonAfterNDays(self, cells, n):
        """
        :type cells: List[int]
        :type n: int
        :rtype: List[int]
        """
        seen = {}

        while n > 0:
            state = tuple(cells)

            if state in seen:
                cycle = seen[state] - n
                n %= cycle

            seen[state] = n

            if n > 0:
                n -= 1
                nxt = [0] * 8

                for i in range(1, 7):
                    if cells[i - 1] == cells[i + 1]:
                        nxt[i] = 1

                cells = nxt

        return cells