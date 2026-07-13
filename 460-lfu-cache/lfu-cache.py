from collections import defaultdict, OrderedDict

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.minFreq = 0
        self.keyMap = {}                      # key -> (value, freq)
        self.freqMap = defaultdict(OrderedDict)  # freq -> OrderedDict(keys)

    def _update(self, key, value=None):
        val, freq = self.keyMap[key]
        if value is not None:
            val = value

        # Remove from current frequency
        del self.freqMap[freq][key]

        if not self.freqMap[freq]:
            del self.freqMap[freq]
            if self.minFreq == freq:
                self.minFreq += 1

        # Add to next frequency
        self.freqMap[freq + 1][key] = None
        self.keyMap[key] = (val, freq + 1)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.keyMap:
            return -1

        value = self.keyMap[key][0]
        self._update(key)
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return

        if key in self.keyMap:
            self._update(key, value)
            return

        if len(self.keyMap) == self.capacity:
            old_key, _ = self.freqMap[self.minFreq].popitem(last=False)
            del self.keyMap[old_key]

            if not self.freqMap[self.minFreq]:
                del self.freqMap[self.minFreq]

        self.keyMap[key] = (value, 1)
        self.freqMap[1][key] = None
        self.minFreq = 1