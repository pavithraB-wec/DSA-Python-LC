class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head

        # Find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Compare both halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True