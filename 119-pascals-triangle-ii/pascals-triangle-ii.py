class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]

        for i in range(1, rowIndex + 1):
            row.append(1)
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]

        return row