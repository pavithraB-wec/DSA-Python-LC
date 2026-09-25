class Solution(object):
    def flipAndInvertImage(self, image):
        for row in image:
            row.reverse()

            for i in range(len(row)):
                row[i] = 1 - row[i]

        return image