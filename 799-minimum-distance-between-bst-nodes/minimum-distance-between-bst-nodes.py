class Solution(object):
    def minDiffInBST(self, root):
        self.prev = None
        self.answer = float('inf')

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if self.prev is not None:
                self.answer = min(
                    self.answer,
                    node.val - self.prev
                )

            self.prev = node.val

            inorder(node.right)

        inorder(root)

        return self.answer