from collections import defaultdict

class FreqStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.freq = defaultdict(int)          # value -> frequency
        self.group = defaultdict(list)        # frequency -> stack of values
        self.maxFreq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] += 1
        f = self.freq[val]

        if f > self.maxFreq:
            self.maxFreq = f

        self.group[f].append(val)

    def pop(self):
        """
        :rtype: int
        """
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1

        if not self.group[self.maxFreq]:
            self.maxFreq -= 1

        return val