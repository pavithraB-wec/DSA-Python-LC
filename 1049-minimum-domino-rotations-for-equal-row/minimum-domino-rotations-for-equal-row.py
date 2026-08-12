class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        def check(x):
            rotate_top = 0
            rotate_bottom = 0

            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')

                if tops[i] != x:
                    rotate_top += 1

                if bottoms[i] != x:
                    rotate_bottom += 1

            return min(rotate_top, rotate_bottom)

        answer = min(check(tops[0]), check(bottoms[0]))

        return -1 if answer == float('inf') else answer