class LockingTree(object):

    def __init__(self, parent):
        self.parent = parent
        n = len(parent)

        self.children = [[] for _ in range(n)]
        self.locked = [0] * n

        for i in range(1, n):
            self.children[parent[i]].append(i)

    def lock(self, num, user):
        if self.locked[num] != 0:
            return False

        self.locked[num] = user
        return True

    def unlock(self, num, user):
        if self.locked[num] != user:
            return False

        self.locked[num] = 0
        return True

    def upgrade(self, num, user):
        if self.locked[num] != 0:
            return False

        # Check locked ancestors
        p = self.parent[num]

        while p != -1:
            if self.locked[p] != 0:
                return False
            p = self.parent[p]

        # Find and unlock locked descendants
        locked_nodes = []
        stack = self.children[num][:]

        while stack:
            node = stack.pop()

            if self.locked[node] != 0:
                locked_nodes.append(node)

            stack.extend(self.children[node])

        if not locked_nodes:
            return False

        for node in locked_nodes:
            self.locked[node] = 0

        self.locked[num] = user
        return True