class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = []

        # Push elements in reverse order
        for item in reversed(nestedList):
            self.stack.append(item)

    def next(self):
        self.hasNext()
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            item = self.stack[-1]

            # If it is an integer, we are ready
            if item.isInteger():
                return True

            # Remove the nested list
            self.stack.pop()

            # Add its elements in reverse order
            for child in reversed(item.getList()):
                self.stack.append(child)

        return False