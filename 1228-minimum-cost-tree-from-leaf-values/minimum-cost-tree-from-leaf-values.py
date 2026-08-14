class Solution:
    def mctFromLeafValues(self, arr):
        stack = [float('inf')]
        total = 0

        for x in arr:
            # Remove smaller values
            while stack[-1] <= x:
                mid = stack.pop()

                # Multiply with the smaller neighbor
                total += mid * min(stack[-1], x)

            stack.append(x)

        # Process remaining elements
        while len(stack) > 2:
            mid = stack.pop()
            total += mid * stack[-1]

        return total