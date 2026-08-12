class Solution(object):
    def brokenCalc(self, startValue, target):
        operations = 0

        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1

            operations += 1

        # target is now <= startValue
        return operations + (startValue - target)