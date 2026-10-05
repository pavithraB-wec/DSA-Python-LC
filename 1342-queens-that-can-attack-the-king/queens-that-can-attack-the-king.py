class Solution(object):
    def queensAttacktheKing(self, queens, king):
        queen_set = set()

        for q in queens:
            queen_set.add((q[0], q[1]))

        directions = [
            (-1, 0),   # up
            (1, 0),    # down
            (0, -1),   # left
            (0, 1),    # right
            (-1, -1),  # up-left
            (-1, 1),   # up-right
            (1, -1),   # down-left
            (1, 1)     # down-right
        ]

        answer = []

        for dx, dy in directions:
            x = king[0] + dx
            y = king[1] + dy

            while 0 <= x < 8 and 0 <= y < 8:
                if (x, y) in queen_set:
                    answer.append([x, y])
                    break

                x += dx
                y += dy

        return answer