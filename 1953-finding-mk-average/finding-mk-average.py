from collections import deque

class MKAverage(object):

    def __init__(self, m, k):
        self.m = m
        self.k = k
        self.queue = deque()
        self.total = 0

        self.count = [0] * 100001
        self.sums = [0] * 100001

    def update(self, tree, index, delta):
        while index <= 100000:
            tree[index] += delta
            index += index & -index

    def query(self, tree, index):
        result = 0
        while index > 0:
            result += tree[index]
            index -= index & -index
        return result

    def findKth(self, k):
        index = 0
        bit = 65536

        while bit > 0:
            next_index = index + bit
            if next_index <= 100000 and self.count[next_index] < k:
                index = next_index
                k -= self.count[next_index]
            bit //= 2

        return index + 1

    def sumSmallest(self, k):
        if k == 0:
            return 0

        value = self.findKth(k)

        count_before = self.query(self.count, value - 1)
        sum_before = self.query(self.sums, value - 1)

        return sum_before + (k - count_before) * value

    def addElement(self, num):
        self.queue.append(num)
        self.total += num

        self.update(self.count, num, 1)
        self.update(self.sums, num, num)

        if len(self.queue) > self.m:
            old = self.queue.popleft()
            self.total -= old

            self.update(self.count, old, -1)
            self.update(self.sums, old, -old)

    def calculateMKAverage(self):
        if len(self.queue) < self.m:
            return -1

        smallest = self.sumSmallest(self.k)
        smallest_m_minus_k = self.sumSmallest(self.m - self.k)

        middle_sum = smallest_m_minus_k - smallest

        return middle_sum // (self.m - 2 * self.k)