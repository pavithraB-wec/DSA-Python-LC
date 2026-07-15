class Solution(object):
    def findReplaceString(self, s, indices, sources, targets):
        replace = {}

        for idx, src, tgt in zip(indices, sources, targets):
            if s.startswith(src, idx):
                replace[idx] = (src, tgt)

        res = []
        i = 0

        while i < len(s):
            if i in replace:
                src, tgt = replace[i]
                res.append(tgt)
                i += len(src)
            else:
                res.append(s[i])
                i += 1

        return "".join(res)