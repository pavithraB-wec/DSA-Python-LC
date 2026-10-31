class UndergroundSystem(object):

    def __init__(self):
        self.checkins = {}
        self.trips = {}

    def checkIn(self, id, stationName, t):
        self.checkins[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        startStation, startTime = self.checkins.pop(id)

        route = (startStation, stationName)
        travelTime = t - startTime

        if route not in self.trips:
            self.trips[route] = [0, 0]

        self.trips[route][0] += travelTime
        self.trips[route][1] += 1

    def getAverageTime(self, startStation, endStation):
        totalTime, count = self.trips[(startStation, endStation)]
        return float(totalTime) / count