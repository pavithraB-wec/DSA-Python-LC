class Solution(object):
    def pancakeSort(self, arr):
        result = []

        for size in range(len(arr), 1, -1):

            # Find the index of the largest element
            # in the unsorted portion
            max_index = arr.index(size, 0, size)

            # Already in correct position
            if max_index == size - 1:
                continue

            # Move largest element to the front
            if max_index != 0:
                arr[:max_index + 1] = reversed(arr[:max_index + 1])
                result.append(max_index + 1)

            # Move largest element to its final position
            arr[:size] = reversed(arr[:size])
            result.append(size)

        return result