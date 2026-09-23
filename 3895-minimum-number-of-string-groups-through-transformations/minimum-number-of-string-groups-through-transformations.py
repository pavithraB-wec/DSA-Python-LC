class Solution(object):

    def min_rotation(self, s):
        n = len(s)

        if n <= 1:
            return s

        ss = s + s
        i = 0
        j = 1
        k = 0

        while i < n and j < n and k < n:
            if ss[i + k] == ss[j + k]:
                k += 1
                continue

            if ss[i + k] > ss[j + k]:
                i = i + k + 1
                if i <= j:
                    i = j + 1
            else:
                j = j + k + 1
                if j <= i:
                    j = i + 1

            k = 0

        start = min(i, j)

        return ss[start:start + n]

    def minimumGroups(self, words):
        groups = set()

        for word in words:
            even = word[::2]
            odd = word[1::2]

            even = self.min_rotation(even)
            odd = self.min_rotation(odd)

            groups.add(even + "#" + odd)

        return len(groups)