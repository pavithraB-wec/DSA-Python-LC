class Solution(object):
    def minDeletionSize(self, strs):
        n = len(strs)
        m = len(strs[0])

        # sorted_pair[i] means strs[i] < strs[i+1]
        # has already been determined by previous columns.
        sorted_pair = [False] * (n - 1)

        deletions = 0

        for col in range(m):

            # Check whether keeping this column causes a problem
            bad = False

            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            # This column must be deleted
            if bad:
                deletions += 1
                continue

            # This column is safe.
            # Mark pairs that are now strictly ordered.
            for i in range(n - 1):
                if not sorted_pair[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pair[i] = True

        return deletions