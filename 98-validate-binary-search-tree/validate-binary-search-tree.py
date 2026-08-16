class Solution(object):
    def isValidBST(self, root):

        def check(node, low, high):
            if not node:
                return True

            if node.val <= low or node.val >= high:
                return False

            return (check(node.left, low, node.val) and
                    check(node.right, node.val, high))

        return check(root, float('-inf'), float('inf'))