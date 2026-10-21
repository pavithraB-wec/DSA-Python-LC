class Solution(object):
    def getAllElements(self, root1, root2):
        def inorder(root, result):
            if not root:
                return
            inorder(root.left, result)
            result.append(root.val)
            inorder(root.right, result)

        a, b = [], []
        inorder(root1, a)
        inorder(root2, b)

        i = j = 0
        result = []

        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1

        result.extend(a[i:])
        result.extend(b[j:])

        return result