import heapq
from collections import defaultdict

class DualHeap(object):
    def __init__(self, k):
        self.small = []      # max heap (store negatives)
        self.large = []      # min heap
        self.delayed = defaultdict(int)
        self.k = k
        self.smallSize = 0
        self.largeSize = 0

    def prune(self, heap):
        while heap:
            num = -heap[0] if heap is self.small else heap[0]
            if self.delayed[num]:
                self.delayed[num] -= 1
                if self.delayed[num] == 0:
                    del self.delayed[num]
                heapq.heappop(heap)
            else:
                break

    def balance(self):
        if self.smallSize > self.largeSize + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
            self.smallSize -= 1
            self.largeSize += 1
            self.prune(self.small)
        elif self.smallSize < self.largeSize:
            heapq.heappush(self.small, -heapq.heappop(self.large))
            self.smallSize += 1
            self.largeSize -= 1
            self.prune(self.large)

    def insert(self, num):
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.smallSize += 1
        else:
            heapq.heappush(self.large, num)
            self.largeSize += 1
        self.balance()

    def erase(self, num):
        self.delayed[num] += 1

        if num <= -self.small[0]:
            self.smallSize -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.largeSize -= 1
            if self.large and num == self.large[0]:
                self.prune(self.large)

        self.balance()

    def median(self):
        if self.k % 2:
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        dh = DualHeap(k)

        for i in range(k):
            dh.insert(nums[i])

        ans = [dh.median()]

        for i in range(k, len(nums)):
            dh.insert(nums[i])
            dh.erase(nums[i - k])
            ans.append(dh.median())

        return ans