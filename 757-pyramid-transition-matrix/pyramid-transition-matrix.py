from collections import defaultdict

class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        mp = defaultdict(list)

        for rule in allowed:
            mp[rule[:2]].append(rule[2])

        def dfs(row):
            if len(row) == 1:
                return True

            def build(idx, nxt):
                if idx == len(row) - 1:
                    return dfs(nxt)

                pair = row[idx:idx + 2]

                if pair not in mp:
                    return False

                for ch in mp[pair]:
                    if build(idx + 1, nxt + ch):
                        return True

                return False

            return build(0, "")

        return dfs(bottom)