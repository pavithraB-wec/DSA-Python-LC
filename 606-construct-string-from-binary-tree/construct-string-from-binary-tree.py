class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        res = str(root.val)

        if root.left or root.right:
            res += "(" + self.tree2str(root.left) + ")"

        if root.right:
            res += "(" + self.tree2str(root.right) + ")"

        return res