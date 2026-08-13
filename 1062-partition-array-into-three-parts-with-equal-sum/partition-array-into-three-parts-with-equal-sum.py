class Solution(object):
    def canThreePartsEqualSum(self, arr):
        total = sum(arr)

        # Total must be divisible by 3
        if total % 3 != 0:
            return False

        target = total // 3
        current = 0
        parts = 0

        for num in arr:
            current += num

            if current == target:
                parts += 1
                current = 0

        return parts >= 3