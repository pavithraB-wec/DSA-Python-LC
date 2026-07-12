from collections import defaultdict

class Solution(object):
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                g = self.gcd(dx, dy)
                dx //= g
                dy //= g

                # Normalize slope
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1

                slopes[(dx, dy)] += 1

            current = 1
            for cnt in slopes.values():
                current = max(current, cnt + 1)

            ans = max(ans, current)

        return ans