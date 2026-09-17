class MyCalendarTwo(object):

    def __init__(self):
        self.booked = []
        self.overlap = []

    def book(self, startTime, endTime):
        # Check for triple booking
        for start, end in self.overlap:
            if max(startTime, start) < min(endTime, end):
                return False

        # Find new double-booked intervals
        for start, end in self.booked:
            overlap_start = max(startTime, start)
            overlap_end = min(endTime, end)

            if overlap_start < overlap_end:
                self.overlap.append((overlap_start, overlap_end))

        # Add the new event
        self.booked.append((startTime, endTime))

        return True