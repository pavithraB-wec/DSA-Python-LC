class Solution(object):
    def closestNodes(self, root, queries):
        import bisect

        nums = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)

        inorder(root)

        answer = []

        for q in queries:
            i = bisect.bisect_left(nums, q)

            if i < len(nums) and nums[i] == q:
                answer.append([q, q])
            else:
                mini = nums[i - 1] if i > 0 else -1
                maxi = nums[i] if i < len(nums) else -1
                answer.append([mini, maxi])

        return answer