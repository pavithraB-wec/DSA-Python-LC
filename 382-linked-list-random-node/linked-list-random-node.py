import random

class Solution(object):

    def __init__(self, head):
        """
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        :rtype: int
        """
        result = self.head.val
        node = self.head.next
        i = 2

        while node:
            if random.randint(1, i) == 1:
                result = node.val
            node = node.next
            i += 1

        return result