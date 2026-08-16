class Solution(object):
    def recoverTree(self, root):
        stack = []
        current = root

        first = None
        second = None
        prev = None

        while stack or current:

            # Go left
            while current:
                stack.append(current)
                current = current.left

            # Visit node
            current = stack.pop()

            # Find incorrect order
            if prev and prev.val > current.val:
                if first is None:
                    first = prev

                second = current

            prev = current

            # Go right
            current = current.right

        # Swap the values
        first.val, second.val = second.val, first.val