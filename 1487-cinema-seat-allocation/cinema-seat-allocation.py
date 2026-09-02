class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = 0
            rows[row] |= 1 << (seat - 1)

        # Rows with no reservations can always fit 2 groups
        ans = (n - len(rows)) * 2

        # Seat blocks:
        # 2,3,4,5
        # 4,5,6,7
        # 6,7,8,9
        left = 0b000011110
        middle = 0b01111000
        right = 0b111100000

        for mask in rows.values():
            can_left = (mask & left) == 0
            can_middle = (mask & middle) == 0
            can_right = (mask & right) == 0

            if can_left and can_right:
                ans += 2
            elif can_left or can_middle or can_right:
                ans += 1

        return ans