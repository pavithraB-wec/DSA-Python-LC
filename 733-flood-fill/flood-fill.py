from collections import deque

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        m = len(image)
        n = len(image[0])

        original = image[sr][sc]

        # Already the target color
        if original == color:
            return image

        queue = deque([(sr, sc)])
        image[sr][sc] = color

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    if image[nr][nc] == original:
                        image[nr][nc] = color
                        queue.append((nr, nc))

        return image