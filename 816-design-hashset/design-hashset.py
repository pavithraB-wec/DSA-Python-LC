class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1009          # Prime number for fewer collisions
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = self._hash(key)
        if key not in self.buckets[h]:
            self.buckets[h].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = self._hash(key)
        if key in self.buckets[h]:
            self.buckets[h].remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        h = self._hash(key)
        return key in self.buckets[h]