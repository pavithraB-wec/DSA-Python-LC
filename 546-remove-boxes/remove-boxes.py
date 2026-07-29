class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        memo = {}

        def dp(l, r, k):
            if l > r:
                return 0

            if (l, r, k) in memo:
                return memo[(l, r, k)]

            rr = r
            kk = k

            while rr > l and boxes[rr] == boxes[rr - 1]:
                rr -= 1
                kk += 1

            res = dp(l, rr - 1, 0) + (kk + 1) * (kk + 1)

            for i in range(l, rr):
                if boxes[i] == boxes[rr]:
                    res = max(res,
                              dp(l, i, kk + 1) +
                              dp(i + 1, rr - 1, 0))

            memo[(l, r, k)] = res
            return res

        return dp(0, len(boxes) - 1, 0)