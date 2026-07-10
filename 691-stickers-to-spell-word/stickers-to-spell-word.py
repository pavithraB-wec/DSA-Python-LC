from collections import Counter

class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        sticker_counts = [Counter(sticker) for sticker in stickers]
        memo = {"": 0}

        def dfs(remain):
            if remain in memo:
                return memo[remain]

            target_count = Counter(remain)
            ans = float('inf')

            for sticker in sticker_counts:
                # Optimization: skip stickers that don't contain
                # the first needed character
                if remain[0] not in sticker:
                    continue

                new_remain = ""

                for ch in target_count:
                    if target_count[ch] > sticker[ch]:
                        new_remain += ch * (target_count[ch] - sticker[ch])

                temp = dfs(new_remain)
                if temp != -1:
                    ans = min(ans, temp + 1)

            memo[remain] = -1 if ans == float('inf') else ans
            return memo[remain]

        return dfs(target)