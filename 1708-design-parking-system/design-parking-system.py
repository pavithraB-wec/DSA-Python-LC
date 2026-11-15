class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.parking = [big, medium, small]

    def addCar(self, carType):
        if self.parking[carType - 1] > 0:
            self.parking[carType - 1] -= 1
            return True

        return False