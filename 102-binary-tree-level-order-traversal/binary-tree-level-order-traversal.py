from collections import deque

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result