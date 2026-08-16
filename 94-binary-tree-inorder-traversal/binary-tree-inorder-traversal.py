class Solution(object):
    def inorderTraversal(self, root):
        result = []
        stack = []
        current = root

        while current or stack:
            
            # Go as far left as possible
            while current:
                stack.append(current)
                current = current.left

            # Process the node
            current = stack.pop()
            result.append(current.val)

            # Move to right subtree
            current = current.right

        return result