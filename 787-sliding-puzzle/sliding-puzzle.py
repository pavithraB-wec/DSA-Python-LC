class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        start = ''.join(str(x) for row in board for x in row)
        target = "123450"

        if start == target:
            return 0

        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        queue = [(start, 0)]
        visited = set([start])
        front = 0

        while front < len(queue):
            state, steps = queue[front]
            front += 1

            zero = state.index('0')

            for nxt in neighbors[zero]:
                arr = list(state)
                arr[zero], arr[nxt] = arr[nxt], arr[zero]
                new_state = ''.join(arr)

                if new_state == target:
                    return steps + 1

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, steps + 1))

        return -1