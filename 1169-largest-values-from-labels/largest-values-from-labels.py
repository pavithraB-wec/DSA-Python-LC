from collections import defaultdict

class Solution:
    def largestValsFromLabels(self, values, labels, numWanted, useLimit):
        # Combine value and label
        items = list(zip(values, labels))

        # Sort by value from largest to smallest
        items.sort(reverse=True)

        used = defaultdict(int)
        total = 0
        count = 0

        for value, label in items:

            # Stop after selecting numWanted items
            if count == numWanted:
                break

            # Check label limit
            if used[label] < useLimit:
                total += value
                used[label] += 1
                count += 1

        return total