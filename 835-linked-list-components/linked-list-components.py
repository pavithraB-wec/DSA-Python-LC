class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: ListNode
        :type nums: List[int]
        :rtype: int
        """
        values = set(nums)
        count = 0

        while head:
            if head.val in values and (head.next is None or head.next.val not in values):
                count += 1
            head = head.next

        return count