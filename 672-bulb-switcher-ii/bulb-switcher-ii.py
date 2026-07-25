class Solution(object):
    def flipLights(self, n, presses):
        """
        :type n: int
        :type presses: int
        :rtype: int
        """
        if presses == 0:
            return 1

        if n == 1:
            return 2

        if n == 2:
            if presses == 1:
                return 3
            return 4

        if presses == 1:
            return 4
        elif presses == 2:
            return 7
        else:
            return 8