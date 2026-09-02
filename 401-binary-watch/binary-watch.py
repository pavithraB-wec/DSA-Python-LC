class Solution(object):
    def readBinaryWatch(self, turnedOn):
        result = []

        for hour in range(12):
            for minute in range(60):
                # Count set bits in hour and minute
                if self.countBits(hour) + self.countBits(minute) == turnedOn:
                    result.append(str(hour) + ":" + "%02d" % minute)

        return result

    def countBits(self, num):
        count = 0

        while num:
            count += num & 1
            num >>= 1

        return count
