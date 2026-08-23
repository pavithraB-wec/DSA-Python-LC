class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0

        def getHeight(node):
            height = 0

            while node:
                height += 1
                node = node.left

            return height

        left_height = getHeight(root.left)
        right_height = getHeight(root.right)

        if left_height == right_height:
            # Left subtree is a perfect binary tree
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # Right subtree is a perfect binary tree
            return (1 << right_height) + self.countNodes(root.left)