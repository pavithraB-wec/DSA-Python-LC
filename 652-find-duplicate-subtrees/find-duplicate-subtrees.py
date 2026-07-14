from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        freq = defaultdict(int)
        result = []

        def dfs(node):
            if not node:
                return "#"

            serial = "{},{},{}".format(
                node.val,
                dfs(node.left),
                dfs(node.right)
            )

            freq[serial] += 1

            if freq[serial] == 2:
                result.append(node)

            return serial

        dfs(root)
        return result