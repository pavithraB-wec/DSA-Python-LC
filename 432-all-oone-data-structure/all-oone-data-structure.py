class Node(object):
    def __init__(self, cnt):
        self.cnt = cnt
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne(object):

    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.keyNode = {}

    def _insertAfter(self, prev, node):
        node.next = prev.next
        node.prev = prev
        prev.next.prev = node
        prev.next = node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key):
        if key not in self.keyNode:
            if self.head.next == self.tail or self.head.next.cnt != 1:
                node = Node(1)
                self._insertAfter(self.head, node)
            else:
                node = self.head.next

            node.keys.add(key)
            self.keyNode[key] = node

        else:
            node = self.keyNode[key]
            nxt = node.next

            if nxt == self.tail or nxt.cnt != node.cnt + 1:
                newNode = Node(node.cnt + 1)
                self._insertAfter(node, newNode)
                nxt = newNode

            nxt.keys.add(key)
            self.keyNode[key] = nxt

            node.keys.remove(key)
            if not node.keys:
                self._remove(node)

    def dec(self, key):
        if key not in self.keyNode:
            return

        node = self.keyNode[key]

        if node.cnt == 1:
            del self.keyNode[key]
        else:
            prev = node.prev

            if prev == self.head or prev.cnt != node.cnt - 1:
                newNode = Node(node.cnt - 1)
                self._insertAfter(prev, newNode)
                prev = newNode

            prev.keys.add(key)
            self.keyNode[key] = prev

        node.keys.remove(key)

        if not node.keys:
            self._remove(node)

    def getMaxKey(self):
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))