class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        my_dist = abs(target[0]) + abs(target[1])

        for x, y in ghosts:
            ghost_dist = abs(x - target[0]) + abs(y - target[1])

            if ghost_dist <= my_dist:
                return False

        return True