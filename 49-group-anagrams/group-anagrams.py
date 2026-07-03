class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = {}

        for s in strs:
            key = "".join(sorted(s))

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())