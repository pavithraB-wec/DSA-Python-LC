class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        point_set = set((x, y) for x, y in points)
        ans = float('inf')

        n = len(points)

        for i in range(n):
            x1, y1 = points[i]

            for j in range(i + 1, n):
                x2, y2 = points[j]

                # Must be diagonal corners
                if x1 != x2 and y1 != y2:
                    if (x1, y2) in point_set and (x2, y1) in point_set:
                        area = abs(x1 - x2) * abs(y1 - y2)
                        ans = min(ans, area)

        return 0 if ans == float('inf') else ans