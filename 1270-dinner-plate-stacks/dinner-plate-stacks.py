import heapq

class DinnerPlates(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        self.available = []
        self.right = -1

    def push(self, val):
        # Remove invalid/full stack indices from heap
        while self.available:
            index = self.available[0]
            if index < len(self.stacks) and len(self.stacks[index]) < self.capacity:
                break
            heapq.heappop(self.available)

        # Use existing available stack
        if self.available:
            index = heapq.heappop(self.available)
            self.stacks[index].append(val)
            self.right = max(self.right, index)
            return

        # Create a new stack
        self.stacks.append([val])
        self.right = len(self.stacks) - 1

        # If it still has space, add it to available
        if len(self.stacks[self.right]) < self.capacity:
            heapq.heappush(self.available, self.right)

    def popAtStack(self, index):
        if index < 0 or index >= len(self.stacks):
            return -1

        if not self.stacks[index]:
            return -1

        value = self.stacks[index].pop()

        # This stack now has space
        heapq.heappush(self.available, index)

        # Update rightmost non-empty stack
        while self.right >= 0 and not self.stacks[self.right]:
            self.right -= 1

        return value

    def pop(self):
        # Find rightmost non-empty stack
        while self.right >= 0 and not self.stacks[self.right]:
            self.right -= 1

        if self.right < 0:
            return -1

        value = self.stacks[self.right].pop()

        # Stack now has space
        heapq.heappush(self.available, self.right)

        # Move right pointer if this stack became empty
        while self.right >= 0 and not self.stacks[self.right]:
            self.right -= 1

        return value