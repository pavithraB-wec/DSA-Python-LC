from collections import defaultdict

class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content_map = defaultdict(list)

        for path in paths:
            parts = path.split()
            directory = parts[0]

            for file in parts[1:]:
                i = file.index('(')
                name = file[:i]
                content = file[i + 1:-1]
                full_path = directory + "/" + name
                content_map[content].append(full_path)

        result = []

        for files in content_map.values():
            if len(files) > 1:
                result.append(files)

        return result