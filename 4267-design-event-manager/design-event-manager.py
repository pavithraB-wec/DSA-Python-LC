import heapq

class EventManager(object):

    def __init__(self, events):
        self.heap = []
        self.active = {}

        for eventId, priority in events:
            self.active[eventId] = priority
            heapq.heappush(self.heap, (-priority, eventId))

    def updatePriority(self, eventId, newPriority):
        self.active[eventId] = newPriority
        heapq.heappush(self.heap, (-newPriority, eventId))

    def pollHighest(self):
        while self.heap:
            priority, eventId = heapq.heappop(self.heap)

            if eventId in self.active:
                if self.active[eventId] == -priority:
                    del self.active[eventId]
                    return eventId

        return -1