class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False

        # Check if this is a leaf
        if root.left is None and root.right is None:
            return root.val == targetSum

        # Check left and right subtrees
        remaining = targetSum - root.val

        return (self.hasPathSum(root.left, remaining) or
                self.hasPathSum(root.right, remaining))