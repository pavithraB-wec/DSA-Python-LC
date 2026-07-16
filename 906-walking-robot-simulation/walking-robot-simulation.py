class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        obstacle_set = set(map(tuple, obstacles))

        # North, East, South, West
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0

        x = y = 0
        ans = 0

        for cmd in commands:
            if cmd == -1:          # Turn right
                d = (d + 1) % 4
            elif cmd == -2:        # Turn left
                d = (d + 3) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(cmd):
                    nx = x + dx
                    ny = y + dy

                    if (nx, ny) in obstacle_set:
                        break

                    x, y = nx, ny
                    ans = max(ans, x * x + y * y)

        return ans