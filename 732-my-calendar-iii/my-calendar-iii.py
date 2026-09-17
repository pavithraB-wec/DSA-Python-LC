class MyCalendarThree(object):

    def __init__(self):
        self.events = {}

    def book(self, startTime, endTime):
        self.events[startTime] = self.events.get(startTime, 0) + 1
        self.events[endTime] = self.events.get(endTime, 0) - 1

        active = 0
        maximum = 0

        for time in sorted(self.events):
            active += self.events[time]
            maximum = max(maximum, active)

        return maximum