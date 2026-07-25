class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx

        if tx == sx and ty == sy:
            return True

        if tx == sx:
            return ty >= sy and (ty - sy) % sx == 0

        if ty == sy:
            return tx >= sx and (tx - sx) % sy == 0

        return False