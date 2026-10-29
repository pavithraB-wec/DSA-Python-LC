class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        self.combinations = []

        def backtrack(start, path):
            if len(path) == combinationLength:
                self.combinations.append("".join(path))
                return

            for i in range(start, len(characters)):
                path.append(characters[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        self.index = 0

    def next(self):
        result = self.combinations[self.index]
        self.index += 1
        return result

    def hasNext(self):
        return self.index < len(self.combinations)