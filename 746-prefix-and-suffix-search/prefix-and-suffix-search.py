class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.lookup = {}

        for index, word in enumerate(words):
            m = len(word)

            for i in range(m + 1):
                prefix = word[:i]

                for j in range(m + 1):
                    suffix = word[j:]
                    self.lookup[(prefix, suffix)] = index

    def f(self, pref, suff):
        """
        :type pref: str
        :type suff: str
        :rtype: int
        """
        return self.lookup.get((pref, suff), -1)