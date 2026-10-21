class Solution(object):
    def sortedListToBST(self, head):
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        def build(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(nums) - 1)