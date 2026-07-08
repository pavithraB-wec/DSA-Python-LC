class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        slots = 1

        for node in preorder.split(','):
            # Every node occupies one slot
            slots -= 1

            if slots < 0:
                return False

            # Non-null node creates two new slots
            if node != '#':
                slots += 2

        return slots == 0