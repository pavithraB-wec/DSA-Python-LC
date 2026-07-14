class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1009          # Prime number
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        h = self._hash(key)

        for pair in self.buckets[h]:
            if pair[0] == key:
                pair[1] = value
                return

        self.buckets[h].append([key, value])

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        h = self._hash(key)

        for k, v in self.buckets[h]:
            if k == key:
                return v

        return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        h = self._hash(key)

        bucket = self.buckets[h]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return