import math

class Solution(object):
    def subarrayMajority(self, nums, queries):
        n = len(nums)

        # Coordinate compression
        values = sorted(set(nums))
        mapping = {v: i for i, v in enumerate(values)}
        arr = [mapping[x] for x in nums]

        size_values = len(values)

        # Segment Tree
        size = 1
        while size < size_values:
            size *= 2

        tree = [0] * (2 * size)
        freq = [0] * size_values

        def update(x, delta):
            freq[x] += delta

            p = size + x
            tree[p] = freq[x]
            p //= 2

            while p:
                new_val = max(tree[2 * p], tree[2 * p + 1])

                if tree[p] == new_val:
                    break

                tree[p] = new_val
                p //= 2

        def get_answer():
            max_freq = tree[1]

            if max_freq == 0:
                return -1

            # Find the smallest value with maximum frequency
            p = 1

            while p < size:
                if tree[2 * p] == max_freq:
                    p = 2 * p
                else:
                    p = 2 * p + 1

            return values[p - size]

        # Mo's Algorithm
        block = max(1, int(n / math.sqrt(len(queries))))

        indexed_queries = []
        for i, (l, r, threshold) in enumerate(queries):
            indexed_queries.append((l, r, threshold, i))

        indexed_queries.sort(
            key=lambda q: (
                q[0] // block,
                q[1] if (q[0] // block) % 2 == 0 else -q[1]
            )
        )

        ans = [-1] * len(queries)

        current_l = 0
        current_r = -1

        for l, r, threshold, idx in indexed_queries:

            while current_l > l:
                current_l -= 1
                update(arr[current_l], 1)

            while current_r < r:
                current_r += 1
                update(arr[current_r], 1)

            while current_l < l:
                update(arr[current_l], -1)
                current_l += 1

            while current_r > r:
                update(arr[current_r], -1)
                current_r -= 1

            if tree[1] >= threshold:
                ans[idx] = get_answer()

        return ans