class Solution(object):
    def videoStitching(self, clips, time):
        clips.sort()

        count = 0
        current_end = 0
        farthest = 0
        i = 0
        n = len(clips)

        while current_end < time:

            # Find the clip that extends coverage the farthest
            while i < n and clips[i][0] <= current_end:
                farthest = max(farthest, clips[i][1])
                i += 1

            # Cannot extend the covered range
            if farthest == current_end:
                return -1

            # Use one more clip
            count += 1
            current_end = farthest

        return count