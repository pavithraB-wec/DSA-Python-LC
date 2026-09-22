class Solution(object):
    def countPairs(self, root, distance):
        self.answer = 0

        def dfs(node):
            if not node:
                return []

            # Leaf node
            if not node.left and not node.right:
                return [1]

            left = dfs(node.left)
            right = dfs(node.right)

            # Check pairs whose LCA is this node
            for d1 in left:
                for d2 in right:
                    if d1 + d2 <= distance:
                        self.answer += 1

            # Return distances to leaves for the parent
            result = []

            for d in left:
                if d + 1 < distance:
                    result.append(d + 1)

            for d in right:
                if d + 1 < distance:
                    result.append(d + 1)

            return result

        dfs(root)

        return self.answer