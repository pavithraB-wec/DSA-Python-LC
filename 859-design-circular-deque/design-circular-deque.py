class MyCircularDeque(object):

    def __init__(self, k):
        self.queue = [0] * k
        self.capacity = k
        self.front = 0
        self.size = 0

    def insertFront(self, value):
        if self.isFull():
            return False

        self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        if self.isFull():
            return False

        rear = (self.front + self.size) % self.capacity
        self.queue[rear] = value
        self.size += 1
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False

        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False

        self.size -= 1
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1

        rear = (self.front + self.size - 1) % self.capacity
        return self.queue[rear]

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity