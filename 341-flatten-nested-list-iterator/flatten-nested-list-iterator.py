class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = []

        # Push in reverse order
        for item in reversed(nestedList):
            self.stack.append(item)

    def next(self):
        # hasNext() makes sure the top is an integer
        self.hasNext()

        item = self.stack.pop()
        return item.getInteger()

    def hasNext(self):
        while self.stack:
            item = self.stack[-1]

            # Top is already an integer
            if item.isInteger():
                return True

            # Top is a list
            self.stack.pop()

            nested = item.getList()

            # Push its elements in reverse order
            for child in reversed(nested):
                self.stack.append(child)

        return False