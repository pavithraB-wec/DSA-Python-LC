class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]
        """
        result = []
        in_block = False
        newline = []

        for line in source:
            i = 0

            if not in_block:
                newline = []

            while i < len(line):
                if not in_block:
                    if i + 1 < len(line) and line[i:i+2] == "/*":
                        in_block = True
                        i += 2
                    elif i + 1 < len(line) and line[i:i+2] == "//":
                        break
                    else:
                        newline.append(line[i])
                        i += 1
                else:
                    if i + 1 < len(line) and line[i:i+2] == "*/":
                        in_block = False
                        i += 2
                    else:
                        i += 1

            if not in_block and newline:
                result.append("".join(newline))

        return result