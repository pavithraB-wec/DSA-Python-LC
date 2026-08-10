class Solution(object):
    def maxDistance(self, arrays):
        # initialize with first array
        global_min = arrays[0][0]
        global_max = arrays[0][-1]
        max_dist = 0

        for i in range(1, len(arrays)):
            curr_min = arrays[i][0]
            curr_max = arrays[i][-1]

            # compute distance with previous arrays
            max_dist = max(max_dist,
                           abs(curr_max - global_min),
                           abs(global_max - curr_min))

            # update global min and max
            global_min = min(global_min, curr_min)
            global_max = max(global_max, curr_max)

        return max_dist