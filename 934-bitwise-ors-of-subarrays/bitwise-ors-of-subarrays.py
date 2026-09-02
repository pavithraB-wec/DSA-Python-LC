class Solution(object):
    def subarrayBitwiseORs(self, arr):
        all_ors = set()
        current = set()

        for x in arr:
            new = set()

            # Start a new subarray
            new.add(x)

            # Extend previous subarrays
            for v in current:
                new.add(v | x)

            current = new
            all_ors.update(current)

        return len(all_ors)