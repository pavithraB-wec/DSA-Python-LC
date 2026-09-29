class Solution(object):
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        result = []
        total = rows * cols

        r = rStart
        c = cStart

        # Right, Down, Left, Up
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1, 0)
        ]

        step = 1
        direction = 0

        result.append([r, c])

        while len(result) < total:
            for _ in range(2):
                dr, dc = directions[direction]

                for _ in range(step):
                    r += dr
                    c += dc

                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])

                        if len(result) == total:
                            return result

                direction = (direction + 1) % 4

            step += 1

        return result