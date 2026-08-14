class Solution:
    def prevPermOpt1(self, arr):
        n = len(arr)

        # Step 1: Find the rightmost position where arr[i] > arr[i + 1]
        i = n - 2

        while i >= 0 and arr[i] <= arr[i + 1]:
            i -= 1

        # No smaller permutation possible
        if i < 0:
            return arr

        # Step 2: Find the largest value smaller than arr[i]
        # Start from the end to handle duplicates correctly
        j = n - 1

        while arr[j] >= arr[i] or (j > 0 and arr[j] == arr[j - 1]):
            j -= 1

        # Step 3: Swap
        arr[i], arr[j] = arr[j], arr[i]

        return arr