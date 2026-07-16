# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        pos = {x: i for i, x in enumerate(postorder)}

        def build(preL, preR, postL, postR):
            if preL > preR:
                return None

            root = TreeNode(preorder[preL])

            if preL == preR:
                return root

            left_root = preorder[preL + 1]
            idx = pos[left_root]

            left_size = idx - postL + 1

            root.left = build(
                preL + 1,
                preL + left_size,
                postL,
                idx
            )

            root.right = build(
                preL + left_size + 1,
                preR,
                idx + 1,
                postR - 1
            )

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)