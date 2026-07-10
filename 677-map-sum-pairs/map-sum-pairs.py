class MapSum(object):

    def __init__(self):
        self.mp = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        self.mp[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        total = 0

        for key in self.mp:
            if key.startswith(prefix):
                total += self.mp[key]

        return total